# m04l01-03 · Ownership answers why

**Lesson:** [What A Package Manager Guarantees](https://learnsome.tech/learn/linux-course/m04l01) (lesson 4.1, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Explain how a package manager tracks files, dependencies, versions, and trusted sources

In the lesson: When a package owns a file, the package database can connect an unexpected path to the transaction that installed it. The example records a file, its owner, and the action that placed it. This is useful evidence when deciding whether to edit a file, reinstall a package, or look for a local override instead of changing vendor content directly.

## Files

- [`starter/shell-ownership-answers-why.py`](starter/shell-ownership-answers-why.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-03/starter`
2. Read `shell-ownership-answers-why.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' file=/etc/web.conf owner=web action=installed
   ```
4. Run it: `bash shell-ownership-answers-why.py`.
5. Check it from the repository root: `./check m04l01-03`.

## Expected output

```text
file=/etc/web.conf
owner=web
action=installed
```

## How to check

`./check m04l01-03` copies `starter/` into a scratch directory and runs `bash shell-ownership-answers-why.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
