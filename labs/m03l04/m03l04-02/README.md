# m03l04-02 · Read a boot selection

**Lesson:** [Booting: GRUB, The Kernel Command Line And initramfs](https://learnsome.tech/learn/linux-course/m03l04) (lesson 3.4, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Trace the main Linux boot stages from firmware through the kernel and initramfs

In the lesson: The record represents the inputs selected by a bootloader: a kernel image, an initramfs image, and a root device. The values are descriptive so the example runs on any host. When a machine fails before user space, compare these inputs with the disks and drivers the kernel can actually see.

## Files

- [`starter/shell-read-a-boot-selection.py`](starter/shell-read-a-boot-selection.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `shell-read-a-boot-selection.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' kernel=vmlinuz initrd=initramfs root=/dev/root
   ```
4. Run it: `bash shell-read-a-boot-selection.py`.
5. Check it from the repository root: `./check m03l04-02`.

## Expected output

```text
kernel=vmlinuz
initrd=initramfs
root=/dev/root
```

## How to check

`./check m03l04-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-boot-selection.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
