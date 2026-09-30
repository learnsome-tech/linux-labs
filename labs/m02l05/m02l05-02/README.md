# m02l05-02 · Describe a setuid boundary

**Lesson:** [Setuid, Setgid, And Root Through sudo](https://learnsome.tech/learn/linux-course/m02l05) (lesson 2.5, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Explain how setuid, setgid, and sudo change effective privilege and how to keep those changes narrow

In the lesson: The teaching record shows an ordinary user invoking a program owned by root with the setuid bit enabled. The process begins with one real UID but performs the protected operation using a different effective UID. The record is descriptive rather than a request to create a privileged binary. In practice, inspect ownership, mode, and the program's inputs before trusting such a boundary.

## Files

- [`starter/shell-describe-a-setuid-boundary.py`](starter/shell-describe-a-setuid-boundary.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `shell-describe-a-setuid-boundary.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' real=1 effective=0 bit=setuid op=limited
   ```
4. Run it: `bash shell-describe-a-setuid-boundary.py`.
5. Check it from the repository root: `./check m02l05-02`.

## Expected output

```text
real=1
effective=0
bit=setuid
op=limited
```

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `bash shell-describe-a-setuid-boundary.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
