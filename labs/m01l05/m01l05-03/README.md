# m01l05-03 · Device names are interfaces

**Lesson:** [Everything Is A File: proc, sys And dev](https://learnsome.tech/learn/linux-course/m01l05) (lesson 1.5, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Distinguish ordinary files from the kernel-backed interfaces exposed through proc, sys, and dev

In the lesson: Device nodes provide names that programs can open, but opening one does not make it an ordinary data file. A terminal, a disk, and a random-number source can each have different kernel behavior behind the same open and read calls. This record highlights that distinction. Before redirecting output into a path under dev, confirm what the device represents and which permissions protect it.

## Files

- [`starter/shell-device-names-are-interfaces.py`](starter/shell-device-names-are-interfaces.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-03/starter`
2. Read `shell-device-names-are-interfaces.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' source=dev node=tty behavior=kernel
   ```
4. Run it: `bash shell-device-names-are-interfaces.py`.
5. Check it from the repository root: `./check m01l05-03`.

## Expected output

```text
source=dev
node=tty
behavior=kernel
```

## How to check

`./check m01l05-03` copies `starter/` into a scratch directory and runs `bash shell-device-names-are-interfaces.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
