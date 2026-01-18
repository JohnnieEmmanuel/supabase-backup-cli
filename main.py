# -*- coding: utf-8 -*-


import sys
import os
import subprocess
from pathlib import Path

try:
    import dotenv
except ImportError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "python-dotenv"]
    )

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from helpers.session import DbConnect


class SupaDbBackup(DbConnect):
    
    def __init__(self):
        super().__init__()
        
        # Prepare environment with PGPASSWORD
        env = dict(os.environ)
        if self.DB_PASSWORD:
            env["PGPASSWORD"] = self.DB_PASSWORD
            
        print(f"Starting backup to {self.save_path}...")
        try:
            subprocess.run(
                self.command_args, 
                env=env,
                check=True,
                capture_output=True,
                text=True
            )
            print("Backup successful!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while backing up the database:\n{e.stderr}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
    
    
if __name__ == "__main__":
    backup_obj = SupaDbBackup()
