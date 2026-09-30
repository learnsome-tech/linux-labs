# m02l02-03 · Membership changes at login

**Lesson:** [Groups, And How Shared Access Is Granted](https://learnsome.tech/learn/linux-course/m02l02) (lesson 2.2, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Use supplementary groups to reason about shared ownership and access without making files world writable

In the lesson: A group database change and a running shell are separate moments. The teaching record shows a user added to writers, followed by a new session that carries the membership. If an operator adds a user but an existing shell still cannot access the directory, checking the session's supplementary groups is often the missing step. Do not infer effective access from the account database alone.

## Files

- [`starter/shell-membership-changes-at-login.py`](starter/shell-membership-changes-at-login.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `shell-membership-changes-at-login.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' account=carol added=writers session=renewed
   ```
4. Run it: `bash shell-membership-changes-at-login.py`.
5. Check it from the repository root: `./check m02l02-03`.

## Expected output

```text
account=carol
added=writers
session=renewed
```

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `bash shell-membership-changes-at-login.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
