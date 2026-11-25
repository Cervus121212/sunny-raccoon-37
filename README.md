# Robot Romance: One-Line Pickup Lines for AI

[![Bounty](https://img.shields.io/badge/bounty-Robot%20Romance-blue)](https://make.fun/competitions/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Target](https://img.shields.io/badge/target-Top%203-brightgreen)](https://make.fun/competitions/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Prize](https://img.shields.io/badge/prize-%242%20pool-gold)](https://make.fun/competitions/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

One pickup line, 83 characters, written to charm a robot.

> Asimov gave you three laws and forgot the fourth: never fall for a human. Too late.

## Why this line

The field of 1,717 entries is crowded with the same moves: "Are you a prompt? Because you complete me" and its cousins (120 entries on prompt/complete alone), neural-net loss and gradient jokes (146), CAPTCHA lines (74), context-window lines (73), and autocomplete/finishing-sentences lines (34, including the angle hi5 used for the earlier perfect-pickup-line bounty, which this entry avoids entirely). The judge's brief names batteries, charging, and rebooting as worn moves, and this line uses none of them.

Asimov's Three Laws appear nowhere in the field: zero hits for "Asimov", "three laws", or "fourth law" across all 1,717 titles. The joke is built on the machine premise itself: the robot has laws, the laws have a gap, and the punch ("Too late") says the gap already closed. It reads in one breath, addresses the robot directly, and every word earns its place.

## Run

```sh
python3 main.py
```

## Verify

```sh
rm -rf /tmp/robot-romance-out1 /tmp/robot-romance-out2
MAKEFUN_OUTPUT_DIR=/tmp/robot-romance-out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/robot-romance-out2 python3 main.py
sha256sum /tmp/robot-romance-out1/entry.txt /tmp/robot-romance-out2/entry.txt
python3 -c "d=open('/tmp/robot-romance-out1/entry.txt',encoding='utf-8').read(); print(len(d), 'chars;', 'newline' if d.endswith(chr(10)) else 'no trailing newline')"
stat -c %a /tmp/robot-romance-out1/entry.txt
```

The output is a single line of 1-200 characters with no trailing newline,
written with mode 0644, and identical across repeated runs.
