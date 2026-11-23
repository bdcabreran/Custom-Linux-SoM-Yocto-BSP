# ST datasheets and application notes

The chip documents for the STM32MP257 and the STPMIC25: datasheets, reference manual, errata,
hardware application notes and the EV1 user manual. We use them for the SoM schematic, the pad map
and the device tree.

The PDFs under `docs/08-references/datasheets/` are git-ignored. This README is the tracked pointer.

## Source

| Field | Value |
|---|---|
| What it is | ST PDFs for the STM32MP25 line and the STPMIC25 |
| Lives in | st.com, one link per file in the Files table. Index: https://wiki.st.com/stm32mpu/wiki/STM32MP25_resources |
| Version | Per file, see the Files table. Revisions are the ones st.com listed on 2026-11-23 |
| Owner | STMicroelectronics |

## Fetch

This cannot be scripted. st.com answered HTTP 567 (a block page) to `curl` from this machine on
2026-11-23. Use a browser.

1. Open each link in the Files table and download the PDF.
2. Save it to `docs/08-references/datasheets/` under the file name in the table (the name ST gives it).
3. If the revision on the first page is newer than the one in the table, update the table.

## Files

| File | Document | Revision | Link |
|---|---|---|---|
| `stm32mp257f.pdf` | DS14284, STM32MP25xC/F datasheet: packages, ball map, electrical limits, boot pins | Rev 5, April 2025 | https://www.st.com/resource/en/datasheet/stm32mp257f.pdf |
| `stpmic25.pdf` | DS14278, STPMIC25 datasheet | Rev 7, October 2026 | https://www.st.com/resource/en/datasheet/stpmic25.pdf |
| `es0598-stm32mp23xx25xx-device-errata-stmicroelectronics.pdf` | ES0598, device errata | Rev 6, May 2026 | https://www.st.com/resource/en/errata_sheet/es0598-stm32mp23xx25xx-device-errata-stmicroelectronics.pdf |
| `an5489-getting-started-with-stm32mp25x-mpus-hardware-development-stmicroelectronics.pdf` | AN5489, hardware getting started: power, clocks, reset, boot, reference schematics | Rev 7, September 2026 | https://www.st.com/resource/en/application_note/an5489-getting-started-with-stm32mp25x-mpus-hardware-development-stmicroelectronics.pdf |
| `an5724-stm32mp25xx-hardware-design-guidelines-stmicroelectronics.pdf` | AN5724, DDR routing guidelines for STM32MP2 | record on download | https://www.st.com/resource/en/application_note/an5724-stm32mp25xx-hardware-design-guidelines-stmicroelectronics.pdf |
| `an6115-stpmic25-application-hints-stmicroelectronics.pdf` | AN6115, STPMIC25 application hints, unused pins | Rev 2, November 2024 | https://www.st.com/resource/en/application_note/an6115-stpmic25-application-hints-stmicroelectronics.pdf |
| `an6116-the-stpmic25-bom-details-stmicroelectronics.pdf` | AN6116, STPMIC25 recommended parts | record on download | https://www.st.com/resource/en/application_note/an6116-the-stpmic25-bom-details-stmicroelectronics.pdf |
| `an6128-the-stpmic25-pcb-layout-guidelines-stmicroelectronics.pdf` | AN6128, STPMIC25 PCB layout guidelines | Rev 1, June 2024 | https://www.st.com/resource/en/application_note/an6128-the-stpmic25-pcb-layout-guidelines-stmicroelectronics.pdf |
| `DB_stm32mp257f-ev1.pdf` | DB5260, EV1 data brief: feature list and ordering codes | Rev 1, June 2024 | https://www.st.com/resource/en/data_brief/stm32mp257f-ev1.pdf |
| `um3359-evaluation-board-with-stm32mp257f-mpu-stmicroelectronics.pdf` | UM3359, EV1 user manual: block diagram, power tree, boot switches, connectors | Rev 7, September 2026 | https://www.st.com/resource/en/user_manual/um3359-evaluation-board-with-stm32mp257f-mpu-stmicroelectronics.pdf |

## What depends on it

- `docs/05-hardware/soc-selection.md` - the package, DDR and interface facts come from DS14284 and AN5489

## Open

- RM0457, the STM32MP23/25 reference manual: the direct PDF link is not recorded yet. Get it from
  https://www.st.com/en/microcontrollers-microprocessors/stm32mp2-series/documentation.html, save it
  here and add its row to the Files table.
