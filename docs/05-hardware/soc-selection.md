# SoC selection

Goal: a SoC with a 3D GPU, display and camera interfaces, Ethernet, SD and enough GPIO, that can be routed on a castellated SoM without HDI.

## Candidates

| SoC | 3D GPU | Display | Camera | Ethernet | Routing |
|---|---|---|---|---|---|
| TI AM62x (AM625) | PowerVR AXE-1-16M, GLES 3.1 / Vulkan, about 16 GFLOPS | RGB 24-bit, 2x LVDS, no DSI | CSI-2 4-lane, no ISP | 2x GbE with switch | Easiest. 0.8 mm pitch package, 16-bit DDR. Octavo OSD62x SiP has DDR and passives inside |
| TI AM62P | PowerVR, about 3x AM62x | DSI, LVDS, RGB | CSI-2 | 2x GbE | Medium-hard, 32-bit LPDDR4 |
| STM32MP257 | GLES 3.1 / Vulkan 1.3, 900 MHz (GPU is optional, check part number) | DSI 4-lane, LVDS, RGB | CSI-2 2-lane with ISP | 2x GbE (TSN) | Medium. 0.8 mm pitch TFBGA361/436 |
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

## Design notes

- MIPI DSI/CSI up to 2.5 Gbps per lane can go through castellations if short, 100 ohm differential, with GND pads between pairs.
- Keep USB3, PCIe and HDMI off the castellations, or use LGA pads for them.
- One 5 V input, PMIC on the SoM.
- SGET OSM (solder-down LGA standard) is a useful pinout reference.
