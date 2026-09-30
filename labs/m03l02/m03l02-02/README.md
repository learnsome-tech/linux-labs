# m03l02-02 · Name the signal

**Lesson:** [Signals, And What kill Really Sends](https://learnsome.tech/learn/linux-course/m03l02) (lesson 3.2, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Choose an appropriate Unix signal and understand what kill sends to a process

In the lesson: The record separates a target PID from the signal being sent. Term asks a process to finish cleanly, while kill is reserved for a process that cannot handle a normal termination request. The command prints the decision without sending a real signal, so the example is safe to replay while you learn the vocabulary.

## Files

- [`starter/shell-name-the-signal.py`](starter/shell-name-the-signal.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `shell-name-the-signal.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' target=42 signal=TERM action=graceful
   ```
4. Run it: `bash shell-name-the-signal.py`.
5. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
target=42
signal=TERM
action=graceful
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `bash shell-name-the-signal.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
