#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:42:42 2023

@author: dale
"""

from pathlib import Path
from datetime import datetime
from helpers.config import settings

class DbConnect:

    DB_NAME = settings.DB_NAME
    DB_URL = settings.SUPA_URL
    DB_USER = settings.USERNAME
    DB_PASSWORD = settings.PASSWORD
    DB_PORT = settings.DB_PORT
    PG_DUMP_PATH = settings.PG_DUMP_PATH
    PREFIX = settings.BACKUP_FILE_PREFIX
    
    _DATE_STR = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    _PROJECT_ROOT = Path(__file__).parent.parent
    SAVE_DIR = Path(_PROJECT_ROOT, 'backups') 
    
    def __init__(self):
        self.SAVE_DIR.mkdir(parents=True, exist_ok=True)
        self.save_path = str(
            Path(
                self.SAVE_DIR,
                f'{self.PREFIX}-{self._DATE_STR}.sql'
            )
        )
        self.command_args = [
            self.PG_DUMP_PATH or 'pg_dump',
            '-h', self.DB_URL,
            '-p', self.DB_PORT,
            '-U', self.DB_USER,
            '-d', self.DB_NAME,
            '-f', self.save_path
        ]
