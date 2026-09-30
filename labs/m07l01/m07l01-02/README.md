# m07l01-02 · Read a request

**Lesson:** [HTTP Is Text: Requests, Status Codes And Headers](https://learnsome.tech/learn/linux-course/m07l01) (lesson 7.1, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Read the main parts of an HTTP request and response and interpret common status classes

In the lesson: The record lists the method, target, and two request headers. A GET asks for a representation, while the host and accept headers tell the server which name and format the client expects. In a packet capture, these lines help separate an HTTP problem from a lower transport failure.

## Files

- [`starter/shell-read-a-request.py`](starter/shell-read-a-request.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-02/starter`
2. Read `shell-read-a-request.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' m=GET t=/health host=example accept=text
   ```
4. Run it: `bash shell-read-a-request.py`.
5. Check it from the repository root: `./check m07l01-02`.

## Expected output

```text
m=GET
t=/health
host=example
accept=text
```

## How to check

`./check m07l01-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-request.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
