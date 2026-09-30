# m08l04-03 · Resolve and route

**Lesson:** [The Diagnostic Ladder: Is It Up, Is It Named, Is It Routed](https://learnsome.tech/learn/linux-course/m08l04) (lesson 8.4, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

You can diagnose a service in order by checking process state, name resolution, and the route to its address.

In the lesson: Next ask the two network questions separately. The first line represents name resolution returning an address. The second represents the route lookup selecting a next hop. If either result is wrong, fix that layer before testing transport or application behaviour.

## Files

- [`starter/shell-resolve-and-route.py`](starter/shell-resolve-and-route.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l04/m08l04-03/starter`
2. Read `shell-resolve-and-route.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' name=resolved
   printf '%s\n' route=selected
   ```
4. Run it: `bash shell-resolve-and-route.py`.
5. Check it from the repository root: `./check m08l04-03`.

## Expected output

```text
name=resolved
route=selected
```

## How to check

`./check m08l04-03` copies `starter/` into a scratch directory and runs `bash shell-resolve-and-route.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
