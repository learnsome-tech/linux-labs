# m05l04-03 · Separate DNS from HTTP

**Lesson:** [DNS Resolution, End To End](https://learnsome.tech/learn/linux-course/m05l04) (lesson 5.4, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Trace a DNS name from an application through a resolver to an authoritative answer

In the lesson: A DNS answer proves that a name mapped to an address at query time. It does not prove a route exists, a port is listening, or an HTTP request will succeed. The record keeps those checks separate so a successful lookup is evidence for naming only. Continue down the diagnostic ladder when the application still fails.

## Files

- [`starter/shell-separate-dns-from-http.py`](starter/shell-separate-dns-from-http.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `shell-separate-dns-from-http.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' dns=ok ip=192.0.2.10 route=? svc=?
   ```
4. Run it: `bash shell-separate-dns-from-http.py`.
5. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
dns=ok
ip=192.0.2.10
route=?
svc=?
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `bash shell-separate-dns-from-http.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
