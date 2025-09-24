# Conditions in Ansible

- **Conditionals**: Used to execute tasks based on specific conditions.

```yaml
---
- name: Install NGINX
  hosts: all
  tasks:
    - name: Install NGINX on Debian
      apt:
        name: nginx
        state: present
      when: ansible_os_family == "Debian" and
        ansible_distribution_version == "16.04"

    - name: Install NGINX on Redhat
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "RedHat" or
        ansible_os_family == "SUSE"
```

```yaml
---
- name: Install Softwares
  hosts: all
  vars:
    packages:
      - name: nginx
        required: True
      - name: mysql
        required: True
      - name: apache
        required: False

  tasks:
    - name: Install "{{ item.name }}" on Debian
      apt:
        name: "{{ item.name }}"
        state: present
      when: item.required == True
      loop: "{{ packages }}"
```

# Loops in Ansible

- **Loops**: Used to iterate over a list of items and perform tasks for each item.
- **loop** and **with_items** are used to create loops in Ansible tasks.
- **item** is a special variable that represents the current item in the loop.

```yaml
---
- name: Create multiple users
  hosts: all
  vars:
    users:
      - name: user1
        uid: 1001
      - name: user2
        uid: 1002
      - name: user3
        uid: 1003
  tasks:
    - name: Create users
      user:
        name: "{{ item.name }}"
        uid: "{{ item.uid }}"
        state: present
      loop: "{{ users }}"
```
