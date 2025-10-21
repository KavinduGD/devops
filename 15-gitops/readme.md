# Gitops

- GitOps is a modern DevOps practice that uses Git as the single source of truth for both your application code and your infrastructure/operations configuration.

- In simple terms:
  - 👉 “If it’s not in Git, it doesn’t exist.”
  - 👉 “If you want to change something in the cluster, make a pull request.”

## 🧭 Core Idea of GitOps

With GitOps, you store the desired state of your system (infrastructure + apps) in a Git repository. A GitOps operator (such as Argo CD or Flux) continuously monitors the repo and automatically applies any changes to your cluster or environment.

- That means:
  - No manual kubectl apply in production.
  - No making changes directly on servers.
  - Every change is done via Git commits → reviewed → approved → deployed.

## ⚙️ How GitOps Works (Typical Flow)

1. Developer updates configuration

   - e.g., modifies a Kubernetes Deployment YAML to use a new app version.

2. Commit & Pull Request

   - The change is pushed to the Git repo. CI can run tests or validations.

3. GitOps Operator syncs

   - The operator (e.g., Argo CD) detects the change in Git.

4. Apply to cluster

   - It reconciles the actual cluster state with what’s declared in Git.

5. Continuous reconciliation
   - If someone manually changes something in the cluster, the operator will revert it back to match Git (unless you update Git too).
