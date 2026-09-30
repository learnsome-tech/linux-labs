# m03l03-03 · Detach intentionally

**Lesson:** [Job Control, And Processes That Outlive You](https://learnsome.tech/learn/linux-course/m03l03) (lesson 3.3, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Explain foreground and background jobs and how a process can outlive the shell that started it

In the lesson: A process that must survive logout needs an intentional detachment plan. The record names a process whose standard output is redirected and whose parent session is no longer the interactive shell. Tools such as nohup, a service manager, or a terminal multiplexer implement different versions of that idea. Do not assume that backgrounding alone makes a workload durable.

## Files

- [`starter/shell-detach-intentionally.py`](starter/shell-detach-intentionally.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `shell-detach-intentionally.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' pid=42 parent=1 stdout=log detached=yes
   ```
4. Run it: `bash shell-detach-intentionally.py`.
5. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
pid=42
parent=1
stdout=log
detached=yes
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `bash shell-detach-intentionally.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
