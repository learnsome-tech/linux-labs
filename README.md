<p>
  <a href="https://learnsome.tech/courses/linux-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Linux Fundamentals & Systems Administration

**Kernel Architecture, File Permissions, Process Trees & Systemd**

8 modules, 39 lessons: The Kernel, The Distribution, The Filesystem; Users, Groups And Permissions; Processes, Signals And Services; Packages, Disks And Space; Addresses And Routes; Transport, Ports And Sockets; HTTP, TLS And SSH; Serving, Guarding And Diagnosing. Beginner level, about 1 hour.

This repository holds the labs of the LearnSome.tech course [Linux Fundamentals & Systems Administration](https://learnsome.tech/courses/linux-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/linux-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/linux-labs.git
  cd linux-labs
  ./check m01l01-02
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-02`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 78 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: The Kernel, The Distribution, The Filesystem

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [What A Kernel Does, And What It Refuses To Do](https://learnsome.tech/learn/linux-course/m01l01) | [2 labs](labs/m01l01/) | Free |
| 1.2 | [What A Distribution Actually Is](https://learnsome.tech/learn/linux-course/m01l02) | [2 labs](labs/m01l02/) | Free |
| 1.3 | [The Filesystem Hierarchy](https://learnsome.tech/learn/linux-course/m01l03) | [2 labs](labs/m01l03/) | Free |
| 1.4 | [Inodes, Hard Links And What rm Removes](https://learnsome.tech/learn/linux-course/m01l04) | [2 labs](labs/m01l04/) | Free |
| 1.5 | [Everything Is A File: proc, sys And dev](https://learnsome.tech/learn/linux-course/m01l05) | [2 labs](labs/m01l05/) | Free |

### Module 2: Users, Groups And Permissions

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Users, UIDs And The Password File](https://learnsome.tech/learn/linux-course/m02l01) | [2 labs](labs/m02l01/) | Pro |
| 2.2 | [Groups, And How Shared Access Is Granted](https://learnsome.tech/learn/linux-course/m02l02) | [2 labs](labs/m02l02/) | Pro |
| 2.3 | [Reading And Setting A File Mode](https://learnsome.tech/learn/linux-course/m02l03) | [2 labs](labs/m02l03/) | Pro |
| 2.4 | [Directories, Umask And The Sticky Bit](https://learnsome.tech/learn/linux-course/m02l04) | [2 labs](labs/m02l04/) | Pro |
| 2.5 | [Setuid, Setgid, And Root Through sudo](https://learnsome.tech/learn/linux-course/m02l05) | [2 labs](labs/m02l05/) | Pro |

### Module 3: Processes, Signals And Services

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [What A Process Is](https://learnsome.tech/learn/linux-course/m03l01) | [2 labs](labs/m03l01/) | Pro |
| 3.2 | [Signals, And What kill Really Sends](https://learnsome.tech/learn/linux-course/m03l02) | [2 labs](labs/m03l02/) | Pro |
| 3.3 | [Job Control, And Processes That Outlive You](https://learnsome.tech/learn/linux-course/m03l03) | [2 labs](labs/m03l03/) | Pro |
| 3.4 | [Booting: GRUB, The Kernel Command Line And initramfs](https://learnsome.tech/learn/linux-course/m03l04) | [2 labs](labs/m03l04/) | Pro |
| 3.5 | [systemd: Units, Targets And The Boot Graph](https://learnsome.tech/learn/linux-course/m03l05) | [2 labs](labs/m03l05/) | Pro |
| 3.6 | [Your Own Unit, And Reading journald](https://learnsome.tech/learn/linux-course/m03l06) | [2 labs](labs/m03l06/) | Pro |

### Module 4: Packages, Disks And Space

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [What A Package Manager Guarantees](https://learnsome.tech/learn/linux-course/m04l01) | [2 labs](labs/m04l01/) | Pro |
| 4.2 | [Three Families: apt, dnf And pacman](https://learnsome.tech/learn/linux-course/m04l02) | [2 labs](labs/m04l02/) | Pro |
| 4.3 | [Disks, Filesystems And Mounting](https://learnsome.tech/learn/linux-course/m04l03) | [2 labs](labs/m04l03/) | Pro |
| 4.4 | [Running Out Of Space: df, du And Inodes](https://learnsome.tech/learn/linux-course/m04l04) | [2 labs](labs/m04l04/) | Pro |

### Module 5: Addresses And Routes

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [The Layer Model, As Far As It Earns Its Place](https://learnsome.tech/learn/linux-course/m05l01) | [2 labs](labs/m05l01/) | Pro |
| 5.2 | [IP Addresses, Netmasks And Subnets](https://learnsome.tech/learn/linux-course/m05l02) | [2 labs](labs/m05l02/) | Pro |
| 5.3 | [Interfaces, Routes And The Default Gateway](https://learnsome.tech/learn/linux-course/m05l03) | [2 labs](labs/m05l03/) | Pro |
| 5.4 | [DNS Resolution, End To End](https://learnsome.tech/learn/linux-course/m05l04) | [2 labs](labs/m05l04/) | Pro |
| 5.5 | [Record Types, Caching And Time To Live](https://learnsome.tech/learn/linux-course/m05l05) | [2 labs](labs/m05l05/) | Pro |

### Module 6: Transport, Ports And Sockets

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [TCP Versus UDP](https://learnsome.tech/learn/linux-course/m06l01) | [2 labs](labs/m06l01/) | Pro |
| 6.2 | [Ports, Sockets And What Listening Means](https://learnsome.tech/learn/linux-course/m06l02) | [2 labs](labs/m06l02/) | Pro |
| 6.3 | [The Handshake, And The States A Socket Passes Through](https://learnsome.tech/learn/linux-course/m06l03) | [2 labs](labs/m06l03/) | Pro |
| 6.4 | [Refused, Timed Out, Reset: Reading A Failure](https://learnsome.tech/learn/linux-course/m06l04) | [2 labs](labs/m06l04/) | Pro |

### Module 7: HTTP, TLS And SSH

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 7.1 | [HTTP Is Text: Requests, Status Codes And Headers](https://learnsome.tech/learn/linux-course/m07l01) | [2 labs](labs/m07l01/) | Pro |
| 7.2 | [What HTTPS Adds, And What It Does Not](https://learnsome.tech/learn/linux-course/m07l02) | [2 labs](labs/m07l02/) | Pro |
| 7.3 | [Certificates, Chains And What A Handshake Proves](https://learnsome.tech/learn/linux-course/m07l03) | [2 labs](labs/m07l03/) | Pro |
| 7.4 | [SSH: The Protocol, And The Host Key You Accept](https://learnsome.tech/learn/linux-course/m07l04) | [2 labs](labs/m07l04/) | Pro |
| 7.5 | [SSH Keys, The Agent And The Config File](https://learnsome.tech/learn/linux-course/m07l05) | [2 labs](labs/m07l05/) | Pro |

### Module 8: Serving, Guarding And Diagnosing

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 8.1 | [Firewalls: Default Deny, State And Rule Order](https://learnsome.tech/learn/linux-course/m08l01) | [2 labs](labs/m08l01/) | Pro |
| 8.2 | [Forward And Reverse Proxies](https://learnsome.tech/learn/linux-course/m08l02) | [2 labs](labs/m08l02/) | Pro |
| 8.3 | [Load Balancing: Algorithms, Health Checks And Layers](https://learnsome.tech/learn/linux-course/m08l03) | [2 labs](labs/m08l03/) | Pro |
| 8.4 | [The Diagnostic Ladder: Is It Up, Is It Named, Is It Routed](https://learnsome.tech/learn/linux-course/m08l04) | [2 labs](labs/m08l04/) | Pro |
| 8.5 | [The Diagnostic Ladder: Is It Listening, Answering, Arriving](https://learnsome.tech/learn/linux-course/m08l05) | [2 labs](labs/m08l05/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
