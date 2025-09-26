## 🔹 What is an Ansible Role?

An **Ansible Role** is a way to organize playbooks and reusable automation code. Instead of placing all configuration in a single playbook, roles allow you to split automation into structured, self-contained directories.

> **Roles** are modular units of automation (e.g., “install nginx”, “deploy app”, “configure database”).

### 🔸 Structure of a Role

A typical role has this directory layout:

```
roles/
    └── myrole/
            ├── tasks/        # main.yml: tasks to execute
            ├── handlers/     # main.yml: handlers (e.g., restart services)
            ├── templates/    # Jinja2 templates
            ├── files/        # static files to copy
            ├── vars/         # variable definitions
            ├── defaults/     # default (lowest-priority) variables
            ├── meta/         # metadata (dependencies, galaxy info)
            └── tests/        # optional test playbooks
```

### 🔸 Example Role: nginx

**tasks/main.yml**

```yaml
- name: Install nginx
    apt:
        name: nginx
        state: present
    become: yes

- name: Start nginx
    service:
        name: nginx
        state: started
        enabled: yes
```

**handlers/main.yml**

```yaml
- name: Restart nginx
    service:
        name: nginx
        state: restarted
```

**playbook.yml**

```yaml
- hosts: webservers
    roles:
        - nginx
```

> Using roles keeps playbooks clean and modular.

---

## 🔹 What is an Ansible Collection?

An **Ansible Collection** is a distribution format that bundles roles, modules, and plugins together. Collections are used to share and distribute automation content at scale (e.g., via Ansible Galaxy or internally).

### 🔸 Structure of a Collection

```
ansible_collections/
    └── mynamespace/
            └── mycollection/
                    ├── roles/        # roles live here
                    ├── plugins/      # modules, filters, inventory, etc.
                    ├── docs/         # documentation
                    ├── playbooks/    # example playbooks
                    ├── tests/
                    └── galaxy.yml    # metadata (name, version, dependencies)
```

### 🔸 Example Collection: `mynamespace.web`

**galaxy.yml**

```yaml
namespace: mynamespace
name: web
version: 1.0.0
readme: README.md
```

A collection can include:

- **Roles**: e.g., `nginx`, `apache`
- **Plugins**: custom filters, inventory scripts
- **Modules**: custom tasks not in Ansible core

Install a collection:

```sh
ansible-galaxy collection install mynamespace.web
```

Use a role from a collection in a playbook:

```yaml
- hosts: webservers
    roles:
        - mynamespace.web.nginx   # role inside collection
```
