# Continuous Delivery (CD)

## Approve before deploy

- Add a manual approval step before deployment to production.

```groovy
pipeline {
    agent any

    stages {
        stage('stage') {
            steps {
                echo 'staging'
            }
        }

        stage('approve') {
            steps {
                input 'Ready to deply'
            }
        }

        stage('deploy') {
            steps {
                echo 'deploy'
            }
        }
    }
}
```
