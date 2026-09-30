# m07l03-03 · Separate proof from trust

**Lesson:** [Certificates, Chains And What A Handshake Proves](https://learnsome.tech/learn/linux-course/m07l03) (lesson 7.3, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Read certificate identity and chain validation as evidence of a TLS server handshake

In the lesson: A valid chain proves possession of a private key for the validated name, not the honesty of every response. The record separates cryptographic proof from application trust and authorization. Keep certificate validation, user authentication, and application authorization as three distinct checks.

## Files

- [`starter/shell-separate-proof-from-trust.py`](starter/shell-separate-proof-from-trust.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-03/starter`
2. Read `shell-separate-proof-from-trust.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' tls=ok id=checked user=? auth=separate
   ```
4. Run it: `bash shell-separate-proof-from-trust.py`.
5. Check it from the repository root: `./check m07l03-03`.

## Expected output

```text
tls=ok
id=checked
user=?
auth=separate
```

## How to check

`./check m07l03-03` copies `starter/` into a scratch directory and runs `bash shell-separate-proof-from-trust.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
