# Linux Fundamentals & Systems Administration — lesson m03l04 — Booting: GRUB, The Kernel Command Line And initramfs
# https://learnsome.tech/courses/linux-course/watch?lesson=m03l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

printf '%s\n' root=/dev/root loglevel=4 console=tty quiet=yes
#   root=/dev/root
#   loglevel=4
#   console=tty
#   quiet=yes
