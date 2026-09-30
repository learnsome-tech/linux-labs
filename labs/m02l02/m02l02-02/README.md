# m02l02-02 · Describe a shared project

**Lesson:** [Groups, And How Shared Access Is Granted](https://learnsome.tech/learn/linux-course/m02l02) (lesson 2.2, module 2: Users, Groups And Permissions) · Pro  
**Check:** Graded

## Goal

Use supplementary groups to reason about shared ownership and access without making files world writable

In the lesson: The example describes a project directory whose group is writers. Alice and Bob belong to that group, while Carol does not. A real host would show this with account and group lookup commands; this portable record lets us focus on the relationship. The directory's group ownership is the shared policy, and membership determines who can use it.

## Files

- [`starter/shell-describe-a-shared-project.py`](starter/shell-describe-a-shared-project.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-02/starter`
2. Read `shell-describe-a-shared-project.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' path=/srv/p group=writers members=alice,bob
   ```
4. Run it: `bash shell-describe-a-shared-project.py`.
5. Check it from the repository root: `./check m02l02-02`.

## Expected output

```text
path=/srv/p
group=writers
members=alice,bob
```

## How to check

`./check m02l02-02` copies `starter/` into a scratch directory and runs `bash shell-describe-a-shared-project.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
