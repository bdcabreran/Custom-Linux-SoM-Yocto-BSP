# Custom Linux SoM - Documentation

Documentation hub for the custom SoM, its carrier board and the Yocto BSP. Each topic lives in its own numbered folder. To add a new doc, use the `new-doc` Claude skill - it places the file in the right folder and updates this index.

> See the repository [README.md](../README.md) for the project overview.

## Folder map

| # | Folder | What goes here |
|---|---|---|
| 01 | [requirements](01-requirements/) | Target features, interfaces, performance goals |
| 02 | [architecture](02-architecture/) | Boot flow, software stack, SoM to carrier split |
| 03 | [features](03-features/) | Per-feature notes: display, camera, 3D, Ethernet, GPIO |
| 04 | [ide-setup](04-ide-setup/) | Yocto build host, VS Code, debug setup |
| 05 | [hardware](05-hardware/) | SoC selection, block diagram, pad map, bring-up notes |
| 06 | [testing](06-testing/) | Bring-up checklists, interface tests, benchmarks |
| 07 | [deployment](07-deployment/) | Image build, flashing, SD and eMMC boot |
| 08 | [references](08-references/) | External docs and links (datasheets stay local, not committed) |
| 09 | [issues](09-issues/) | Bug tracker, open questions |

## Index

### 01 - Requirements
*(No documents yet)*

### 02 - Architecture
*(No documents yet)*

### 03 - Features
*(No documents yet)*

### 04 - IDE setup
*(No documents yet)*

### 05 - Hardware
- [soc-selection.md](05-hardware/soc-selection.md) - SoC decision (STM32MP257), ST reference designs, candidates, prices, castellated pad budget and design notes
- [som-pad-map.md](05-hardware/som-pad-map.md) - Draft 1 of the SoM to carrier pad map: 160 pads, signal groups, EV1 balls and open decisions
- [ev1-reference-block-diagram.md](05-hardware/ev1-reference-block-diagram.md) - Block diagram, buses and power tree of ST's EV1 reference board, built from its netlist
- [hw-framework/hw-docs-standard.md](05-hardware/hw-framework/hw-docs-standard.md) - The standard the hardware docs follow

### 06 - Testing
*(No documents yet)*

### 07 - Deployment
*(No documents yet)*

### 08 - References
- [README.md](08-references/README.md) - Lookup table: which reference file answers which question
- [ev1-mb1936/README.md](08-references/ev1-mb1936/README.md) - STM32MP257F-EV1 schematic, Altium project, BOM and manufacturing files (pointer, files stay local)
- [dk-mb1605/README.md](08-references/dk-mb1605/README.md) - STM32MP257F-DK schematic (pointer, files stay local)
- [datasheets/README.md](08-references/datasheets/README.md) - ST datasheets, errata, application notes and user manual (pointer, files stay local)

### 09 - Issues
*(No documents yet)*
