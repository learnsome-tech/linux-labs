# m05l02-03 · Compare two destinations

**Lesson:** [IP Addresses, Netmasks And Subnets](https://learnsome.tech/learn/linux-course/m05l02) (lesson 5.2, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Calculate a host and network boundary from an IP address and prefix length

In the lesson: Two addresses with the same prefix can be local to one another, while an address outside that range needs a route to a gateway. The record classifies both outcomes. Do not infer reachability from address appearance alone; compare the prefix and then inspect the route table.

## Files

- [`starter/shell-compare-two-destinations.py`](starter/shell-compare-two-destinations.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `shell-compare-two-destinations.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' a=192.0.2.9 local=y b=198.51.100.9 local=n
   ```
4. Run it: `bash shell-compare-two-destinations.py`.
5. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
a=192.0.2.9
local=y
b=198.51.100.9
local=n
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `bash shell-compare-two-destinations.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
