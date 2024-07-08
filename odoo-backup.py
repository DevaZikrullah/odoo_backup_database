import requests
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Download Odoo database backup")

# Add arguments
parser.add_argument("--url", type=str, required=True, help="URL for the backup endpoint")
parser.add_argument("--master_pwd", type=str, required=True, help="Master password")
parser.add_argument("--name", type=str, required=True, help="Database name")
parser.add_argument("--backup_format", type=str, choices=['zip', 'dump'], default='zip', help="Backup format (zip or dump)")
parser.add_argument("--backup_file_path", type=str, default='depo_backup.zip', help="Path to save the backup file")

# Parse the arguments
args = parser.parse_args()

form_data = {
    'master_pwd': args.master_pwd,
    'name': args.name,
    'backup_format': args.backup_format
}

response = requests.post(args.url, data=form_data)

if response.status_code == 200:
    with open(args.backup_file_path, 'wb') as f:
        f.write(response.content)
    print(f"Backup file downloaded successfully and saved to {args.backup_file_path}")
else:
    print(f"Failed to download the backup file. Status code: {response.status_code}")
