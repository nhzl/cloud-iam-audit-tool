import boto3
from modules.utils import save_to_csv

def run_audit():
    iam = boto3.client("iam")
    
    # List IAM users
    users = iam.list_users()["Users"]
    
    audit_results = []
    
    for user in users:
        # List username
        username = user["UserName"]

        # List user arn

        user_arn = user["Arn"]

        # List Creation Date

        user_createdate = user["CreateDate"].strftime("%Y-%m-%d %H:%M:%S")

        # List if has console access
        has_console_access = False
        try:
            iam.get_login_profile(UserName=username)
            has_console_access = True
        except iam.exceptions.NoSuchEntityException:
            has_console_access = False

        # List if has MFA enabled
        mfa_devices = iam.list_mfa_devices(UserName=username)
        has_mfa = len(mfa_devices['MFADevices']) > 0
        
        # List managed policies
        attached_policies = iam.list_attached_user_policies(UserName=username)["AttachedPolicies"]
        attached_policy_names = [p["PolicyName"] for p in attached_policies]

        # List inline policies
        inline_policies = iam.list_user_policies(UserName=username)

        # List Groups
        groups = iam.list_groups_for_user(UserName=username)
        group_names = [group['GroupName'] for group in groups['Groups']]

        
        audit_results.append({
            "Username": username,
            "User ARN": user_arn,
            "User Creation Date": user_createdate,
            "Has console access": has_console_access,
            "Has MFA enabled": has_mfa,
            "AttachedPolicies": ", ".join(attached_policy_names) or "None",
            "InlinePolicies": ", ".join(inline_policies.get("PolicyNames", [])) or "None",
            "Groups": ", ".join(group_names) or "None" 
            



        })
    
    save_to_csv(
        "output/iam_user_audit.csv",
        audit_results,
        headers=[
            "Username",
            "User ARN",
            "User Creation Date",
            "Has console access",
            "Has MFA enabled",
            "AttachedPolicies",
            "InlinePolicies",
            "Groups"
    ]
)