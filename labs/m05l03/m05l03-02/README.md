# m05l03-02 · Read interface state

**Lesson:** [Interfaces, Routes And The Default Gateway](https://learnsome.tech/learn/linux-course/m05l03) (lesson 5.3, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Read interface state and route selection, including the role of a default gateway

In the lesson: The record separates an interface name, administrative state, link state, and address. An interface can be enabled while its physical or virtual link is down. Check both states before blaming a route or remote service.

## Files

- [`starter/shell-read-interface-state.py`](starter/shell-read-interface-state.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `shell-read-interface-state.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' iface=eth0 admin=up link=up ip=192.0.2.42
   ```
4. Run it: `bash shell-read-interface-state.py`.
5. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
iface=eth0
admin=up
link=up
ip=192.0.2.42
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `bash shell-read-interface-state.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
