# m06l01-02 · Compare transport choices

**Lesson:** [TCP Versus UDP](https://learnsome.tech/learn/linux-course/m06l01) (lesson 6.1, module 6: Transport, Ports And Sockets) · Pro  
**Check:** Graded

## Goal

Choose between TCP and UDP by comparing connection state, delivery guarantees, and application needs

In the lesson: The record compares the properties an application cares about: connection state, ordering, and retransmission. A file transfer usually wants the TCP contract, while a time-sensitive datagram protocol may accept loss to avoid waiting for old data. Choose from the behavior, not from a preference for one acronym.

## Files

- [`starter/shell-compare-transport-choices.py`](starter/shell-compare-transport-choices.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-02/starter`
2. Read `shell-compare-transport-choices.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' tcp=s o=y r=y udp=d o=n r=n
   ```
4. Run it: `bash shell-compare-transport-choices.py`.
5. Check it from the repository root: `./check m06l01-02`.

## Expected output

```text
tcp=s
o=y
r=y
udp=d
o=n
r=n
```

## How to check

`./check m06l01-02` copies `starter/` into a scratch directory and runs `bash shell-compare-transport-choices.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
