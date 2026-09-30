# m07l05-03 · Track the agent session

**Lesson:** [SSH Keys, The Agent And The Config File](https://learnsome.tech/learn/linux-course/m07l05) (lesson 7.5, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Use SSH key, agent, and host configuration concepts without confusing convenience with authorization

In the lesson: An agent is a local key broker, not a remote permission grant. The record shows a key loaded for one session and an explicit forwarding policy. Limit agent lifetime and forwarding because a process that can reach the agent may ask it to authenticate elsewhere. Remove keys when the work is finished.

## Files

- [`starter/shell-track-the-agent-session.py`](starter/shell-track-the-agent-session.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-03/starter`
2. Read `shell-track-the-agent-session.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' agent=on keys=1 fwd=off life=session
   ```
4. Run it: `bash shell-track-the-agent-session.py`.
5. Check it from the repository root: `./check m07l05-03`.

## Expected output

```text
agent=on
keys=1
fwd=off
life=session
```

## How to check

`./check m07l05-03` copies `starter/` into a scratch directory and runs `bash shell-track-the-agent-session.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
