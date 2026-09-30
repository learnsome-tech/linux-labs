# m08l01-03 · State changes the return path

**Lesson:** [Firewalls: Default Deny, State And Rule Order](https://learnsome.tech/learn/linux-course/m08l01) (lesson 8.1, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

Reason about firewall defaults, stateful return traffic, and first-match rule order

In the lesson: A stateful firewall records an outbound connection and permits its matching return traffic. The record shows an outbound request, an established state, and a return decision. This is narrower than allowing every inbound packet to the same port, but it still depends on correct state tracking and rule placement.

## Files

- [`starter/shell-state-changes-the-return-path.py`](starter/shell-state-changes-the-return-path.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-03/starter`
2. Read `shell-state-changes-the-return-path.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' out=yes state=est reply=yes new=no
   ```
4. Run it: `bash shell-state-changes-the-return-path.py`.
5. Check it from the repository root: `./check m08l01-03`.

## Expected output

```text
out=yes
state=est
reply=yes
new=no
```

## How to check

`./check m08l01-03` copies `starter/` into a scratch directory and runs `bash shell-state-changes-the-return-path.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
