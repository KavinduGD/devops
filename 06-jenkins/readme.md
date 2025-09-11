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

### Source Control Polling in Jenkins

- **Jenkins checks your source code repository at regular intervals to see if there are any changes (new commits, new branches, etc.). If it detects changes, it triggers a build automatically.**

### Webhooks in Jenkins

- **way for external services (like GitHub, GitLab, or Bitbucket) to notify Jenkins automatically when something happens.**
  > Example: You push code to GitHub → GitHub sends a webhook (HTTP POST request) to Jenkins → Jenkins starts a build.
- So instead of Jenkins polling ("check every 5 minutes if repo changed"), the repo pushes an event to Jenkins immediately.
- **👉 This makes builds faster and reduces unnecessary checks.**

### Polling ≠ Webhooks

- Polling: Jenkins repeatedly asks the repo, “Any changes?”
- Webhooks: The repo notifies Jenkins immediately when changes happen. (More efficient, no unnecessary checks.)

### mvn `<plugin-prefix>:<goal>`

`mvn checkstyle:checkstyle`

- **plugin-prefix**: Short name for a Maven plugin (e.g., `checkstyle`).
- **goal**: Specific task provided by the plugin (e.g., `checkstyle`).

### SonarQube Integration with Jenkins

- **We use sonar scanner to scan the code and send the report to sonarqube server**
- **Also we can use sonarqube plugin in jenkins to do the same task**
- **After scanning we can see the report in sonarqube server**

#### Sonarqube Quality Gates

- **Quality Gates are a set of conditions that your code must meet to be considered acceptable.**
- **sonarqube use web hooks to notify jenkins about the quality gate status**

  > `http://<jenkins-url>/sonarqube-webhook/ `
