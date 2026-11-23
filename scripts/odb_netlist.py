"""Build a flat netlist (net, refdes, pin, part) from an ODB++ step folder.

Usage: python3 -I odb_netlist.py <odb/steps/pcb> <out.txt> <source label>
"""
import re
import sys
from pathlib import Path

step, out, label = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]

nets = []
for line in (step / "eda" / "data").read_text(encoding="latin-1").splitlines():
    if line.startswith("NET "):
        nets.append(line[4:].split(";")[0].strip())

rows = []
parts = 0
for side in ("comp_+_top", "comp_+_bot"):
    f = step / "layers" / side / "components"
    if not f.exists():
        continue
    refdes, mpn = None, ""
    pending = []
    def flush():
        for net, pin in pending:
            rows.append((net, refdes, pin, mpn))
    for line in f.read_text(encoding="latin-1").splitlines():
        if line.startswith("CMP "):
            if refdes is not None:
                flush()
            fields = line.split(";")[0].split()
            refdes, mpn, pending = fields[6], "", []
            parts += 1
        elif line.startswith("PRP Manufacturer_Part_Number "):
            m = re.search(r"'(.*)'", line)
            mpn = m.group(1).strip() if m else ""
        elif line.startswith("TOP ") and refdes is not None:
            fields = line.split(";")[0].split()
            pending.append((nets[int(fields[6])], fields[8]))
    if refdes is not None:
        flush()

def key(r):
    return (r[0], [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", r[1])], r[2])

rows.sort(key=key)
with out.open("w", encoding="utf-8") as fh:
    fh.write(f"# Netlist derived from {label}\n")
    fh.write("# Not an ST file: built from the ODB++ data with odb_netlist.py. Check against the schematic PDF.\n")
    fh.write(f"# {len(nets)} nets, {parts} parts, {len(rows)} pins\n")
    fh.write("# net\trefdes\tpin\tpart number\n")
    for r in rows:
        fh.write("\t".join(r) + "\n")
print(f"nets={len(nets)} parts={parts} pins={len(rows)} unconnected={sum(1 for r in rows if r[0] == '$NONE$')}")
