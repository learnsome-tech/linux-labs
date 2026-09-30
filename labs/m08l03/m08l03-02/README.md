# m08l03-02 · Read backend selection

**Lesson:** [Load Balancing: Algorithms, Health Checks And Layers](https://learnsome.tech/learn/linux-course/m08l03) (lesson 8.3, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

Explain how a load balancer selects backends and why health checks must test the right layer

In the lesson: The record shows a request selected by round robin from two healthy backends. A real balancer also tracks failures and connection counts. When traffic is uneven, inspect the algorithm and whether session affinity or long-lived connections are changing the expected distribution.

## Files

- [`starter/shell-read-backend-selection.py`](starter/shell-read-backend-selection.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-02/starter`
2. Read `shell-read-backend-selection.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' algo=rr req=42 be=app-a ok=y
   ```
4. Run it: `bash shell-read-backend-selection.py`.
5. Check it from the repository root: `./check m08l03-02`.

## Expected output

```text
algo=rr
req=42
be=app-a
ok=y
```

## How to check

`./check m08l03-02` copies `starter/` into a scratch directory and runs `bash shell-read-backend-selection.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
