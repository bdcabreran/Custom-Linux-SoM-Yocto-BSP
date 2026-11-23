# Pointer README template

The exact shape of a `docs/08-references/<folder>/README.md`. The `/references` skill reads this file
when it checks a folder and when it writes a new one, so this is the contract - change it here and
both follow.

Why it is strict: the pointer is the only thing git carries. If one folder records its revision in a
different row name, the next engineer misses it and the folder quietly stops being reproducible.

Before writing one, check the material belongs here at all: this folder is for what stays put.
Requirements and anything that moves with the project live in `docs/01-requirements/`. See "Adding
something" in the references root README.

## Required

In this order. Extra sections are welcome anywhere after `## Source`.

1. `# <Title>` - what the material is, in a few words.
2. An opening paragraph: one or two sentences on what it is and what we use it for.
3. The pointer line, near the top: says the payload is git-ignored and this README is the tracked
   pointer.
4. `## Source` - a two-column table with these four rows, in this order, none empty:

   | Field | Value |
   |---|---|
   | What it is | one line, plain |
   | Lives in | the URL, the G-Drive folder, or the vendor page |
   | Version | pinned commit, schematic revision, datasheet date, or `live clone` |
   | Owner | the team or person who publishes it |

   More rows may follow the four.

5. `## Fetch` - how the next person gets the identical copy. Either a `sh` code block with the
   commands, or numbered steps when it cannot be scripted (a G-Drive download, a login). When it
   cannot be scripted, the steps must name the destination path and the file-name pattern.
6. `## What depends on it` - a list of the docs and code a new version would touch. One bullet each,
   opening with the repo-relative path in backticks, then a dash and why. The skill tests that first
   path and reads the list back when a revision lands, so keep the path first and keep it real.

## Optional

- `## Files` - a table of the files in the folder and what each is. Add it once there is more than
  one file, or when several revisions sit side by side.
- `## Open` - anything genuinely missing, such as a link nobody has recorded yet. One short list.

## Skeleton

````markdown
# <Title>

<What this material is and what we use it for. One or two sentences.>

<The clone / the exports / the decks> under `<path>/` is git-ignored. This README is the tracked
pointer.

## Source

| Field | Value |
|---|---|
| What it is | <one line> |
| Lives in | <URL, G-Drive folder, or vendor page> |
| Version | <pinned commit, revision, date, or `live clone`> |
| Owner | <team or person> |

## Fetch

```sh
<commands that produce the identical copy>
```

## What depends on it

- `<path>` - <why it depends on this>
````

## What the skill checks

Mechanical, run as commands rather than judged: the four Source rows are present and non-empty, the
three required sections exist with these exact names, the pointer line is there, every path under
"What depends on it" exists, the folder has a row in the routing table and in the tracked table, and
`git check-ignore` confirms the README is tracked while the payload is not.
