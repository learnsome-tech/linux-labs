# m07l01-03 · Classify the response

**Lesson:** [HTTP Is Text: Requests, Status Codes And Headers](https://learnsome.tech/learn/linux-course/m07l01) (lesson 7.1, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Read the main parts of an HTTP request and response and interpret common status classes

In the lesson: The response record pairs a status with headers that explain the body and caching behavior. A two hundred response is success, while a four hundred or five hundred status requires a different owner to investigate. Read headers before assuming the body contains the complete reason for a failure.

## Files

- [`starter/shell-classify-the-response.py`](starter/shell-classify-the-response.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-03/starter`
2. Read `shell-classify-the-response.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' status=200 type=text cache=no id=abc
   ```
4. Run it: `bash shell-classify-the-response.py`.
5. Check it from the repository root: `./check m07l01-03`.

## Expected output

```text
status=200
type=text
cache=no
id=abc
```

## How to check

`./check m07l01-03` copies `starter/` into a scratch directory and runs `bash shell-classify-the-response.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
