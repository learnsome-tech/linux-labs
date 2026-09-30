# m03l05-03 · Separate state from enablement

**Lesson:** [systemd: Units, Targets And The Boot Graph](https://learnsome.tech/learn/linux-course/m03l05) (lesson 3.5, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Read systemd units and targets as a dependency graph rather than a flat startup script

In the lesson: A service can be enabled for a future boot without currently running, or running without being enabled for the next boot. The record keeps those states separate. This distinction prevents a common operational mistake: using one command to answer whether a service is active now and another question about whether it will start later.

## Files

- [`starter/shell-separate-state-from-enablement.py`](starter/shell-separate-state-from-enablement.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `shell-separate-state-from-enablement.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' unit=web active=no enabled=yes preset=def
   ```
4. Run it: `bash shell-separate-state-from-enablement.py`.
5. Check it from the repository root: `./check m03l05-03`.

## Expected output

```text
unit=web
active=no
enabled=yes
preset=def
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `bash shell-separate-state-from-enablement.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
