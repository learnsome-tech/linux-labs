# m06l04-03 · Record the next test

**Lesson:** [Refused, Timed Out, Reset: Reading A Failure](https://learnsome.tech/learn/linux-course/m06l04) (lesson 6.4, module 6: Transport, Ports And Sockets) · Pro  
**Check:** Graded

## Goal

Differentiate refused, timed out, and reset connection failures by the evidence they provide

In the lesson: A good incident note pairs the observed result with the next narrow test. The record shows a timeout followed by a route check, rather than immediately changing application settings. Test from more than one vantage point when possible so a local firewall or asymmetric route does not look like a remote outage.

## Files

- [`starter/shell-record-the-next-test.py`](starter/shell-record-the-next-test.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-03/starter`
2. Read `shell-record-the-next-test.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' result=timeout next=route vantage=second-host
   ```
4. Run it: `bash shell-record-the-next-test.py`.
5. Check it from the repository root: `./check m06l04-03`.

## Expected output

```text
result=timeout
next=route
vantage=second-host
```

## How to check

`./check m06l04-03` copies `starter/` into a scratch directory and runs `bash shell-record-the-next-test.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
