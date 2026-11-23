# SoC selection

Goal: a SoC with a 3D GPU, display and camera interfaces, Ethernet, SD and enough GPIO, that can be routed on a castellated SoM without HDI.

## Decision (2026-11-23)

**STM32MP257**, part `STM32MP257FAI3`: TFBGA436, 18 x 18 mm, 0.8 mm pitch, 172 GPIO, dual Cortex-A35 at 1.5 GHz plus a Cortex-M33.

Why this one:

- It is the only candidate that has DSI, CSI-2 with ISP, Gigabit Ethernet, CAN FD and a GLES 3.1 / Vulkan GPU, all native, on a 0.8 mm pitch package.
- ST lists the 18 x 18 mm package for a 4-layer board with plain through-hole vias, so no HDI. ST's own EV1 board uses 6 layers, also with through-hole vias only.
- ST maintains the Yocto BSP (`meta-st-stm32mp`), TF-A, OP-TEE, U-Boot and the kernel.
- The ST evaluation board uses the same part, so its schematic is a direct reference for the SoM.

Known limits:

- CSI-2 has 2 data lanes only. Pick the camera sensor with that in mind.
- The GPU driver is a vendor binary under the ST EULA, not open source.
- DDR is limited to 4 GB.

Still open on the hardware side:

- DDR type: 2x 16-bit DDR4 (as on the EV1) or LPDDR4 (as on the DK).
- STPMIC25 variant. It depends on the DDR type and the I/O voltage, see AN5489 section 8.5.
- Display panel and camera sensor part numbers.
- Pad map, SoM to carrier.

## ST reference material

| Item | What it gives |
|---|---|
| [STM32MP257F-EV1](https://www.st.com/en/evaluation-tools/stm32mp257f-ev1.html) (board MB1936) | Main reference. Same `STM32MP257FAI3`, STPMIC25, 2x 16-bit DDR4, eMMC, microSD, Gigabit Ethernet, DSI, CSI-2, CAN FD. Schematic PDF, Altium project, BOM and manufacturing files are on the product page |
| [STM32MP257F-DK](https://www.st.com/en/evaluation-tools/stm32mp257f-dk.html) (board MB1605) | Uses the 14 x 14 mm, 0.5 mm pitch package, so not a layout reference. Useful for its LPDDR4 and camera circuits |
| [AN5489](https://www.st.com/resource/en/application_note/an5489-getting-started-with-stm32mp25x-mpus-hardware-development-stmicroelectronics.pdf) | Getting started with STM32MP23/25xx hardware: power, clocks, reset, boot pins, reference schematics |
| [AN5724](https://www.st.com/resource/en/application_note/an5724-stm32mp25xx-hardware-design-guidelines-stmicroelectronics.pdf) | DDR routing guidelines for STM32MP2 |
| AN6115, AN6116, AN6128 | STPMIC25 application hints, BOM details and PCB layout. Linked from the [STM32MP25 resources](https://wiki.st.com/stm32mpu/wiki/STM32MP25_resources) wiki page |
| [DS14284](https://www.st.com/resource/en/datasheet/stm32mp257f.pdf) | Datasheet: packages, ball map, electrical limits |

The ST board files come under ST's Open Platform License Agreement (www.st.com/opla). Read it before reusing them.

## Candidates

| SoC | 3D GPU | Display | Camera | Ethernet | Routing |
|---|---|---|---|---|---|
| TI AM62x (AM625) | PowerVR AXE-1-16M, GLES 3.1 / Vulkan, about 16 GFLOPS | RGB 24-bit, 2x LVDS, no DSI | CSI-2 4-lane, no ISP | 2x GbE with switch | Easiest. 0.8 mm pitch package, 16-bit DDR. Octavo OSD62x SiP has DDR and passives inside |
| TI AM62P | PowerVR, about 3x AM62x | DSI, LVDS, RGB | CSI-2 | 2x GbE | Medium-hard, 32-bit LPDDR4 |
| STM32MP257 | GLES 3.1 / Vulkan 1.3, 900 MHz (GPU is optional, check part number) | DSI 4-lane, LVDS, RGB | CSI-2 2-lane with ISP | 3x GbE (2 + 1 switch, TSN) | Medium. 0.8 mm pitch TFBGA361 (16 x 16) or TFBGA436 (18 x 18). The 10 x 10 and 14 x 14 packages are 0.5 mm |
| Rockchip RK3566/3568 | Mali-G52, GLES 3.2 / Vulkan 1.1 | RGB, DSI, LVDS, eDP, HDMI | CSI-2 4-lane with ISP | 1x / 2x GbE | Medium-hard. Many stamp-hole modules exist to compare |
| NXP i.MX 8M Plus | GC7000UL, GLES 3.1 / Vulkan | DSI, LVDS, HDMI, no RGB | 2x CSI with ISP | 2x GbE | Hard. 0.5 mm pitch, 8+ layers |

Not suitable: i.MX 8M Mini (GLES 2.0 only), STM32MP15 (GLES 2.0, parallel camera only), i.MX 93 and AM62A (no 3D GPU), Allwinner T113 (no GPU).

## Prices (chip only, checked 2026-10-07)

| SoC | 1 pc | Volume | Source |
|---|---|---|---|
| RK3566 | $14.65 | $9.84 (102+) | LCSC |
| AM62P54 | - | $26.14 (1k) | ti.com |
| RK3568 | $29.57 | $23.21 (490+) | LCSC |
| STM32MP257FAI3 | $32.09 | about $21.71 (100) | DigiKey |
| AM6254 | $32.63 | $22.99 (119) | DigiKey |
| Octavo OSD6254-1G (AM625 + 1 GB DDR4) | $36.56 | $24.68 (100+) | DigiKey |
| i.MX 8M Plus (MIMX8ML8DVNLZAB) | $48.27 | $32.18 (252) | DigiKey |

Bare SoCs still need DDR, PMIC, eMMC and crystal, roughly $10-25 more.

## Pad budget (castellated, rough)

| Group | Pads |
|---|---|
| Display, DSI 4-lane + backlight + touch | ~16 (RGB24: ~34) |
| Camera, CSI + I2C + reset + MCLK | 10-14 |
| SD 4-bit | ~8 |
| Ethernet MDI (PHY on SoM) | ~10 |
| USB2 x2 | ~6 |
| Boot mode, reset, power button, debug UART | ~7 |
| GPIO, I2C, SPI, UART, CAN | 30-40 |
| Ground | ~20% of all pads |

Total about 130-150 pads with DSI. At 1 mm pitch that needs roughly a 50-55 mm square module.

This was the first rough budget. The signal-by-signal draft is in [som-pad-map.md](som-pad-map.md) and comes to 160 pads.

## Design notes

- MIPI DSI/CSI up to 2.5 Gbps per lane can go through castellations if short, 100 ohm differential, with GND pads between pairs.
- Keep USB3, PCIe and HDMI off the castellations, or use LGA pads for them.
- One 5 V input, PMIC on the SoM.
- SGET OSM (solder-down LGA standard) is a useful pinout reference.
