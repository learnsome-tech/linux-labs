# m04l03-03 · Mount is an attachment

**Lesson:** [Disks, Filesystems And Mounting](https://learnsome.tech/learn/linux-course/m04l03) (lesson 4.3, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Distinguish block devices, filesystems, and mount points when inspecting storage

In the lesson: Mounting attaches an existing filesystem at a directory. The directory must exist, and anything previously visible beneath that path is hidden until the filesystem is unmounted. The record shows a deliberate mount with a read-only option, which is useful during investigation. Treat mount options as part of the security and reliability policy, not as decoration.

## Files

- [`starter/shell-mount-is-an-attachment.py`](starter/shell-mount-is-an-attachment.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-03/starter`
2. Read `shell-mount-is-an-attachment.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' source=disk1 target=/mnt/x mode=ro mounted=yes
   ```
4. Run it: `bash shell-mount-is-an-attachment.py`.
5. Check it from the repository root: `./check m04l03-03`.

## Expected output

```text
source=disk1
target=/mnt/x
mode=ro
mounted=yes
```

## How to check

`./check m04l03-03` copies `starter/` into a scratch directory and runs `bash shell-mount-is-an-attachment.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
