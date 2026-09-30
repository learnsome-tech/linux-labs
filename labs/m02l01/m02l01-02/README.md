# m02l01-02 · Read an account record

**Lesson:** [Users, UIDs And The Password File](https://learnsome.tech/learn/linux-course/m02l01) (lesson 2.1, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Explain how Linux identifies users with UIDs and how account metadata is separated from password hashes

In the lesson: An account record can be represented as fields in a fixed order: name, UID, primary group, home, and shell. The teaching command prints those fields without exposing any real host account. On Linux, local records traditionally come from passwd data, while password hashes are kept separately and protected. Learn the field order before editing identity configuration by hand.

## Files

- [`starter/shell-read-an-account-record.py`](starter/shell-read-an-account-record.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `shell-read-an-account-record.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' name=ana uid=1001 group=staff home=/home/a
   ```
4. Run it: `bash shell-read-an-account-record.py`.
5. Check it from the repository root: `./check m02l01-02`.

## Expected output

```text
name=ana
uid=1001
group=staff
home=/home/a
```

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `bash shell-read-an-account-record.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
