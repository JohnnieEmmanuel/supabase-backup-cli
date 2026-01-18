
---

# Supabase Free DB Backup Utility

Supabase Free DB Backup Utility is a lightweight open source Python tool for backing up your Supabase PostgreSQL database using pg_dump. It is designed for developers and teams running on the Supabase free tier who want a simple and reliable way to export their data without paying for additional backup features.

This tool connects using your own Supabase database credentials and creates timestamped SQL backup files that you can store locally or move to external storage.

---

## Features

* Works on the Supabase free plan
* Uses PostgreSQL native pg_dump
* Secure credential based connection
* Generates timestamped SQL backups
* Simple script based setup
* Fully open source

---

## Requirements

* Python 3.6 or higher
* PostgreSQL 15 or higher
* pg_dump installed on your system
* Supabase database credentials
* A .env file for configuration

---

## Project Setup

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/supabase-free-backup.git
   ```

2. Navigate into the project directory

   ```bash
   cd supabase-free-backup
   ```

3. Create a .env file in the same directory as config.py

---

## Environment Variables

Create a `.env` file with the following contents:

```env
SUPA_ID=""
SUPA_DB_NAME="postgres"
SUPA_PORT="5432"
SUPA_USER="postgres.<SUPA_ID>"
SUPA_PASSWORD=""
SUPA_HOST="aws-1-us-east-1.pooler.supabase.com"

# Optional. Only required if pg_dump is not in your system PATH
PG_DUMP_PATH="C:\\Program Files\\PostgreSQL\\18\\bin\\pg_dump.exe"
```

### Variable Explanation

* SUPA_ID
  Your Supabase project reference ID.

* SUPA_DB_NAME
  Database name. Defaults to postgres for most Supabase projects.

* SUPA_PORT
  Database port. Usually 5432.

* SUPA_USER
  Database username in the format:

  ```
  postgres.<SUPA_ID>
  ```

* SUPA_PASSWORD
  Your Supabase database password.

* SUPA_HOST
  Supabase connection pooler host.

* PG_DUMP_PATH
  Optional full path to pg_dump. Mostly required on Windows if pg_dump is not in PATH.

---

## Usage

Run the backup script from the project root:

```bash
python main.py
```

The script will connect to your Supabase database and create a SQL dump file in the `backups` directory.

### Backup File Naming

Backup files are named using the format:

```
DB_NAME-YYYY-MM-DD_HH-MM-SS.sql
```

Example:

```
postgres-2026-01-18_14-32-10.sql
```

---

## Important Notes

* The DB name used in the backup filename is taken from SUPA_DB_NAME.
* Ensure pg_dump is the same or newer version than your Supabase PostgreSQL version.
* Minimal error handling is implemented. Any errors during execution will be printed to the console.
* This tool does not modify your database. It only performs read operations.

---

## Security

Do not commit your `.env` file to GitHub.

Add this to your `.gitignore` file:

```gitignore
.env
```

---

## Why This Tool Exists

Database backups should not be locked behind a paywall.

This utility gives developers full control over their Supabase data while staying on the free plan and avoiding vendor lock in.

---

## License

MIT License

---

