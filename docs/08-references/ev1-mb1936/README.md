# STM32MP257F-EV1 board design (MB1936)

ST's evaluation board for the STM32MP257. It uses the same `STM32MP257FAI3` part as our SoM (TFBGA436,
0.8 mm pitch) with the STPMIC25APQR, two 16-bit DDR4 chips, eMMC, microSD, Gigabit Ethernet, DSI,
CSI-2 and CAN FD. It is the main reference for our SoM schematic and layout.

The ST files under `docs/08-references/ev1-mb1936/` are git-ignored. This README is the tracked
pointer.

## Source

| Field | Value |
|---|---|
| What it is | Schematic PDFs, Altium board design project, BOM and manufacturing files of the MB1936 main board |
| Lives in | https://www.st.com/en/evaluation-tools/stm32mp257f-ev1.html, section "CAD resources" |
| Version | Board revision E01 is current (schematic dated 27 Nov 2025). The three ZIP packages are version 3.0, dated 11 Dec 2025 in their `readme.txt`, and hold revisions D and E |
| Owner | STMicroelectronics |
| License | ST Open Platform License Agreement, www.st.com/opla. Do not commit or redistribute the files |

## Fetch

This cannot be scripted. st.com answered HTTP 567 (a block page) to `curl` from this machine on
2026-11-23, and the ZIP files ask you to accept the ST license first. Use a browser.

1. Open the product page above and go to "CAD resources".
2. Download the schematic PDFs and the three ZIP files. Keep the file names ST gives them:
   `mb1936-mp257f-x-e01-schematic.pdf`, `mb1936-schematics.pdf`, `mb1936-mp257f-x-d01-schematic.pdf`,
   `mb1936-bdp.zip`, `mb1936-bom.zip`, `mb1936-manufacturing.zip`.
3. Save them to `docs/08-references/ev1-mb1936/`.
4. From the repo root, unzip each ZIP into its own folder and rebuild the netlist:

   ```sh
   cd docs/08-references/ev1-mb1936
   unzip -d board-design   mb1936-bdp.zip
   unzip -d bom            mb1936-bom.zip
   unzip -d manufacturing  mb1936-manufacturing.zip
   tar -xzf manufacturing/MB1936E/ODB++/MB1936E.tgz -C manufacturing/MB1936E/ODB++
   python3 ../../../scripts/odb_netlist.py manufacturing/MB1936E/ODB++/odb/steps/pcb \
       mb1936-e01-netlist.txt "MB1936E ODB++ (ST manufacturing files 3.0, board revision E01)"
   ```

## Files

| File or folder | What it is |
|---|---|
| `mb1936-mp257f-x-e01-schematic.pdf` | Schematic, revision E, 27 Nov 2025, 22 pages. The current one, use this |
| `mb1936-schematics.pdf` | Schematic, revision D, 21 May 2025 (the D02 BOM update). Kept for comparison |
| `mb1936-mp257f-x-d01-schematic.pdf` | Schematic, revision D, 16 May 2024 (D01). Kept for comparison |
| `mb1936-e01-netlist.txt` | Text netlist of revision E01: one line per pin with net, reference, pin and part number. 673 nets, 852 parts, 3452 pins. Not an ST file, we build it from the ODB++ data |
| `board-design/MB1936E/Altium_Designer/` | Altium project of revision E: `MB1936.PrjPcb`, `MB1936.PcbDoc` and 19 `.SchDoc` sheets |
| `board-design/MB1936D/` | The same for revision D |
| `bom/` | `MB1936-MP257F_X-E01_BOM.xlsx` (current), plus the D01 and D02 BOMs |
| `manufacturing/MB1936E/` | Revision E: `Gerber/`, `Assembly/` (pick and place, assembly PDF), `Mechanical/` (STEP, dimensions), `ODB++/` |
| `manufacturing/MB1936D/` | The same for revision D |
| `mb1936-bdp.zip`, `mb1936-bom.zip`, `mb1936-manufacturing.zip` | The packages as downloaded |

## What we read from it so far

- The EV1 is a 6-layer board with through-hole vias only: the ODB++ data has six signal layers and one
  plated drill span, top to bottom. So no HDI, but two layers more than the 4 that ST lists as
  possible for this package.
- The PMIC is the `STPMIC25APQR` and the DDR4 chips are `MT40A1G16TB-062E IT:F` (U28, U29).

## What depends on it

- `docs/05-hardware/soc-selection.md` - names this board as the main reference for the SoM
- `meta-custom-som/conf/machine/custom-som-mp257.conf` - builds the EV1 device trees until our own exist
- `docs/05-hardware/ev1-reference-block-diagram.md` - block diagram, buses and power tree read from the E01 netlist
- `scripts/odb_netlist.py` - builds the text netlist from the ODB++ data in `manufacturing/`

## Open

- The netlist is derived, not exported from Altium. A spot check against the schematic passed (the
  MPU has 436 pins, `DDR_CLK_P` reaches both DDR4 chips and the 100 ohm resistor R270), but it has
  not been compared line by line. If the HW engineer exports one from Altium, keep that one too.
