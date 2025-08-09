## Login shell

When you open a terminal or switch to a shell that asks for your username and password first before showing a prompt, that shell is a login shell.

> Logging in via SSH.
> Switching user with su - or logging in on a virtual console (Ctrl+Alt+F2).

- **Login shells read files like /etc/profile and ~/.profile first to set environment variables and user settings.**

## Non-login shell

When you open a terminal (like GNOME Terminal, VS Code terminal, or opening a new tab in your terminal) and it does NOT ask for username/password and just shows the prompt right away, that shell is a non-login shell.

- **Non-login shells read files like ~/.bashrc which usually contain aliases, functions, and interactive settings.**

---

# Different ways of setting envs

- **export in terminal**: can pass current shell to child processes. **Per session**
- **.bashrc**: sets environment variables for non-login shells. **Per user**
- **.profile**: sets environment variables for login shells. **Per user**
- **/etc/profile**: sets environment variables for all users on the system. **System-wide**
