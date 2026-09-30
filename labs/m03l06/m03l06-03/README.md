# m03l06-03 · Query the journal

**Lesson:** [Your Own Unit, And Reading journald](https://learnsome.tech/learn/linux-course/m03l06) (lesson 3.6, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Design a small systemd service and read its journal by unit and time

In the lesson: Journald records structured events that can be filtered by unit, boot, priority, and time. The example represents a unit query and its useful fields: timestamp, priority, and message. Start with a narrow time window and the unit name, then widen the search only when the first evidence does not explain the failure.

## Files

- [`starter/shell-query-the-journal.py`](starter/shell-query-the-journal.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l06/m03l06-03/starter`
2. Read `shell-query-the-journal.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' unit=worker since=boot pri=err msg=timeout
   ```
4. Run it: `bash shell-query-the-journal.py`.
5. Check it from the repository root: `./check m03l06-03`.

## Expected output

```text
unit=worker
since=boot
pri=err
msg=timeout
```

## How to check

`./check m03l06-03` copies `starter/` into a scratch directory and runs `bash shell-query-the-journal.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
