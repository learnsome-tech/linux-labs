# m05l05-03 · Account for cached time

**Lesson:** [Record Types, Caching And Time To Live](https://learnsome.tech/learn/linux-course/m05l05) (lesson 5.5, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Interpret common DNS records and explain how TTL controls cached answer freshness

In the lesson: A cached answer is accompanied by a remaining lifetime. The record shows a published TTL and the smaller value left in a resolver cache. During a migration, clients can continue using the old address until that remaining time expires, so change plans must account for caches outside your control.

## Files

- [`starter/shell-account-for-cached-time.py`](starter/shell-account-for-cached-time.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-03/starter`
2. Read `shell-account-for-cached-time.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' name=www ttl=300 remaining=120 source=cache
   ```
4. Run it: `bash shell-account-for-cached-time.py`.
5. Check it from the repository root: `./check m05l05-03`.

## Expected output

```text
name=www
ttl=300
remaining=120
source=cache
```

## How to check

`./check m05l05-03` copies `starter/` into a scratch directory and runs `bash shell-account-for-cached-time.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
