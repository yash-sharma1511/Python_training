import datetime
import os

os.makedirs("backups", exist_ok=True)

date_str = datetime.datetime.now().strftime("%Y-%m-%d")
backup_file = f"backups/data_backup_{date_str}.csv"

with open("data.csv", 'r') as file, open(backup_file, 'w') as backfile:
    for line in file:
        backfile.write(line)