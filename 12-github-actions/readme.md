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

### 🛑 In github actions, all jobs run in parallel by default.

## Secrets and environment variables

- **Secrets**: Securely store sensitive information (e.g., API keys, passwords).
- **Environment Variables**: Store non-sensitive configuration data.

### $GITHUB_ENV file

- When a GitHub Actions job runs, the runner (the virtual machine that executes your steps) automatically creates a temporary file — the path of that file is stored in an environment variable called $GITHUB_ENV.

```yaml
steps:
  - name: Set variable
    run: echo "GREETING=Hello" >> $GITHUB_ENV

  - name: Use variable
    run: echo "$GREETING world!"
```
#### 🧱 Why use $GITHUB_ENV instead of export?

- Because each step in a GitHub Action runs in a new shell, so export variables vanish after one step. $GITHUB_ENV is GitHub’s official way to share variables between steps.

## Conditionals

- Use `if` to run steps or jobs based on conditions.
- Common conditions: `success()`, `failure()`, `always()`, `cancelled()`.

  - `success()`: True if all previous steps/jobs succeeded.
  - `failure()`: True if any previous step/job failed.
  - `always()`: Always true, regardless of previous outcomes.
  - `cancelled()`: True if the workflow was cancelled.

## Permissions

- **Default Permissions**: Read/write access to the repository.
- **Custom Permissions**: Fine-tune access for specific jobs or steps.
- Use the `permissions` key in the workflow file to set custom permissions.

- Example:

  ```yaml
  permissions:
    contents: read
  ```

## Variables

1. ${{ }} → GitHub Actions Expression Syntax

- Evaluated by the workflow engine (YAML parser) before the job/step runs.
- Used to reference contexts (like github.sha, secrets, steps._.outputs, vars._, env.\*).

2. $VAR → Shell Variable

- Used inside your script/command (the run: block).
- Standard Bash/Unix variable syntax.
