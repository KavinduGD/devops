# Ansible Modules

- **Modules**: Predefined scripts that perform specific tasks in Ansible.
  - Examples: `file`, `copy`, `yum`, `apt`, `service`

## Basic Modules

- **ping** - check connectivity to remote hosts(not same as ICMP ping)
- **setup** - gather facts about remote hosts. Called automatically at the start of a playbook run unless disabled.
- **file** - manage file and directory properties (e.g., create, delete, set permissions)
- **copy** - copy files from the control machine to remote hosts
- **command** - run a command on remote hosts (does not use a shell)
- **fetch** - fetch files from remote hosts to the control machine
- **set_fact** - set custom facts for use later in the playbook
- **pause** - pause playbook execution for a specified amount of time or until user input
- **wait_for** - wait for a condition before proceeding (e.g., wait for a port to be open)

---

## Idempotency in Modules

- Modules are designed to be idempotent, meaning running the same module multiple times will not change the system.
  - Example: Installing a package that is already installed will not reinstall it.

## Plugins in Ansible

### 🔹 Types of Ansible Plugins

Ansible ships with many plugin types. Here are the main categories:

1. **Action Plugins**  
   Modify how modules are run.  
   Examples: `normal`, `async`, `wait_for_connection`  
   Use case: Customize how a module is executed on the remote node.

   ```yaml
   - name: Run command asynchronously
     command: /usr/bin/long_task
     async: 45
     poll: 0
   ```

   Here Ansible uses the async action plugin to execute the task without waiting.

2. **Callback Plugins**  
   Control output format and logging.  
   Examples: `default`, `json`, `yaml`, `minimal`, `profile_tasks`  
   Use case: Customize how playbook results appear or send logs to an external system.

   ```bash
   ANSIBLE_STDOUT_CALLBACK=yaml ansible-playbook play.yml
   ```

   👉 This makes Ansible output results in YAML instead of default human-readable text.

3. **Connection Plugins**  
   Define how Ansible connects to remote systems.  
   Examples: `ssh`, `paramiko`, `local`, `docker`, `winrm`  
   Use case: Run playbooks over different protocols.

   ```yaml
   - hosts: all
     connection: docker
     tasks:
       - name: Check hostname inside container
         command: hostname
   ```

4. **Filter Plugins**  
   Extend Jinja2 filters for templates.  
   Examples: `ipaddr`, `to_nice_json`, `b64encode`  
   Use case: Transform variables in playbooks/templates.

   ```yaml
   - debug:
       msg: "{{ 'Hello World' | b64encode }}"
   ```

   **Output:**

   ```yaml
   ok: [localhost] => {
     "msg": "SGVsbG8gV29ybGQ="
   }
   ```

5. **Lookup Plugins**  
   Fetch data from external sources.  
   Examples: `file`, `env`, `passwordstore`, `aws_ssm`  
   Use case: Dynamically pull in variables.

   ```yaml
   - debug:
       msg: "{{ lookup('env', 'HOME') }}"
   ```

6. **Strategy Plugins**  
   Control execution strategy of tasks across hosts.  
   Examples: `linear` (default), `free`, `debug`  
   Use case: Run tasks in parallel or debug execution.

   ```bash
   ansible-playbook site.yml -e ansible_strategy=free
   ```

7. **Vars Plugins**  
   Load variables dynamically from sources like vaults, inventory, etc.  
   Examples: `host_group_vars`, `yaml`, `ini`  
   Use case: Auto-load vars depending on environment.

8. **Inventory Plugins**  
   Define how inventory is sourced.  
   Examples: `yaml`, `ini`, `aws_ec2`, `gcp_compute`, `azure_rm`  
   Use case: Dynamic inventory from cloud providers.

   ```bash
   ansible-inventory -i aws_ec2.yml --list
   ```

9. **Test Plugins**  
   Custom assertions for conditions in playbooks.  
   Examples: `is_ipv4`, `is_macos`, `is_version`  
   Use case: Validate inputs or states.

   ```yaml
   - assert:
       that:
         - ansible_os_family is match("Debian")
   ```

### 🔹 Plugin Index (Where They Live)

The plugin index is the searchable catalog of plugins in Ansible.  
You can browse it in two ways:

- **Official Documentation:**  
  Ansible Plugin Index  
  It lists plugins by type (action, callback, connection, etc.) with descriptions and examples.

- **Command Line (local search):**

  ```bash
  ansible-doc -t callback -l      # List all callback plugins
  ansible-doc -t connection -l    # List all connection plugins
  ansible-doc -t filter -l        # List all filter plugins
  ```

  **Example:**

  ```bash
  ansible-doc -t callback profile_tasks
  ```

  **Output:**

  ```
  profile_tasks - adds time profiling to tasks
  ```
