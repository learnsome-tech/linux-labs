# m04l03-02 · Read a storage map

**Lesson:** [Disks, Filesystems And Mounting](https://learnsome.tech/learn/linux-course/m04l03) (lesson 4.3, module 4: Packages, Disks And Space) · Pro  
**Check:** Graded

## Goal

Distinguish block devices, filesystems, and mount points when inspecting storage

In the lesson: The record connects a device to a filesystem and a mount point. On Linux, storage inspection tools provide this map with device names, filesystem types, and mounted paths. Read the map before formatting or mounting anything; the wrong device can destroy unrelated data even when the command itself succeeds.

## Files

- [`starter/shell-read-a-storage-map.py`](starter/shell-read-a-storage-map.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `shell-read-a-storage-map.py`.
3. The session types these commands, in order:

   ```sh
   printf '%s\n' device=disk1 fs=ext4 mount=/srv/data
   ```
4. Run it: `bash shell-read-a-storage-map.py`.
5. Check it from the repository root: `./check m04l03-02`.

## Expected output

```text
device=disk1
fs=ext4
mount=/srv/data
```

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `bash shell-read-a-storage-map.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The expected output is the output recorded in the session itself (its `#   ` comment lines), collected into `expected.txt`. Output is compared line by line; spaces at the end of a line and blank lines at the end do not count, and if that differs standard output followed by standard error is compared with Python traceback frames and blank lines set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/linux-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
