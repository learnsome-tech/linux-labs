# m01l01-02 · A shell is user space

**Lesson:** [What A Kernel Does, And What It Refuses To Do](https://learnsome.tech/learn/linux-course/m01l01) (lesson 1.1, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Explain how the kernel mediates hardware access without replacing user space

In the lesson: We can make the boundary visible without needing a special diagnostic tool. First, the shell evaluates a command and the printf program writes text to standard output. The kernel supplies the process, file descriptor, and terminal behind that action, but it does not know that the text is a greeting. Notice the division of responsibility: the command has meaning in user space, while the kernel provides the mechanism that lets it run.

## Files

- [`starter/shell-a-shell-is-user-space.py`](starter/shell-a-shell-is-user-space.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-02/starter`
2. Read `shell-a-shell-is-user-space.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' 'user space chose this text'
   ```
4. Run it: `bash shell-a-shell-is-user-space.py`.
5. Check it from the repository root: `./check m01l01-02`.

## Expected output

```text
user space chose this text
```

## How to check

`./check m01l01-02` copies `starter/` into a scratch directory and runs `bash shell-a-shell-is-user-space.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
