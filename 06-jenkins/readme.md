# Jenkins

## features

- **open-source automation server**
- **wide range of plugins**

## Freestyle vs Pipeline as a code

- **Freestyle Jobs**:

  - Traditional way
  - Configuration is done through the UI
  - Suitable for simple tasks.

- **Pipeline as Code**:

  - Repeatable
  - Complex workflows and version control.

### How 3rd party software be use

- **we can install them in the os and give their path**
- **we can tell jenkins the version and jenkins will download and use them when the job runs**
- **we can tel jenkins the url to download the software and jenkins download when the job runs**

### Jenkins Pipeline vs. Jobs

Jenkins provides two primary models for defining and managing builds:

1. Jobs (also known as "Freestyle Jobs")
2. Pipelines

## Types of Jenkins Pipelines

### 1. Declarative Pipeline

- Definition: A newer, simpler, and more structured syntax for Jenkins pipelines.
- Syntax: Uses a predefined pipeline {} block.
- Goal: Make pipelines easier to read, write, and maintain.

### 2. Scripted Pipeline

- Definition: Older, more flexible pipeline style written in Groovy code.
- Syntax: Uses node {} blocks and allows full programming logic.
- Goal: Provide full control over pipeline logic.

### jenkins cli

- **Jenkins CLI (Command Line Interface) is a tool that allows you to interact with a Jenkins server from the command line.**

  ```bash
  java -jar jenkins-cli.jar -s http://13.201.95.47:8080 -auth kavindu_gihan:11338a47ede2dc3bcd4b9bd402e48ea1e9 list-jobs
  ```

---

## Triggers in Jenkins

### 1.Source Control Polling in Jenkins

- **Jenkins checks your source code repository at regular intervals to see if there are any changes (new commits, new branches, etc.). If it detects changes, it triggers a build automatically.**

### 2.Webhooks in Jenkins

- **way for external services (like GitHub, GitLab, or Bitbucket) to notify Jenkins automatically when something happens.**
  > Example: You push code to GitHub → GitHub sends a webhook (HTTP POST request) to Jenkins → Jenkins starts a build.
- So instead of Jenkins polling ("check every 5 minutes if repo changed"), the repo pushes an event to Jenkins immediately.
- **👉 This makes builds faster and reduces unnecessary checks.**

### Polling ≠ Webhooks

- Polling: Jenkins repeatedly asks the repo, “Any changes?”
- Webhooks: The repo notifies Jenkins immediately when changes happen. (More efficient, no unnecessary checks.)

### 3.Scheduled Builds in Jenkins

- **Jenkins can be configured to run builds at specific times or intervals.**
- **This is useful for regular tasks like nightly builds or weekly reports.**

### 4.Remote Triggering in Jenkins

- **You can start a Jenkins build remotely using a URL or an API call.**
- **This is useful for integrating Jenkins with other tools or scripts.**

  ```curl -X POST "http://<jenkins-server>:8080/job/<job-name>/build" \
      --user "<username>:<api-token>" \
      -H "Jenkins-Crumb:abcd1234efgh"
  ```

### 5.Build after other projects(Job) are built

- **You can set up a Jenkins job to start building after another job completes.**

---

## Master / Slave Architecture

### Why use Slave (Agent)?

- **Distribute Workload**
- **Different Environments** - Some jobs may require specific OS or software.
- **Isolation**

> 🛑 By default, linux machine do not provide user,password authentication from ssh (so when adding node take this to consideration)

---

## Security in Jenkins

- **Jenkins has a built-in user database for managing users and their permissions.**
- **You can create users, assign roles, and set permissions to control who can do what**

---

## Workspace in Jenkins

- **where the files for a specific job are stored during its execution.**
- **All builds gets of one job share the same workspace unless configured otherwise.**
- **We can clean the workspace before or after the build.**

### mvn `<plugin-prefix>:<goal>`

`mvn checkstyle:checkstyle`

- **plugin-prefix**: Short name for a Maven plugin (e.g., `checkstyle`).
- **goal**: Specific task provided by the plugin (e.g., `checkstyle`).

---

## Basic plugins in Jenkins

- **Git plugin**: Integrates Git with Jenkins.
- **GitHub plugin**: Integrates GitHub with Jenkins.
- **Pipeline plugin**: Enables Jenkins Pipeline as code.
- **Docker plugin**: Allows jenkins to provision agents as docker containers.
- **Docker pipeline plugin**: Run build steps inside Docker within your pipeline.
- **Blue Ocean plugin**: Modern UI for Jenkins Pipelines.
- **Stage View plugin**: Visualize pipeline stages.
