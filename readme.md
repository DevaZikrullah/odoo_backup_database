# Odoo Database Backup Script

This script downloads a backup of an Odoo database using specified parameters. It allows you to specify the master password, database name, backup format, URL, and the path to save the backup file.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```
Run 
```sh
python odoo-backup.py --url http://localhost:8069/web/database/backup --master_pwd admin123 --name_db hij --backup_format zip --backup_file_path backup_database.zip
```