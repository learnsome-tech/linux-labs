# m03l04-03 · The command line changes behavior

**Lesson:** [Booting: GRUB, The Kernel Command Line And initramfs](https://learnsome.tech/learn/linux-course/m03l04) (lesson 3.4, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Trace the main Linux boot stages from firmware through the kernel and initramfs

In the lesson: The kernel command line is a compact configuration channel for early boot. Parameters can select a root device, change logging, or request a recovery target. The record shows a quiet boot with an explicit root and console. When diagnosing a boot problem, capture the complete command line; one parameter can explain why a healthy kernel chooses the wrong root or hides useful messages.

## Files

- [`starter/shell-the-command-line-changes-behavior.py`](starter/shell-the-command-line-changes-behavior.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-03/starter`
2. Read `shell-the-command-line-changes-behavior.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' root=/dev/root loglevel=4 console=tty quiet=yes
   ```
4. Run it: `bash shell-the-command-line-changes-behavior.py`.
5. Check it from the repository root: `./check m03l04-03`.

## Expected output

```text
root=/dev/root
loglevel=4
console=tty
quiet=yes
```

## How to check

`./check m03l04-03` copies `starter/` into a scratch directory and runs `bash shell-the-command-line-changes-behavior.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
