# m03l01-02 · Describe process identity

**Lesson:** [What A Process Is](https://learnsome.tech/learn/linux-course/m03l01) (lesson 3.1, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Describe a process as a running program with identity, state, resources, and a parent relationship

In the lesson: The record shows the fields an operator wants when identifying a process: its PID, parent PID, user, and command. A real Linux inspection command can expose these fields for every process, but the portable example keeps values fixed for the lesson. Start with identity before deciding whether a process is the one you meant to inspect or stop.

## Files

- [`starter/shell-describe-process-identity.py`](starter/shell-describe-process-identity.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `shell-describe-process-identity.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' pid=42 ppid=1 user=ana cmd=worker
   ```
4. Run it: `bash shell-describe-process-identity.py`.
5. Check it from the repository root: `./check m03l01-02`.

## Expected output

```text
pid=42
ppid=1
user=ana
cmd=worker
```

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `bash shell-describe-process-identity.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
