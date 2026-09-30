# m08l05-02 · Check listener and answer

**Lesson:** [The Diagnostic Ladder: Is It Listening, Answering, Arriving](https://learnsome.tech/learn/linux-course/m08l05) (lesson 8.5, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

Complete a service diagnostic by checking listeners, application responses, and packet arrival

In the lesson: The record shows a listener, an application response, and packet arrival as separate observations. A listener without an answer points toward the process; an answer without remote arrival points toward the path or intermediary. Record the vantage point for every observation.

## Files

- [`starter/shell-check-listener-and-answer.py`](starter/shell-check-listener-and-answer.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l05/m08l05-02/starter`
2. Read `shell-check-listener-and-answer.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' listen=yes answer=ok arrive=yes source=client
   ```
4. Run it: `bash shell-check-listener-and-answer.py`.
5. Check it from the repository root: `./check m08l05-02`.

## Expected output

```text
listen=yes
answer=ok
arrive=yes
source=client
```

## How to check

`./check m08l05-02` copies `starter/` into a scratch directory and runs `bash shell-check-listener-and-answer.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
