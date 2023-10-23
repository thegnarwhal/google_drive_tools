import os
import argparse
from googleapiclient.discovery import build
from authenticate_drive_api import get_api_services

def count_files_and_folders_recursive(drive_service, folder_id):
    # List files and folders in the specified folder
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents",
        fields='files(id, name, mimeType)'
    ).execute()

    # Initialize counters
    file_count = 0
    folder_count = 0

    # Iterate through the files and folders
    for item in results.get('files', []):
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            folder_count += 1
        else:
            file_count += 1

    return file_count, folder_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count files and folders in a Google Drive folder.")
    parser.add_argument("--source_id", required=True, type=str, help="Google Drive source ID of the folder")

    args = parser.parse_args()

    # Authenticate with Google Drive API
    drive_service = authenticate_drive_api(args.credentials_path)

    # Get the counts for files and folders in the specified folder
    file_count, folder_count = count_files_and_folders_recursive(drive_service, args.source_id)

    print(f"Total number of files: {file_count}")
    print(f"Total number of folders: {folder_count}")