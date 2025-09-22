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
