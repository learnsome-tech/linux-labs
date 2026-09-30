# m06l02-03 · Bind address changes reachability

**Lesson:** [Ports, Sockets And What Listening Means](https://learnsome.tech/learn/linux-course/m06l02) (lesson 6.2, module 6: Transport, Ports And Sockets) · Pro  
**Check:** Graded

## Goal

Distinguish a port, socket, and listening endpoint when inspecting a service

In the lesson: Two services can listen on the same port when they bind to different local addresses, while one wildcard bind can claim that port everywhere. The record contrasts loopback and wildcard behavior. When a local health check succeeds but a remote client fails, inspect the bind address before changing firewall rules.

## Files

- [`starter/shell-bind-address-changes-reachability.py`](starter/shell-bind-address-changes-reachability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-03/starter`
2. Read `shell-bind-address-changes-reachability.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' local=127.0.0.1 host=only any=0.0.0.0 host=all
   ```
4. Run it: `bash shell-bind-address-changes-reachability.py`.
5. Check it from the repository root: `./check m06l02-03`.

## Expected output

```text
local=127.0.0.1
host=only
any=0.0.0.0
host=all
```

## How to check

`./check m06l02-03` copies `starter/` into a scratch directory and runs `bash shell-bind-address-changes-reachability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
