# m01l02-02 · Read the release identity

**Lesson:** [What A Distribution Actually Is](https://learnsome.tech/learn/linux-course/m01l02) (lesson 1.2, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Describe how a Linux distribution assembles a kernel, user space, and release policy

In the lesson: The distribution identity is data exposed to user space. On a Linux machine, an operator commonly reads an os release file, while other Unix systems expose different metadata. For a portable demonstration, we will print the fields a release description needs: a name, a version, and a support channel. The important habit is to read the machine's declared identity before choosing package commands or troubleshooting instructions.

## Files

- [`starter/shell-read-the-release-identity.py`](starter/shell-read-the-release-identity.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-02/starter`
2. Read `shell-read-the-release-identity.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' NAME=Example VERSION=1 CHANNEL=stable
   ```
4. Run it: `bash shell-read-the-release-identity.py`.
5. Check it from the repository root: `./check m01l02-02`.

## Expected output

```text
NAME=Example
VERSION=1
CHANNEL=stable
```

## How to check

`./check m01l02-02` copies `starter/` into a scratch directory and runs `bash shell-read-the-release-identity.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
