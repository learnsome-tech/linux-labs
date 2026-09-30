# m07l02-02 · List the TLS promises

**Lesson:** [What HTTPS Adds, And What It Does Not](https://learnsome.tech/learn/linux-course/m07l02) (lesson 7.2, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Explain how HTTPS uses TLS to protect HTTP in transit and where that protection ends

In the lesson: The record separates confidentiality, integrity, and server authentication from claims HTTPS cannot make. Use these as questions during an incident: was the certificate trusted, was the session encrypted, and where does the session terminate? A proxy or load balancer may become the next endpoint.

## Files

- [`starter/shell-list-the-tls-promises.py`](starter/shell-list-the-tls-promises.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-02/starter`
2. Read `shell-list-the-tls-promises.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' enc=y int=y auth=y app=no
   ```
4. Run it: `bash shell-list-the-tls-promises.py`.
5. Check it from the repository root: `./check m07l02-02`.

## Expected output

```text
enc=y
int=y
auth=y
app=no
```

## How to check

`./check m07l02-02` copies `starter/` into a scratch directory and runs `bash shell-list-the-tls-promises.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
