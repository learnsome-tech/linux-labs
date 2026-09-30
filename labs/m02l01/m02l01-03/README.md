# m02l01-03 · Names are not secrets

**Lesson:** [Users, UIDs And The Password File](https://learnsome.tech/learn/linux-course/m02l01) (lesson 2.1, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Explain how Linux identifies users with UIDs and how account metadata is separated from password hashes

In the lesson: The account name and UID identify an account; they do not authenticate it. Authentication data belongs in a protected credential store, commonly represented by a shadow record with a hash and account aging policy. The example keeps the value descriptive rather than real. Treat identity metadata and authentication secrets as separate kinds of data, with different permissions and audit requirements.

## Files

- [`starter/shell-names-are-not-secrets.py`](starter/shell-names-are-not-secrets.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `shell-names-are-not-secrets.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' account=analyst credential=protected hash=stored
   ```
4. Run it: `bash shell-names-are-not-secrets.py`.
5. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
account=analyst
credential=protected
hash=stored
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `bash shell-names-are-not-secrets.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
