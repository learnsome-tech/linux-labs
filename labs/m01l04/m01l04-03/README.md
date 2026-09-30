# m01l04-03 · rm removes a directory entry

**Lesson:** [Inodes, Hard Links And What rm Removes](https://learnsome.tech/learn/linux-course/m01l04) (lesson 1.4, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Explain how directory names point to inodes and why removing a name does not erase every reference

In the lesson: The name rm is easy to misread. In the ordinary case it removes one directory entry and decrements the inode's link count. With two hard-link names, removing report leaves archive pointing to the same data. Only after the final name disappears, and after open readers close the file, can the filesystem reclaim the blocks. The operation is about unlinking a name, not about shredding bytes immediately.

## Files

- [`starter/shell-rm-removes-a-directory-entry.py`](starter/shell-rm-removes-a-directory-entry.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-03/starter`
2. Read `shell-rm-removes-a-directory-entry.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' 'rm->archive' links=1 data=reachable
   ```
4. Run it: `bash shell-rm-removes-a-directory-entry.py`.
5. Check it from the repository root: `./check m01l04-03`.

## Expected output

```text
rm->archive
links=1
data=reachable
```

## How to check

`./check m01l04-03` copies `starter/` into a scratch directory and runs `bash shell-rm-removes-a-directory-entry.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
