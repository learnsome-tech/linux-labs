# m06l03-02 · Read the handshake

**Lesson:** [The Handshake, And The States A Socket Passes Through](https://learnsome.tech/learn/linux-course/m06l03) (lesson 6.3, module 6: Transport, Ports And Sockets) · Pro  
**Check:** Graded

## Goal

Trace the TCP handshake and use socket states to locate connection progress

In the lesson: The record lists the handshake messages in order: request, acknowledgment with a synchronize, then final acknowledgment. It is the sequence to look for in a packet trace. If the first message leaves no reply, the problem is below the application protocol.

## Files

- [`starter/shell-read-the-handshake.py`](starter/shell-read-the-handshake.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `shell-read-the-handshake.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' one=SYN two=SYN-ACK three=ACK result=established
   ```
4. Run it: `bash shell-read-the-handshake.py`.
5. Check it from the repository root: `./check m06l03-02`.

## Expected output

```text
one=SYN
two=SYN-ACK
three=ACK
result=established
```

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `bash shell-read-the-handshake.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
