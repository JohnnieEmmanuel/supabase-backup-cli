#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:31:59 2023

@author: dale
"""


import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    
    DB_NAME = os.getenv('SUPA_DB_NAME', 'postgres')
    BACKUP_FILE_PREFIX = 'PG_Insights' # Used for the filename
    
    # Variables below must be in a .env file located within same directory
    PG_DUMP_PATH = os.getenv('PG_DUMP_PATH') # Optional: Full path to pg_dump executable
    PASSWORD = os.getenv('SUPA_PASSWORD')
    SUPA_ID = os.getenv('SUPA_ID')
    DB_PORT = os.getenv('SUPA_PORT', '5432')
    USERNAME = os.getenv('SUPA_USER', 'postgres')
    
    # URL below generated from the ID above and shouldn't be changed
    # Unless referencing a direct connection string or pooler different from default
    SUPA_HOST = os.getenv('SUPA_HOST')
    SUPA_URL = SUPA_HOST if SUPA_HOST else f'db.{SUPA_ID}.supabase.co'
    
    
settings = Settings()