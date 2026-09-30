# m07l05-02 · Read a host alias

**Lesson:** [SSH Keys, The Agent And The Config File](https://learnsome.tech/learn/linux-course/m07l05) (lesson 7.5, module 7: HTTP, TLS And SSH) · Pro  
**Check:** Graded

## Goal

Use SSH key, agent, and host configuration concepts without confusing convenience with authorization

In the lesson: The record describes a host alias with its real name, user, port, and preferred identity file. A config alias reduces typing but does not bypass host key checks or server authorization. Review the expanded values when debugging a connection that reaches the wrong account or port.

## Files

- [`starter/shell-read-a-host-alias.py`](starter/shell-read-a-host-alias.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-02/starter`
2. Read `shell-read-a-host-alias.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' alias=prod host=server user=ana p=22 key=id_ed
   ```
4. Run it: `bash shell-read-a-host-alias.py`.
5. Check it from the repository root: `./check m07l05-02`.

## Expected output

```text
alias=prod
host=server
user=ana
p=22
key=id_ed
```

## How to check

`./check m07l05-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-host-alias.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
