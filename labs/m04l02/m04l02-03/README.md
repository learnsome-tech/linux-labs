# m04l02-03 · Compare a transaction preview

**Lesson:** [Three Families: apt, dnf And pacman](https://learnsome.tech/learn/linux-course/m04l02) (lesson 4.2, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Recognize the apt, dnf, and pacman package families and choose commands from the host distribution

In the lesson: A preview should tell you what will change before files move. This record compares the same requested package across two families and makes the planned action visible. Look for removals, replacements, held packages, and service restarts in a real preview; a short install command can have a wide dependency effect.

## Files

- [`starter/shell-compare-a-transaction-preview.py`](starter/shell-compare-a-transaction-preview.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `shell-compare-a-transaction-preview.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' fam=apt package=web action=install preview=yes
   ```
4. Run it: `bash shell-compare-a-transaction-preview.py`.
5. Check it from the repository root: `./check m04l02-03`.

## Expected output

```text
fam=apt
package=web
action=install
preview=yes
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `bash shell-compare-a-transaction-preview.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
