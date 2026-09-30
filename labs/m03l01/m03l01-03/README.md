# m03l01-03 · State and resources change

**Lesson:** [What A Process Is](https://learnsome.tech/learn/linux-course/m03l01) (lesson 3.1, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Describe a process as a running program with identity, state, resources, and a parent relationship

In the lesson: A process also has a current state and a set of resources. The example describes a worker that is sleeping while it waits for input and has two file descriptors open. State is a snapshot: the same process may be running, sleeping, stopped, or waiting moments later. When diagnosing a process, capture the observation and the time rather than treating one state as permanent.

## Files

- [`starter/shell-state-and-resources-change.py`](starter/shell-state-and-resources-change.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `shell-state-and-resources-change.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' pid=42 state=sleeping fds=2 memory=18M
   ```
4. Run it: `bash shell-state-and-resources-change.py`.
5. Check it from the repository root: `./check m03l01-03`.

## Expected output

```text
pid=42
state=sleeping
fds=2
memory=18M
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `bash shell-state-and-resources-change.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
