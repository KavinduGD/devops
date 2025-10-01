# Github actions

## Why Github actions?

- **Native integration**: Github actions are built into Github
- **Cost-effective**: Generous free tier
- **Marketplace**: A wide range of pre-built actions
- **Scalable runners**: Linux, Windows, and macOS runners

## Core blocks

- **Workflow**: Pipeline definition file
- **Job**: A set of steps executed on the same runner
- **Step**: A single task in a job
- **Runner**: The server that runs the jobs
- **Event**: Triggers that start workflows

### Runners

- **Runners are Virtual Machines (VMs), not containers.**
- GitHub-hosted runners are virtual machines running in Azure.
- Each job runs on a brand new VM that gets destroyed afterward.
- This ensures isolation: jobs don’t interfere with each other.

### In github actions, all jobs run in parallel by default.
