# Hardware docs standard

Every board revision gets exactly two firmware-side hardware docs, always with these names:

- `docs/05-hardware/hardware-block-diagram.md` - what is on the board and how it is wired, at
  block level. The map a new firmware engineer reads first.
- `docs/05-hardware/pinout-<mcu>.md` (e.g. `pinout-esp32s3.md`) - every wired MCU pin, from the
  firmware side. The file the code's pin definitions are checked against.

This standard is project-agnostic; the project-specific seam (board identity, where the schematic
sources live) is `.claude/rules/hardware-docs.md`. Scaffolding is automated by the
`hw-block-diagram` and `hw-pinout` skills, which follow this file.

## Source of truth

The HW team's schematic is the source; these docs reconcile against it and never invent wiring.

- Each doc states, at the top, the schematic file name, revision, and date it was read from.
- A conflict between the schematic and the firmware architecture (a missing gate, a moved pin) is
  logged in the issues tracker, not silently patched in either place.
- When the schematic revs, update both docs in the same change and fill the delta table in the
  pinout doc.

## Template: hardware-block-diagram.md

Section order is fixed:

1. **Title + scope note** - board name and revision, which schematic file this describes.
2. **At a glance** - one table, <= 12 rows: MCU, power input, each major subsystem in one line.
3. **System block diagram** - one rendered SVG (see diagram rules). Bus colors named in a caption.
4. **Buses** - one table: bus, MCU side, devices (with I2C addresses where they exist).
5. **Power** - the power-tree SVG plus one rails table: rail, source, feeds, current notes from
   the schematic.
6. **Numbered block sections** - one short section per functional block that exists on the board
   (MCU, motor drive, sensors, connectivity, UI, ...). Prose says what the firmware needs to know:
   parts, key values (dividers, trip currents), quirks. Do not re-draw the schematic.
7. **Open items** - what the schematic leaves unresolved, one bullet each.
8. **Component references** - datasheet links for the main ICs.

## Template: pinout-<mcu>.md

Section order is fixed:

1. **Header block** - board + revision, schematic file, MCU part, framework, programming path.
2. **Purpose** - two or three sentences: which board, which revision, what changed.
3. **Bus summary** - one table: bus, use, GPIOs.
4. **Full pin assignment** - one table, every wired GPIO exactly once: GPIO, signal, function.
   This table is the single home of pin numbers; on a conflict with any other doc, this wins.
5. **Per-block detail** - a small table per block (GPIO, signal, notes) with the electrical notes
   that matter to firmware: pull-ups, active levels, divider ratios, series resistors.
6. **What changed from the previous revision** - delta table: signal, before, after, why. Keeps
   every revision honest; on the first revision, state that there is no previous one.
7. **Strapping pins** - each strapping pin, what it is used for, and the required circuitry.
8. **Unavailable GPIOs** - pins the module cannot expose (flash, PSRAM, not bonded) and why.
9. **Open hardware questions** - numbered, answerable, aimed at the HW team.

## Diagram rules

- Diagrams are PlantUML: author `NN-name.puml` under `diagrams/<doc-stem>/`, render to SVG next to
  it, commit both together, embed the SVG with `![alt](diagrams/<doc-stem>/NN-name.svg)`.
- Dark theme: copy the skinparam header from an existing hardware diagram (or the AO kit's
  plotting standard if the project has it). Never a raw diagram fence in the `.md`.
- The system block diagram shows blocks and buses, not every net. Color edges by kind (power red,
  I2C blue, parallel data purple, GPIO grey, analog amber) and say so in the caption.
- ASCII hyphen only, in labels too.

## Review checklist (before locking either doc)

- Every wired GPIO appears in the full pin table exactly once; nothing in the schematic is missing.
- Strapping pins and unavailable pins are listed for the exact module variant (flash/PSRAM type).
- Every block on the schematic is either a numbered section or an open item - nothing dropped.
- The delta table matches the HW team's change log for this revision.
- Pin numbers quoted anywhere else (block diagram, code) agree with the full pin table.
- Diagrams re-rendered after any `.puml` edit; spell check passes.
