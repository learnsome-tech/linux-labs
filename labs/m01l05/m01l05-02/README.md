# m01l05-02 · Read a live view

**Lesson:** [Everything Is A File: proc, sys And dev](https://learnsome.tech/learn/linux-course/m01l05) (lesson 1.5, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Distinguish ordinary files from the kernel-backed interfaces exposed through proc, sys, and dev

In the lesson: A live interface can be represented as a small record with a source and a changing value. The teaching command prints a process view and a device view side by side. On a real Linux host you would inspect files below proc or sys with commands such as cat, but their exact contents depend on the current machine. The stable lesson is the ownership: the kernel generates the view and user space reads it.

## Files

- [`starter/shell-read-a-live-view.py`](starter/shell-read-a-live-view.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-02/starter`
2. Read `shell-read-a-live-view.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' source=proc view=process owner=kernel
   ```
4. Run it: `bash shell-read-a-live-view.py`.
5. Check it from the repository root: `./check m01l05-02`.

## Expected output

```text
source=proc
view=process
owner=kernel
```

## How to check

`./check m01l05-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-live-view.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
