# STM32MP257F-DK board design (MB1605)

ST's Discovery kit for the STM32MP257. It uses the 14 x 14 mm, 0.5 mm pitch package
(`STM32MP257FAK3`), so it is not a layout reference for our SoM. We use it as a second example for
LPDDR4 and for the camera and LVDS circuits.

The ST files under `docs/08-references/dk-mb1605/` are git-ignored. This README is the tracked
pointer.

## Source

| Field | Value |
|---|---|
| What it is | Schematic PDF of the MB1605 main board. Design project, BOM and manufacturing ZIPs are on the same page |
| Lives in | https://www.st.com/en/evaluation-tools/stm32mp257f-dk.html, section "CAD resources" |
| Version | Schematic MB1605-MP257F-C01 (board revision C01), dated 18 Oct 2024 on st.com |
| Owner | STMicroelectronics |
| License | ST Open Platform License Agreement, www.st.com/opla. Do not commit or redistribute the files |

## Fetch

This cannot be scripted. st.com answered HTTP 567 (a block page) to `curl` from this machine on
2026-11-23. Use a browser.

1. Download the schematic:
   https://www.st.com/resource/en/schematic_pack/mb1605-mp257f-c01-schematic.pdf
2. Save it to `docs/08-references/dk-mb1605/` as `mb1605-mp257f-c01-schematic.pdf`.
3. Only if the LPDDR4 layout is needed: download "MB1605 Board design project files" (ZIP) from the
   product page, save it here as ST names it (`mb1605*.zip`) and unzip it into `board-design/`.

## What depends on it

- `docs/05-hardware/soc-selection.md` - lists this board as the LPDDR4 and camera reference
