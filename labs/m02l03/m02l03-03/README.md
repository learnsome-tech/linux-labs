# m02l03-03 · Change only the intended class

**Lesson:** [Reading And Setting A File Mode](https://learnsome.tech/learn/linux-course/m02l03) (lesson 2.3, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Read a Unix file mode and choose owner, group, and other permissions deliberately

In the lesson: Changing a mode is a policy decision. This example starts with a shared report and adds group write permission while leaving other users unable to write. A symbolic change names the class and operation, which is often safer in a runbook than replacing every bit with a guessed number. After changing it, inspect the resulting mode and confirm the owning group is the one you intended.

## Files

- [`starter/shell-change-only-the-intended-class.py`](starter/shell-change-only-the-intended-class.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-03/starter`
2. Read `shell-change-only-the-intended-class.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' before=640 change=g+w after=660 group=writers
   ```
4. Run it: `bash shell-change-only-the-intended-class.py`.
5. Check it from the repository root: `./check m02l03-03`.

## Expected output

```text
before=640
change=g+w
after=660
group=writers
```

## How to check

`./check m02l03-03` copies `starter/` into a scratch directory and runs `bash shell-change-only-the-intended-class.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
