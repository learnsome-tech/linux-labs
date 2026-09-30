# m02l04-02 · Apply a umask

**Lesson:** [Directories, Umask And The Sticky Bit](https://learnsome.tech/learn/linux-course/m02l04) (lesson 2.4, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Predict default permissions for new objects and explain how the sticky bit protects shared directories

In the lesson: This record shows a regular file requested with mode six six six and a umask of zero two seven. The umask removes group write and all permissions for other users, leaving six four zero: owner read and write plus group read. The command is a compact calculation aid; on a real host, inspect the process umask and then verify the mode of an object you actually created.

## Files

- [`starter/shell-apply-a-umask.py`](starter/shell-apply-a-umask.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-02/starter`
2. Read `shell-apply-a-umask.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' request=666 umask=027 result=640
   ```
4. Run it: `bash shell-apply-a-umask.py`.
5. Check it from the repository root: `./check m02l04-02`.

## Expected output

```text
request=666
umask=027
result=640
```

## How to check

`./check m02l04-02` copies `starter/` into a scratch directory and runs `bash shell-apply-a-umask.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
