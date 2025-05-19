# ☁️ Cloud IAM Audit Tool

A lightweight Python tool to audit AWS IAM users and identify security misconfigurations. This utility helps security engineers, auditors, and cloud practitioners generate a snapshot of IAM posture for detection engineering, compliance, and governance.

---

## 🔍 Features

- Enumerates all IAM users
- Collects:
  - Username & ARN
  - Creation date
  - Console access status
  - MFA status
  - Attached managed policies
  - Inline policies
  - Group memberships
- Exports clean CSV for reporting or ingestion
- Modular and extensible for multi-cloud or deeper role analysis

---

## 📁 Sample Output

| Username | User ARN | MFA Enabled | Console Access | Attached Policies | Inline Policies | Groups |
|----------|----------|-------------|----------------|-------------------|-----------------|--------|
| alice    | arn:aws:iam::123456789012:user/alice | ✅ | ✅ | `SecurityAudit` | `None` | `DevOpsTeam` |

---

## 🧰 Tech Stack

- **Python 3.10+**
- **boto3** – AWS SDK for Python
- **tabulate** – table formatting
- **CSV** – for audit reporting

---

## 🚀 Usage

```bash
# 1. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate      # Windows
source venv/bin/activate     # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure AWS credentials
aws configure                # OR manually set ~/.aws/credentials

# 4. Run the tool
python main.py
```
## 🔐 Required AWS IAM Permissions
The following policy is needed for your audit user:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListUsers",
        "iam:GetLoginProfile",
        "iam:ListMFADevices",
        "iam:ListAttachedUserPolicies",
        "iam:ListUserPolicies",
        "iam:ListGroupsForUser"
      ],
      "Resource": "*"
    }
  ]
}
```
## 🔮 Future Roadmap

- ✅ IAM user audit (initial release)

- 🔁 IAM role trust policy review

- 📉 Identify unused accounts

- 📊 Integration with OpenSearch or Splunk

- ☁️ Azure/GCP IAM audit support

## 👤 Author

Nicholas Hezel
Cloud Security Engineer | Azure, AWS, Terraform | IAM | Incident Response
🔗 [Portfolio](https://github.com/nhzl) | 💼 [LinkedIn](https://www.linkedin.com/in/nicholas-h-793b89220/)
