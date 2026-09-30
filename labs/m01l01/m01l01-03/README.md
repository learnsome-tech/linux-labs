# m01l01-03 · The kernel supplies the mechanism

**Lesson:** [What A Kernel Does, And What It Refuses To Do](https://learnsome.tech/learn/linux-course/m01l01) (lesson 1.1, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Explain how the kernel mediates hardware access without replacing user space

In the lesson: Now ask the shell to start a short child process. The child prints a fixed message and exits; the shell then returns to its prompt. The shell owns the wording of that message, while the kernel tracks the process and its exit status. This is the useful operational picture: when a program fails, ask whether the fault is in user space, at the system call boundary, or in the kernel and hardware underneath it.

## Files

- [`starter/shell-the-kernel-supplies-the-mechanism.py`](starter/shell-the-kernel-supplies-the-mechanism.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-03/starter`
2. Read `shell-the-kernel-supplies-the-mechanism.py`.
3. The session types these commands, in order:

   ```sh
   sh -c 'printf "child finished\n"'
   ```
4. Run it: `bash shell-the-kernel-supplies-the-mechanism.py`.
5. Check it from the repository root: `./check m01l01-03`.

## Expected output

```text
child finished
```

## How to check

`./check m01l01-03` copies `starter/` into a scratch directory and runs `bash shell-the-kernel-supplies-the-mechanism.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
