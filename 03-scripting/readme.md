# Terminal, Command Line, Shell, Kernel

## 😀 Terminal

> The window or program you open to interact with the system (like **GNOME Terminal** or **Windows Terminal**).

---

## 😀 Command Line

> The spot inside that terminal window where you type your commands (the blinking cursor at the prompt). _Not a process._

---

## 😀 Shell

> A program that runs in the terminal.  
> Reads your commands, interprets them, and talks to the kernel to run them using system calls.

**Examples:**

- `bash`
- `sh`
- `zsh`

---

# How Shell Works

### Scenario 1: Running a Script

1. You run the script file, e.g., `./myscript.sh`.
2. The kernel checks the first line of the script file (like `#!/bin/bash`).
3. The kernel starts a new `/bin/bash` process.
4. This new `/bin/bash` process opens your script file and starts interpreting it line by line.
5. While interpreting, if the script runs commands like `ls`, `grep`, etc., the `/bin/bash` process starts new child processes to run those commands.
6. When the script finishes interpreting all lines, this `/bin/bash` process exits.
7. The operating system frees all memory used by this `/bin/bash` process.

---

### Scenario 2: Running Commands Interactively in the Terminal

1. You open a terminal, which starts a single `/bin/bash` process running interactively.
2. You type a command, e.g., `ls`, and press Enter.
3. The interactive `/bin/bash` process reads your command and interprets it.
4. If the command is built-in (like `cd` or `echo`), the `/bin/bash` process runs it inside itself.
5. If the command is external (like `ls`, `grep`), the `/bin/bash` process starts a new child process to run that command.
6. When the command finishes, the child process exits and its memory is freed.
7. The interactive `/bin/bash` process waits for your next command.
