# m01l04-02 · A hard link is another name

**Lesson:** [Inodes, Hard Links And What rm Removes](https://learnsome.tech/learn/linux-course/m01l04) (lesson 1.4, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Explain how directory names point to inodes and why removing a name does not erase every reference

In the lesson: Imagine one inode with two directory entries. The teaching record names the inode and shows its link count rising from one to two. Editing through either name changes the same underlying file because there is still only one inode. This is different from copying: a copy creates a second inode with independent data. The command prints the relationship so we can focus on the model without depending on filesystem-specific inode numbers.

## Files

- [`starter/shell-a-hard-link-is-another-name.py`](starter/shell-a-hard-link-is-another-name.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `shell-a-hard-link-is-another-name.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' 'inode=42' 'names=report,archive' 'links=2'
   ```
4. Run it: `bash shell-a-hard-link-is-another-name.py`.
5. Check it from the repository root: `./check m01l04-02`.

## Expected output

```text
inode=42
names=report,archive
links=2
```

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `bash shell-a-hard-link-is-another-name.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
