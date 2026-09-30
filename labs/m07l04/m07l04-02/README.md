# m07l04-02 · Check a host key

**Lesson:** [SSH: The Protocol, And The Host Key You Accept](https://learnsome.tech/learn/linux-course/m07l04) (lesson 7.4, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Explain SSH host key verification and distinguish server identity from user authentication

In the lesson: The record shows a server name, a key fingerprint, and the local trust decision. Compare a first-seen fingerprint with an independent source before accepting it. A changed key may be a legitimate rebuild, but it can also indicate a man in the middle or a connection to the wrong host.

## Files

- [`starter/shell-check-a-host-key.py`](starter/shell-check-a-host-key.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-02/starter`
2. Read `shell-check-a-host-key.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' host=server key=abc known=no ask=verify
   ```
4. Run it: `bash shell-check-a-host-key.py`.
5. Check it from the repository root: `./check m07l04-02`.

## Expected output

```text
host=server
key=abc
known=no
ask=verify
```

## How to check

`./check m07l04-02` copies `starter/` into a scratch directory and runs `bash shell-check-a-host-key.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
