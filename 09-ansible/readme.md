# Ansible

- **Simple** - human-readable automation
- **Many usecases** - provisioning, configuration management, application deployment, orchestration, network automation
- **Agentless** - no need to install agents (ansible) on target machines

### architecture

<img src="./images/architecture.png" width="600" />

### order in which Ansible looks for its configuration file

1. /etc/ansible/ansible.cfg (system-wide config)
2. ~/.ansible.cfg (user-specific config)
3. ./ansible.cfg (project-specific config)
4. ANSIBLE_CONFIG environment variable

task - application of a module to perform a specific unit of work
play - sequence of tasks to be applied, in order, to one or more hosts selected from your inventory
playbook - text file containing a list of one or more plays to run in a specific order
role - way of automatically loading certain vars_files, tasks, and handlers based on a known file structure
