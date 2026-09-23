<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Linux Fundamentals & Systems Administration

8 modules, 39 lessons: The Kernel, The Distribution, The Filesystem; Users, Groups And Permissions; Processes, Signals And Services; Packages, Disks And Space; Addresses And Routes; Transport, Ports And Sockets; HTTP, TLS And SSH; Serving, Guarding And Diagnosing.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/linux-course](https://learnsome.tech/courses/linux-course)
- **Video player**: [https://learnsome.tech/courses/linux-course/watch](https://learnsome.tech/courses/linux-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/linux/book.pdf](https://learnsome.tech/handbooks/linux/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/linux-course/book](https://learnsome.tech/courses/linux-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
39 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **The Kernel, The Distribution, The Filesystem** | | | |
| 1 | What A Kernel Does, And What It Refuses To Do | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-1-1) |
| 2 | What A Distribution Actually Is | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-1-2) |
| 3 | The Filesystem Hierarchy | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-1-3) |
| 4 | Inodes, Hard Links And What rm Removes | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-1-4) |
| 5 | Everything Is A File: proc, sys And dev | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-1-5) |
| | **Users, Groups And Permissions** | | | |
| 6 | Users, UIDs And The Password File | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-2-1) |
| 7 | Groups, And How Shared Access Is Granted | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-2-2) |
| 8 | Reading And Setting A File Mode | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-2-3) |
| 9 | Directories, Umask And The Sticky Bit | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-2-4) |
| 10 | Setuid, Setgid, And Root Through sudo | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-2-5) |
| | **Processes, Signals And Services** | | | |
| 11 | What A Process Is | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-1) |
| 12 | Signals, And What kill Really Sends | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-2) |
| 13 | Job Control, And Processes That Outlive You | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-3) |
| 14 | Booting: GRUB, The Kernel Command Line And initramfs | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-4) |
| 15 | systemd: Units, Targets And The Boot Graph | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-5) |
| 16 | Your Own Unit, And Reading journald | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m03l06) | [labs/m03l06/](labs/m03l06/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-3-6) |
| | **Packages, Disks And Space** | | | |
| 17 | What A Package Manager Guarantees | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-4-1) |
| 18 | Three Families: apt, dnf And pacman | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-4-2) |
| 19 | Disks, Filesystems And Mounting | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-4-3) |
| 20 | Running Out Of Space: df, du And Inodes | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-4-4) |
| | **Addresses And Routes** | | | |
| 21 | The Layer Model, As Far As It Earns Its Place | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-5-1) |
| 22 | IP Addresses, Netmasks And Subnets | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-5-2) |
| 23 | Interfaces, Routes And The Default Gateway | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-5-3) |
| 24 | DNS Resolution, End To End | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-5-4) |
| 25 | Record Types, Caching And Time To Live | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m05l05) | [labs/m05l05/](labs/m05l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-5-5) |
| | **Transport, Ports And Sockets** | | | |
| 26 | TCP Versus UDP | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m06l01) | [labs/m06l01/](labs/m06l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-6-1) |
| 27 | Ports, Sockets And What Listening Means | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m06l02) | [labs/m06l02/](labs/m06l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-6-2) |
| 28 | The Handshake, And The States A Socket Passes Through | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m06l03) | [labs/m06l03/](labs/m06l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-6-3) |
| 29 | Refused, Timed Out, Reset: Reading A Failure | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m06l04) | [labs/m06l04/](labs/m06l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-6-4) |
| | **HTTP, TLS And SSH** | | | |
| 30 | HTTP Is Text: Requests, Status Codes And Headers | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m07l01) | [labs/m07l01/](labs/m07l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-7-1) |
| 31 | What HTTPS Adds, And What It Does Not | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m07l02) | [labs/m07l02/](labs/m07l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-7-2) |
| 32 | Certificates, Chains And What A Handshake Proves | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m07l03) | [labs/m07l03/](labs/m07l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-7-3) |
| 33 | SSH: The Protocol, And The Host Key You Accept | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m07l04) | [labs/m07l04/](labs/m07l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-7-4) |
| 34 | SSH Keys, The Agent And The Config File | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m07l05) | [labs/m07l05/](labs/m07l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-7-5) |
| | **Serving, Guarding And Diagnosing** | | | |
| 35 | Firewalls: Default Deny, State And Rule Order | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m08l01) | [labs/m08l01/](labs/m08l01/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-8-1) |
| 36 | Forward And Reverse Proxies | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m08l02) | [labs/m08l02/](labs/m08l02/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-8-2) |
| 37 | Load Balancing: Algorithms, Health Checks And Layers | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m08l03) | [labs/m08l03/](labs/m08l03/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-8-3) |
| 38 | The Diagnostic Ladder: Is It Up, Is It Named, Is It Routed | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m08l04) | [labs/m08l04/](labs/m08l04/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-8-4) |
| 39 | The Diagnostic Ladder: Is It Listening, Answering, Arriving | [▶](https://learnsome.tech/courses/linux-course/watch?lesson=m08l05) | [labs/m08l05/](labs/m08l05/) | [§](https://learnsome.tech/courses/linux-course/book#lesson-8-5) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
