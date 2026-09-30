# m02l03-02 · Read symbolic and octal modes

**Lesson:** [Reading And Setting A File Mode](https://learnsome.tech/learn/linux-course/m02l03) (lesson 2.3, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Read a Unix file mode and choose owner, group, and other permissions deliberately

In the lesson: A mode can be read symbolically or as three octal digits. The record here describes a private script: the owner may read, write, and execute it, while the group and other classes have no bits. Octal is compact because read is four, write is two, and execute is one. Add the values inside each class to translate between the two forms.

## Files

- [`starter/shell-read-symbolic-and-octal-modes.py`](starter/shell-read-symbolic-and-octal-modes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-02/starter`
2. Read `shell-read-symbolic-and-octal-modes.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' mode=700 octal=700 u=rwx g=--- o=---
   ```
4. Run it: `bash shell-read-symbolic-and-octal-modes.py`.
5. Check it from the repository root: `./check m02l03-02`.

## Expected output

```text
mode=700
octal=700
u=rwx
g=---
o=---
```

## How to check

`./check m02l03-02` copies `starter/` into a scratch directory and runs `bash shell-read-symbolic-and-octal-modes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
