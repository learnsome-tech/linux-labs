# m08l01-02 · Read a firewall policy

**Lesson:** [Firewalls: Default Deny, State And Rule Order](https://learnsome.tech/learn/linux-course/m08l01) (lesson 8.1, module 8: Serving, Guarding And Diagnosing) · Pro  
**Check:** Graded

## Goal

Reason about firewall defaults, stateful return traffic, and first-match rule order

In the lesson: The record describes a narrow inbound rule for a web port and a default deny policy after it. The fields make the scope visible: direction, protocol, destination port, and source. Review that scope before widening a rule to every interface or address.

## Files

- [`starter/shell-read-a-firewall-policy.py`](starter/shell-read-a-firewall-policy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-02/starter`
2. Read `shell-read-a-firewall-policy.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' in=tcp p=443 src=any act=allow def=deny
   ```
4. Run it: `bash shell-read-a-firewall-policy.py`.
5. Check it from the repository root: `./check m08l01-02`.

## Expected output

```text
in=tcp
p=443
src=any
act=allow
def=deny
```

## How to check

`./check m08l01-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-firewall-policy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
