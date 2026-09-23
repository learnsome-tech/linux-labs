# Linux Fundamentals & Systems Administration — lesson m03l05 — systemd: Units, Targets And The Boot Graph
# https://learnsome.tech/courses/linux-course/watch?lesson=m03l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

printf '%s\n' unit=web target=multi wants=web after=net
#   unit=web
#   target=multi
#   wants=web
#   after=net
