# m04l04-02 · Read filesystem capacity

**Lesson:** [Running Out Of Space: df, du And Inodes](https://learnsome.tech/learn/linux-course/m04l04) (lesson 4.4, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Distinguish block exhaustion from inode exhaustion and use df and du evidence in the right order

In the lesson: A capacity summary should show the filesystem, block usage, and inode usage. The record has room in both resources, but the values are independent. On a real host, df reports filesystem totals; use its block and inode views before deciding which directory deserves closer inspection.

## Files

- [`starter/shell-read-filesystem-capacity.py`](starter/shell-read-filesystem-capacity.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `shell-read-filesystem-capacity.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' mount=/ usage=82% inodes=41% state=healthy
   ```
4. Run it: `bash shell-read-filesystem-capacity.py`.
5. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
mount=/
usage=82%
inodes=41%
state=healthy
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `bash shell-read-filesystem-capacity.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
