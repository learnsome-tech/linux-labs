# m02l05-03 · sudo records an approved action

**Lesson:** [Setuid, Setgid, And Root Through sudo](https://learnsome.tech/learn/linux-course/m02l05) (lesson 2.5, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Explain how setuid, setgid, and sudo change effective privilege and how to keep those changes narrow

In the lesson: Sudo takes a different approach: an administrator policy names which users may run which commands as which target identity. A successful invocation is logged, and the command can remain explicit instead of granting a shell with unrestricted power. The example records a narrow restart permission. Prefer a specific, reviewable rule and ask for the smallest privilege the task needs.

## Files

- [`starter/shell-sudo-records-an-approved-action.py`](starter/shell-sudo-records-an-approved-action.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `shell-sudo-records-an-approved-action.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' user=ana cmd=restart target=root decision=ok
   ```
4. Run it: `bash shell-sudo-records-an-approved-action.py`.
5. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
user=ana
cmd=restart
target=root
decision=ok
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `bash shell-sudo-records-an-approved-action.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
