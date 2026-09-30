# m05l01-03 · Stop at the first failed layer

**Lesson:** [The Layer Model, As Far As It Earns Its Place](https://learnsome.tech/learn/linux-course/m05l01) (lesson 5.1, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Use a small network layer model to locate where a connection problem begins

In the lesson: A diagnostic record should name the first failed dependency. Here the link is up but the route is missing, so there is no reason to investigate HTTP yet. Capture that boundary, fix or escalate it, and then repeat the higher layer test. This keeps troubleshooting evidence ordered instead of mixing symptoms from several failures.

## Files

- [`starter/shell-stop-at-the-first-failed-layer.py`](starter/shell-stop-at-the-first-failed-layer.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `shell-stop-at-the-first-failed-layer.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' link=up route=missing next=route
   ```
4. Run it: `bash shell-stop-at-the-first-failed-layer.py`.
5. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
link=up
route=missing
next=route
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `bash shell-stop-at-the-first-failed-layer.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
