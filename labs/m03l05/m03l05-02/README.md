# m03l05-02 · Read a unit relationship

**Lesson:** [systemd: Units, Targets And The Boot Graph](https://learnsome.tech/learn/linux-course/m03l05) (lesson 3.5, module 3: Processes, Signals And Services) · Pro  
**Check:** Graded

## Goal

Read systemd units and targets as a dependency graph rather than a flat startup script

In the lesson: The record shows a web service enabled by a target and ordered after the network is ready. It is a small view of the dependency graph: the target wants the service, and the service starts after networking. On a Linux host, unit inspection commands expose the complete graph; begin by reading the relationships before changing them.

## Files

- [`starter/shell-read-a-unit-relationship.py`](starter/shell-read-a-unit-relationship.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `shell-read-a-unit-relationship.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' unit=web target=multi wants=web after=net
   ```
4. Run it: `bash shell-read-a-unit-relationship.py`.
5. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
unit=web
target=multi
wants=web
after=net
```

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-unit-relationship.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
