# m05l05-02 · Read typed records

**Lesson:** [Record Types, Caching And Time To Live](https://learnsome.tech/learn/linux-course/m05l05) (lesson 5.5, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Interpret common DNS records and explain how TTL controls cached answer freshness

In the lesson: The record places several common answers beside their types. The type tells the resolver and operator how to interpret the value. When debugging a name, query the record type you expect instead of assuming every answer is an address.

## Files

- [`starter/shell-read-typed-records.py`](starter/shell-read-typed-records.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-02/starter`
2. Read `shell-read-typed-records.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' A=192.0.2.10 AAAA=2001:db8::10 CNAME=www MX=mail
   ```
4. Run it: `bash shell-read-typed-records.py`.
5. Check it from the repository root: `./check m05l05-02`.

## Expected output

```text
A=192.0.2.10
AAAA=2001:db8::10
CNAME=www
MX=mail
```

## How to check

`./check m05l05-02` copies `starter/` into a scratch directory and runs `bash shell-read-typed-records.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
