# m03l03-02 · Represent a background job

**Lesson:** [Job Control, And Processes That Outlive You](https://learnsome.tech/learn/linux-course/m03l03) (lesson 3.3, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Explain foreground and background jobs and how a process can outlive the shell that started it

In the lesson: The record shows a command placed in the background with a shell job number and a process identifier. The ampersand is a request to the shell, not a special property of the program itself. Use the job number for shell control while the process identifier is the handle other tools use to inspect or signal the process.

## Files

- [`starter/shell-represent-a-background-job.py`](starter/shell-represent-a-background-job.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-02/starter`
2. Read `shell-represent-a-background-job.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' job=1 pid=42 state=running terminal=shared
   ```
4. Run it: `bash shell-represent-a-background-job.py`.
5. Check it from the repository root: `./check m03l03-02`.

## Expected output

```text
job=1
pid=42
state=running
terminal=shared
```

## How to check

`./check m03l03-02` copies `starter/` into a scratch directory and runs `bash shell-represent-a-background-job.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
