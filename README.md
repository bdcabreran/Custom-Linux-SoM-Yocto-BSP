# Custom Linux SoM - Yocto BSP

Firmware and Linux BSP for a custom System-on-Module (SoM) with castellated pads and its carrier board.

The SoM and carrier are designed in-house. This repo holds the firmware side: Yocto layer, bootloader, kernel and device tree, plus demo apps for 3D graphics, display and camera.

> Hardware design files (schematics, layout) are private. Block diagrams, pin maps and bring-up notes are shared in [`docs/hardware`](docs/hardware). Design files are available on request.

## Target features

| Function | Target |
|---|---|
| CPU | Arm Cortex-A, embedded Linux (Yocto) |
| Graphics | 3D GPU, OpenGL ES 3.x / Vulkan |
| Display | MIPI DSI or parallel RGB, with touch |
| Camera | MIPI CSI-2 |
| Storage | eMMC on SoM, microSD on carrier |
| Network | Gigabit Ethernet (PHY on SoM) |
| I/O | GPIO, I2C, SPI, UART, CAN for peripherals |
| Module | Castellated pads, single 5 V input, PMIC on SoM |

## Status

- [ ] SoC selection
- [ ] Pad map (SoM to carrier)
- [ ] SoM and carrier design
- [ ] Board bring-up (power, DDR, first boot)
- [ ] Yocto BSP (U-Boot, kernel, device tree)
- [ ] Display, camera and 3D demos

## SoC candidates

| SoC | 3D GPU | Display | Camera | Notes |
|---|---|---|---|---|
| TI AM62x | PowerVR AXE-1-16M, GLES 3.1 | RGB, LVDS | CSI-2 4-lane | 0.8 mm pitch, also as Octavo OSD62x SiP |
| TI AM62P | PowerVR, about 3x AM62x | DSI, LVDS, RGB | CSI-2 | 32-bit LPDDR4 |
| STM32MP257 | GLES 3.1, Vulkan 1.3 | DSI, LVDS, RGB | CSI-2 with ISP | 0.8 mm pitch, NPU |
| Rockchip RK3566 | Mali-G52, GLES 3.2 | DSI, RGB, LVDS, HDMI | CSI-2 with ISP | Low cost |
| NXP i.MX 8M Plus | GC7000UL, GLES 3.1 | DSI, LVDS, HDMI | 2x CSI with ISP | 0.5 mm pitch, NPU |

Full comparison: [`docs/soc-selection.md`](docs/soc-selection.md).

## Repo layout

```
docs/             SoC selection, hardware overview, bring-up notes
meta-custom-som/  Yocto layer (machine config, recipes)
u-boot/           Bootloader patches and board config
linux/            Kernel config, device tree, drivers
apps/             3D, display and camera demo apps
```

## Roles

- Firmware, BSP, SoC selection, pin mapping and bring-up: [@bdcabreran](https://github.com/bdcabreran)
- Schematics and PCB layout: (HW engineer)
