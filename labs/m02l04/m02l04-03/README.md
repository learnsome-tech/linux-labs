# m02l04-03 · Protect a shared directory

**Lesson:** [Directories, Umask And The Sticky Bit](https://learnsome.tech/learn/linux-course/m02l04) (lesson 2.4, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Predict default permissions for new objects and explain how the sticky bit protects shared directories

In the lesson: A shared directory often lets everyone create files, but users should not be able to remove one another's entries. The sticky bit adds that ownership check to deletion and rename operations. The example labels a temporary directory with a sticky bit and a group that may work there. It does not replace ordinary read, write, and search permissions; it adds a rule for who may remove a name.

## Files

- [`starter/shell-protect-a-shared-directory.py`](starter/shell-protect-a-shared-directory.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `shell-protect-a-shared-directory.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' dir=/tmp/x mode=1770 sticky=on group=team
   ```
4. Run it: `bash shell-protect-a-shared-directory.py`.
5. Check it from the repository root: `./check m02l04-03`.

## Expected output

```text
dir=/tmp/x
mode=1770
sticky=on
group=team
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `bash shell-protect-a-shared-directory.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
