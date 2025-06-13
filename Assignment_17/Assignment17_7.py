#Schedule a function that perform file backup every hour and writes log_entry into backup_log.txt

import schedule
import time
import shutil
import datetime

def backup_file():

    FirstFile = "important_data.txt"    
    SecondFile = "backup_imp_log.txt" 

    try:
        shutil.copy(FirstFile, SecondFile )
        
        now = datetime.datetime.now()
        log_entry = f"[{str(now)}] Backup completed successfully.\n"
    except Exception as e:
        log_entry = f"[{str(now)}] Backup failed: {str(e)}\n"

    log = open("backup_log.txt", "a")
    log.write(log_entry)

def main():
    schedule.every().hour.do(backup_file)
    print("Backup scheduler started.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

