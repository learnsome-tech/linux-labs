# m04l01-02 · Record a package plan

**Lesson:** [What A Package Manager Guarantees](https://learnsome.tech/learn/linux-course/m04l01) (lesson 4.1, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Explain how a package manager tracks files, dependencies, versions, and trusted sources

In the lesson: The record shows the information a package transaction should make explicit: name, version, source, and dependencies. A real package manager obtains these fields from signed repository metadata. Read the plan before applying it, especially on a production host where an upgrade can replace configuration or restart a service.

## Files

- [`starter/shell-record-a-package-plan.py`](starter/shell-record-a-package-plan.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `shell-record-a-package-plan.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' name=web version=2 source=stable deps=ssl
   ```
4. Run it: `bash shell-record-a-package-plan.py`.
5. Check it from the repository root: `./check m04l01-02`.

## Expected output

```text
name=web
version=2
source=stable
deps=ssl
```

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `bash shell-record-a-package-plan.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
