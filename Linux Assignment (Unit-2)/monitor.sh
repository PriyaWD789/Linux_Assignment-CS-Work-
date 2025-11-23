#!/bin/bash
#
# Shell Script Development - Assignment Option A
# Purpose: Copies a specified directory to a backup folder with a timestamp.
# Author: Your Name/Student ID
# Date: 2025-11-16
#
# --------------------------------------------------------------------------------

# 1. Define meaningful variables
# The directory to be backed up (Source)
# >>> ACTION REQUIRED: CHANGE THIS PATH to the actual directory you want to back up.
SOURCE_DIR="/home/$USER/Documents/my_project"
# The destination directory where backups will be stored
BACKUP_ROOT="/home/$USER/Backups"
# Generate a timestamp for the backup folder name (Format: YYYY-MM-DD-HHMMSS)
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
# The full path for the new, unique backup directory
BACKUP_DEST="$BACKUP_ROOT/project_backup_$TIMESTAMP"

# 2. Check if the source directory exists
# If the source directory is not found, print an error and exit the script with a non-zero status.
if [ ! -d "$SOURCE_DIR" ]; then
    echo "ERROR: Source directory not found at $SOURCE_DIR"
    exit 1
fi

# 3. Create the root backup directory if it doesn't exist
# The -p flag ensures parent directories are created if necessary.
if [ ! -d "$BACKUP_ROOT" ]; then
    mkdir -p "$BACKUP_ROOT"
    echo "Created backup root directory: $BACKUP_ROOT"
fi

# 4. Perform the recursive copy operation
# cp: copy command
# -r: recursive copy (crucial for directories and their contents)
# -v: verbose output (shows files being copied for confirmation)
echo "Starting backup of $SOURCE_DIR to $BACKUP_DEST..."
cp -rv "$SOURCE_DIR" "$BACKUP_DEST"

# 5. Check if the copy was successful
# $? holds the exit status of the last executed command (0 means success).
if [ $? -eq 0 ]; then
    echo "SUCCESS: Backup completed successfully!"
    echo "Backup location: $BACKUP_DEST"
else
    echo "FAILURE: An error occurred during the copy process. Check permissions."
    exit 1
fi