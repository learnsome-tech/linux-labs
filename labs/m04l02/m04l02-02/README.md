# m04l02-02 · Map a family to its tool

**Lesson:** [Three Families: apt, dnf And pacman](https://learnsome.tech/learn/linux-course/m04l02) (lesson 4.2, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Recognize the apt, dnf, and pacman package families and choose commands from the host distribution

In the lesson: The table maps a distribution family to its usual high-level tool. The values are a memory aid, not a substitute for checking the host. Once the family is known, read its configured repositories and simulate a transaction before changing installed software.

## Files

- [`starter/shell-map-a-family-to-its-tool.py`](starter/shell-map-a-family-to-its-tool.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `shell-map-a-family-to-its-tool.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' debian=apt fedora=dnf arch=pacman
   ```
4. Run it: `bash shell-map-a-family-to-its-tool.py`.
5. Check it from the repository root: `./check m04l02-02`.

## Expected output

```text
debian=apt
fedora=dnf
arch=pacman
```

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `bash shell-map-a-family-to-its-tool.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
