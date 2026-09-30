# m01l02-03 · Policy is part of the product

**Lesson:** [What A Distribution Actually Is](https://learnsome.tech/learn/linux-course/m01l02) (lesson 1.2, module 1: The Kernel, The Distribution, The Filesystem) · Free  
**Check:** Graded

## Goal

Describe how a Linux distribution assembles a kernel, user space, and release policy

In the lesson: A distribution also chooses defaults around the same kernel. Here the shell prints a small policy record that distinguishes a rolling channel from a fixed release. The record is intentionally plain text because the point is the decision, not a particular command. Before changing a production host, identify its release family, repository sources, and support window; a command copied from another family may have the wrong package names or assumptions.

## Files

- [`starter/shell-policy-is-part-of-the-product.py`](starter/shell-policy-is-part-of-the-product.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `shell-policy-is-part-of-the-product.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' policy=fixed updates=security
   ```
4. Run it: `bash shell-policy-is-part-of-the-product.py`.
5. Check it from the repository root: `./check m01l02-03`.

## Expected output

```text
policy=fixed
updates=security
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `bash shell-policy-is-part-of-the-product.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
