from modules.aws_audit import run_audit

def main():
    print("Starting AWS IAM audit...")
    run_audit()
    print("Audit complete. Check the output folder for results.")

if __name__ == "__main__":
    main()
