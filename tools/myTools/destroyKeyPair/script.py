import argparse, sys, boto3
from botocore.config import Config

parser = argparse.ArgumentParser()
parser.add_argument("--region_name", required=True)
parser.add_argument("--AWS_ACCESS_KEY_ID", required=True)
parser.add_argument("--AWS_SECRET_ACCESS_KEY", required=True)
parser.add_argument("--AWS_SESSION_TOKEN", help="Only required when using temporary credentials.")
parser.add_argument("--KeyName", required=True)
args = parser.parse_args()

print("Getting EC2 client...", file=sys.stderr)
client = boto3.client(
    "ec2",
    config=Config(region_name = args.region_name),
    aws_access_key_id=args.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=args.AWS_SECRET_ACCESS_KEY
)

print("Destroying keypair...", file=sys.stderr)
result = client.delete_key_pair(
    KeyName=args.KeyName
)

print("Returning result...", file=sys.stderr)
print(result)