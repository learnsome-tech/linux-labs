# m05l02-02 · Read a subnet

**Lesson:** [IP Addresses, Netmasks And Subnets](https://learnsome.tech/learn/linux-course/m05l02) (lesson 5.2, module 5: Addresses And Routes) · Pro  
**Check:** Graded

## Goal

Calculate a host and network boundary from an IP address and prefix length

In the lesson: The record gives an address with a twenty four bit prefix and names its network and host portions. The values are fixed for a portable demonstration. In a real incident, calculate the boundary before deciding whether a peer should be reached directly or through a router.

## Files

- [`starter/shell-read-a-subnet.py`](starter/shell-read-a-subnet.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `shell-read-a-subnet.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' ip=192.0.2.42 p=24 net=192.0.2.0 host=42
   ```
4. Run it: `bash shell-read-a-subnet.py`.
5. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
ip=192.0.2.42
p=24
net=192.0.2.0
host=42
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-subnet.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
