# m08l02-03 · Apply forward policy

**Lesson:** [Forward And Reverse Proxies](https://learnsome.tech/learn/linux-course/m08l02) (lesson 8.2, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

Distinguish forward and reverse proxy roles and identify where each one terminates a request

In the lesson: A forward proxy evaluates the client and destination before allowing an outbound request. The record names a user, destination, and policy decision. A failed request may therefore belong to client identity, proxy policy, destination routing, or the remote service; identify the leg before changing the rule.

## Files

- [`starter/shell-apply-forward-policy.py`](starter/shell-apply-forward-policy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-03/starter`
2. Read `shell-apply-forward-policy.py`.
3. The session types these commands, in order:

   ```sh
   echo -e 'mode=fwd\nuser=ana\ndest=ex\nallow=yes\ncache=hit'
   ```
4. Run it: `bash shell-apply-forward-policy.py`.
5. Check it from the repository root: `./check m08l02-03`.

## Expected output

```text
mode=fwd
user=ana
dest=ex
allow=yes
cache=hit
```

## How to check

`./check m08l02-03` copies `starter/` into a scratch directory and runs `bash shell-apply-forward-policy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
