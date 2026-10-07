# meta-custom-som

Yocto layer for the custom SoM and carrier.

| Folder | What goes here |
|---|---|
| `conf/machine/` | Machine config for the SoM + carrier |
| `recipes-bsp/u-boot/` | U-Boot board config and patches |
| `recipes-kernel/linux/` | Kernel config fragments, device tree, driver patches |
| `recipes-graphics/` | GPU driver and 3D stack (Mesa or vendor driver) |
| `recipes-multimedia/camera/` | Camera sensor driver and pipeline config |
| `recipes-core/images/` | Image recipes (dev image, demo image) |
| `recipes-apps/` | Recipes for the demo apps in `../apps` |
