"""Draw the STM32MP257 TFBGA436 ball map as an SVG, colored by what each ball does on the EV1.

Usage: python3 -I ball_map_svg.py <netlist.txt> <out.svg> [refdes, default U27]
The netlist is the tab-separated file written by odb_netlist.py.
"""
import re
import sys
from collections import Counter

netlist, out = sys.argv[1], sys.argv[2]
ref = sys.argv[3] if len(sys.argv) > 3 else "U27"

ROWS = "A B C D E F G H J K L M N P R T U V W Y AA AB".split()
COLS = list(range(1, 23))

GROUPS = [  # key, label, fill, text color
    ("disp", "Display and camera (DSI, CSI-2, LVDS, control)", "#15803d", "#e5e7eb"),
    ("eth", "Ethernet (3x RGMII, MDIO)", "#0e7490", "#e5e7eb"),
    ("usb", "USB and PCIe", "#7c3aed", "#e5e7eb"),
    ("stor", "Storage (SD, eMMC, NOR flash)", "#b45309", "#e5e7eb"),
    ("io", "Low-speed I/O and system (GPIO, UART, I2C, SPI, CAN, JTAG, boot, clocks)", "#94a3b8", "#0f172a"),
    ("ddr", "DDR4, stays on the SoM", "#475569", "#e5e7eb"),
    ("pwr", "Power and ground", "#1e293b", "#94a3b8"),
    ("nc", "Not connected on the EV1", "#0f172a", "#94a3b8"),
]


def classify(net):
    if net == "$NONE$":
        return "nc"
    if net.startswith("DDR_"):
        return "ddr"
    if re.match(r"(DSI|CSI|LVDS1|DISP|HDMI)[._]|CAM_", net):
        return "disp"
    if net.startswith("ETH"):
        return "eth"
    if re.match(r"USB|UCPD|PCIE|COMBOTX|VBUS_DIV|TCPP", net):
        return "usb"
    if re.match(r"SD\.|eMMC\.|QSPI1\.|GPIO\.SDMMC3", net):
        return "stor"
    if net == "GND" or re.match(r"VDD|1V8|3V3|VBAT|VREF|Net", net):
        return "pwr"
    return "io"


balls = {}
for line in open(netlist, encoding="utf-8"):
    if line.startswith("#"):
        continue
    net, r, pin, _ = line.rstrip("\n").split("\t")
    if r == ref:
        balls[pin] = classify(net)

count = Counter(balls.values())
P, X0, Y0, RAD = 27, 70, 96, 11
W = X0 + P * len(COLS) + 30
H = Y0 + P * len(ROWS) + 40 + 22 * len(GROUPS)
color = {k: (f, t) for k, _, f, t in GROUPS}

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Arial, sans-serif">']
s.append(f'<rect width="{W}" height="{H}" fill="#0f172a"/>')
s.append(f'<text x="{W / 2}" y="30" fill="#e5e7eb" font-size="15" font-weight="bold" text-anchor="middle">STM32MP257FAI3 ball map, colored by use on the EV1 (MB1936 rev E01)</text>')
s.append(f'<text x="{W / 2}" y="50" fill="#94a3b8" font-size="12" text-anchor="middle">TFBGA436, 22 x 22 grid, 0.8 mm pitch. Ball A1 is at the top left. Colors are named in the legend.</text>')
for j, c in enumerate(COLS):
    s.append(f'<text x="{X0 + j * P}" y="{Y0 - 20}" fill="#94a3b8" font-size="11" text-anchor="middle">{c}</text>')
for i, r in enumerate(ROWS):
    y = Y0 + i * P
    s.append(f'<text x="{X0 - 26}" y="{y + 4}" fill="#94a3b8" font-size="11" text-anchor="middle">{r}</text>')
    for j, c in enumerate(COLS):
        g = balls.get(f"{r}{c}")
        if g is None:
            continue
        fill, _ = color[g]
        stroke = "#475569" if g in ("pwr", "nc") else fill
        s.append(f'<circle cx="{X0 + j * P}" cy="{y}" r="{RAD}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
ly = Y0 + P * len(ROWS) + 14
for k, label, fill, _ in GROUPS:
    s.append(f'<circle cx="{X0 - 20}" cy="{ly - 4}" r="8" fill="{fill}" stroke="#475569" stroke-width="1"/>')
    s.append(f'<text x="{X0}" y="{ly}" fill="#e5e7eb" font-size="12">{label}: {count[k]} balls</text>')
    ly += 22
s.append("</svg>")
open(out, "w", encoding="utf-8").write("\n".join(s) + "\n")
print(f"balls={len(balls)}", dict(count))
missing = [f"{r}{c}" for r in ROWS for c in COLS if f"{r}{c}" not in balls]
print(f"grid positions without a ball: {len(missing)}")
