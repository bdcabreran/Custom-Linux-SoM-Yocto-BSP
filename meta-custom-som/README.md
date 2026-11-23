# meta-custom-som

Yocto layer for the custom SoM and carrier. The SoC is the STM32MP257F, so this layer sits on top of ST's `meta-st-stm32mp` (branch `scarthgap`, OpenSTLinux 6.2).

Machine: `custom-som-mp257`. Until our own device tree exists it builds the STM32MP257F-EV1 device trees, so the image runs on an EV1 board. It has not been built yet.

The GPU driver is a vendor binary. To enable it, add `ACCEPT_EULA_custom-som-mp257 = "1"` to `local.conf`.

| Folder | What goes here |
|---|---|
| `conf/machine/` | Machine config for the SoM + carrier |
| `recipes-bsp/u-boot/` | U-Boot board config and patches |
| `recipes-kernel/linux/` | Kernel config fragments, device tree, driver patches |
| `recipes-graphics/` | GPU driver and 3D stack (Mesa or vendor driver) |
| `recipes-multimedia/camera/` | Camera sensor driver and pipeline config |
| `recipes-core/images/` | Image recipes (dev image, demo image) |
| `recipes-apps/` | Recipes for the demo apps in `../apps` |
