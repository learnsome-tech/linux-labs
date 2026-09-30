# m03l02-03 · Escalate deliberately

**Lesson:** [Signals, And What kill Really Sends](https://learnsome.tech/learn/linux-course/m03l02) (lesson 3.2, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Choose an appropriate Unix signal and understand what kill sends to a process

In the lesson: A forced stop is different from a graceful request. The kernel delivers KILL and does not offer the process a handler or cleanup phase. That can leave temporary files, locks, or partial writes behind. The example records an escalation only after a timeout, and it names the operational cost so the action is a considered last resort rather than a reflex.

## Files

- [`starter/shell-escalate-deliberately.py`](starter/shell-escalate-deliberately.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `shell-escalate-deliberately.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' target=42 sig=KILL why=timeout cleanup=none
   ```
4. Run it: `bash shell-escalate-deliberately.py`.
5. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
target=42
sig=KILL
why=timeout
cleanup=none
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `bash shell-escalate-deliberately.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
