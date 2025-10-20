# Kubenetes

## Setup k8 cluster using kops

Kops is a tool that helps you create, destroy, upgrade and maintain production-grade, highly available, Kubernetes clusters from the command line.

### Prerequisites

- AWS CLI installed and configured
- kubectl installed
- kops installed
- An S3 bucket to store the cluster state
- A domain name for the cluster
- SSH key pair for accessing the nodes
- IAM user with necessary permissions
- Route53 hosted zone for the domain

### Steps to create a k8 cluster using kops

1. Create an S3 bucket to store the cluster state
2. Create a Route53 hosted zone for your domain
3. Create a kops cluster configuration file
4. Create the cluster using kops
5. Validate the cluster

#### create cluster setup

```bash
kops create cluster --name=experts247.online --state=s3://kopk8tkg --zones=ap-south-1a,ap-south-1b --node-count=2 --node-size=t2.large --control-plane-size=t2.large --dns-zone=experts247.online --node-volume-size=20 --control-plane-volume-size=20 --ssh-public-key ~/.ssh/id_ed25519.pub
```

#### create cluster

```bash
kops update cluster --name=experts247.online --state=s3://kopk8tkg --yes --admin
```

#### validate cluster

```bash
kops validate cluster --name=experts247.online --state=s3://kopk8tkg
```

#### delete cluster

```bash
kops delete cluster --name=experts247.online --state=s3://kopk8tkg --yes
```

## ✅ Cluster Validation: `experts247.online`

### 🧩 Instance Groups

| **Name**                  | **Role**     | **Machine Type** | **Min** | **Max** | **Subnets** |
| ------------------------- | ------------ | ---------------- | ------- | ------- | ----------- |
| control-plane-ap-south-1a | ControlPlane | t2.large         | 1       | 1       | ap-south-1a |
| nodes-ap-south-1a         | Node         | t2.large         | 1       | 1       | ap-south-1a |
| nodes-ap-south-1b         | Node         | t2.large         | 1       | 1       | ap-south-1b |

---

### 🖥️ Node Status

| **Name**            | **Role**      | **Ready** |
| ------------------- | ------------- | --------- |
| i-052cbab3f45ec8ab4 | node          | ✅ True   |
| i-09e8fe2a5ff6aba0c | node          | ✅ True   |
| i-0b39fea10d042936e | control-plane | ✅ True   |

---

### 🚀 Cluster Status

✅ **Your cluster `experts247.online` is ready.**
