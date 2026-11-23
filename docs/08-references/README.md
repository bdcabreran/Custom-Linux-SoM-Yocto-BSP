# References

Source material the SoM and the BSP are designed against, kept next to the repo so a question gets
answered from the real document instead of from memory. This is the lookup library for whoever works
on the project, the engineer and the coding agent alike.

What lives here: the ST reference board designs we copy from, and the chip documents. Nothing here is
built, and nothing is edited in place. Our own schematics and layout stay in the private hardware
repo, not here.

## Where to look

| Question | Open |
|---|---|
| How does ST connect the STM32MP257 in our package to DDR4, the PMIC, eMMC, Ethernet, DSI, CSI or CAN? | `ev1-mb1936/` - the schematic PDF first |
| Which exact part did ST fit, and what are its value and footprint? | `ev1-mb1936/bom/` |
| How did ST route the DDR4 and the PMIC, and what is the stackup? | `ev1-mb1936/board-design/` (Altium project) and `ev1-mb1936/manufacturing/` |
| What is wired to which net or pin on the EV1? | `ev1-mb1936/mb1936-e01-netlist.txt` - grep the net name or the reference (`U27` is the MPU, `U26` the PMIC) |
| How does ST connect LPDDR4, or the camera and LVDS circuits on the small package? | `dk-mb1605/` |
| What is the ball map, the electrical limit, the boot pin table? | `datasheets/stm32mp257f.pdf` (DS14284) |
| How do I design the power, clock, reset and boot circuits? | `datasheets/` - AN5489 |
| What are the DDR routing rules? | `datasheets/` - AN5724 |
| Which STPMIC25 variant, which parts around it, how to lay it out? | `datasheets/` - DS14278, AN6115, AN6116, AN6128 |
| Is this a known chip bug? | `datasheets/` - ES0598 errata sheet |
| How does a peripheral register work? | `datasheets/` - RM0457 reference manual |

## How to use it

1. Before answering anything about the chip or the reference board, open the table above and pick the
   row.
2. If a folder looks empty, it is git-ignored on purpose. Follow the fetch steps in that folder's
   README.
3. Search text with `rg`. A netlist is plain text, so grep the net name. Read a PDF by page range, not
   whole.
4. Say which file and which section, page, or net you used.
5. If nothing here answers it, say so instead of guessing.
6. If you had to hunt for it, add a row to the table above. That is what keeps this useful.

## What is tracked

The material is large, and it belongs to ST under its own license, so the payload is git-ignored and
a small README is tracked in its place. This repo is public: never commit the ST files themselves.

| Folder | Holds | Comes from | Tracked |
|---|---|---|---|
| `ev1-mb1936/` | STM32MP257F-EV1 schematic, Altium project, BOM, manufacturing files | st.com product page | README only |
| `dk-mb1605/` | STM32MP257F-DK schematic | st.com product page | README only |
| `datasheets/` | Datasheets, reference manual, errata, application notes, user manual | st.com | README only |
| `ref-framework/` | The pointer README template the `/references` skill follows | this repo | yes, it is the kit |

## Adding something

Only material that stays put: datasheets, schematics, vendor examples, toolchains. Requirements and
anything else that moves as the project runs belong in `docs/01-requirements/`.

Put it in the folder that matches where it came from. If none fits, add a folder with its own README
on the same pattern. Then add a row to the "Where to look" table with the question it answers.

Run `/references add <folder>` rather than doing it by hand - it writes the README from the template,
wires the ignore rules, adds both table rows, and tests the link before recording it as fetchable.
