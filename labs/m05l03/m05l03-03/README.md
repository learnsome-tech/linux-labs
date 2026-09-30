# m05l03-03 · Choose the route

**Lesson:** [Interfaces, Routes And The Default Gateway](https://learnsome.tech/learn/linux-course/m05l03) (lesson 5.3, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Read interface state and route selection, including the role of a default gateway

In the lesson: Route selection prefers the most specific matching prefix. The record shows a local network route and a default route through a gateway. A destination inside the local prefix uses the interface directly; an outside destination takes the gateway. When a route test fails, inspect the selected prefix and next hop rather than only checking that an address exists.

## Files

- [`starter/shell-choose-the-route.py`](starter/shell-choose-the-route.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `shell-choose-the-route.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' local=192.0.2.0/24 via=eth0 def=192.0.2.1
   ```
4. Run it: `bash shell-choose-the-route.py`.
5. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
local=192.0.2.0/24
via=eth0
def=192.0.2.1
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `bash shell-choose-the-route.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
