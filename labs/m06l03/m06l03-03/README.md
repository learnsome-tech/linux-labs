# m06l03-03 · Interpret a socket state

**Lesson:** [The Handshake, And The States A Socket Passes Through](https://learnsome.tech/learn/linux-course/m06l03) (lesson 6.3, module 6: Transport, Ports And Sockets) · Pro  
**Check:** Graded

## Goal

Trace the TCP handshake and use socket states to locate connection progress

In the lesson: A state snapshot tells you which part of the exchange has progressed. The record shows a client waiting after sending a synchronize and a server still listening. That combination points toward a missing or blocked reply, not an HTTP handler bug. Compare both endpoints when the state does not advance.

## Files

- [`starter/shell-interpret-a-socket-state.py`](starter/shell-interpret-a-socket-state.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-03/starter`
2. Read `shell-interpret-a-socket-state.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' client=SYN-SENT server=LISTEN next=reply
   ```
4. Run it: `bash shell-interpret-a-socket-state.py`.
5. Check it from the repository root: `./check m06l03-03`.

## Expected output

```text
client=SYN-SENT
server=LISTEN
next=reply
```

## How to check

`./check m06l03-03` copies `starter/` into a scratch directory and runs `bash shell-interpret-a-socket-state.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
