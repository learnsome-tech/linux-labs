# m01l03-03 · Separate special views

**Lesson:** [The Filesystem Hierarchy](https://learnsome.tech/learn/linux-course/m01l03) (lesson 1.3, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Navigate the Linux filesystem hierarchy by purpose rather than by memorized paths

In the lesson: Some paths look like directories but represent live interfaces rather than ordinary stored files. Proc describes processes and kernel data, sys exposes device and kernel attributes, and dev provides device nodes used by programs. The table separates those views from persistent configuration. When a troubleshooting guide asks you to inspect one, remember that its contents describe the current machine and can change while you read them.

## Files

- [`starter/shell-separate-special-views.py`](starter/shell-separate-special-views.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-03/starter`
2. Read `shell-separate-special-views.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' /proc=kernel /sys=device /dev=nodes
   ```
4. Run it: `bash shell-separate-special-views.py`.
5. Check it from the repository root: `./check m01l03-03`.

## Expected output

```text
/proc=kernel
/sys=device
/dev=nodes
```

## How to check

`./check m01l03-03` copies `starter/` into a scratch directory and runs `bash shell-separate-special-views.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
