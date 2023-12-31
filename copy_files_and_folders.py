import argparse
from get_api_services import get_api_services

def copy_files_and_folders(drive, source_folder_id, destination_folder_id):
    # Retrieve the list of files and folders in the source folder
    results = drive.files().list(
        q=f"'{source_folder_id}' in parents",
        fields="files(id, name, mimeType)").execute()

    files = results.get('files', [])

    for file in files:
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            # If it's a folder, create a new folder in the destination and copy its contents recursively
            copied_folder = {'parents': [destination_folder_id], 'name': file['name'], 'mimeType': 'application/vnd.google-apps.folder'}
            copied_folder = drive.files().create(body=copied_folder, fields='id').execute()

            print(f"Created folder '{file['name']}' in destination folder.")

            # Recursively copy the contents of the subfolder(s)
            copy_files_and_folders(drive, file['id'], copied_folder['id'])
        else:
            # If it's a file, copy it to the destination folder
            copied_file = {'parents': [destination_folder_id]}
            drive.files().copy(
                fileId=file['id'], body=copied_file).execute()

            print(f"Copied '{file['name']}' to destination folder.")

def main():
    parser = argparse.ArgumentParser(description="Copy files and folders recursively from a Google Drive folder.")
    parser.add_argument("--source_id", required=True, help="Source folder ID in Google Drive")
    parser.add_argument("--destination_id", required=True, help="Destination folder ID in Google Drive")

    args = parser.parse_args()

    # Authenticate with Google Drive using the provided credentials
    drive_service = get_api_services()

    # Copy the contents of the source folder to the destination folder
    copy_files_and_folders(drive_service, args.source_id, args.destination_id)

if __name__ == "__main__":
    main()
