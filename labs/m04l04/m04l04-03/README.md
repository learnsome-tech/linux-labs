# m04l04-03 · Find the directory pressure

**Lesson:** [Running Out Of Space: df, du And Inodes](https://learnsome.tech/learn/linux-course/m04l04) (lesson 4.4, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Distinguish block exhaustion from inode exhaustion and use df and du evidence in the right order

In the lesson: Once block pressure is confirmed, du helps rank directories by their visible data. The example records a large log tree and a smaller cache tree. Remember that du may not explain all used space when a process still holds a deleted file open; compare filesystem totals with directory totals and then inspect open handles if the numbers do not agree.

## Files

- [`starter/shell-find-the-directory-pressure.py`](starter/shell-find-the-directory-pressure.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `shell-find-the-directory-pressure.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' log=8G cache=2G next=handles
   ```
4. Run it: `bash shell-find-the-directory-pressure.py`.
5. Check it from the repository root: `./check m04l04-03`.

## Expected output

```text
log=8G
cache=2G
next=handles
```

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `bash shell-find-the-directory-pressure.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
