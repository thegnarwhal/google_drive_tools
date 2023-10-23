import argparse
from get_api_services import get_api_services

def count_files_and_folders(drive, folder_id):
    # Function to add recursive count files and folders
    def count_recursive(folder_id):
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents",
            fields='files(id, name, mimeType)'
        ).execute()

        file_count = 0
        folder_count = 0

        for item in results.get('files', []):
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                sub_folder_count, sub_file_count = count_recursive(item['id'])
                folder_count += sub_folder_count + 1  # Counting the current folder
                file_count += sub_file_count
            else:
                file_count += 1

        return folder_count, file_count

    # Start counting from the root folder
    folder_count, file_count = count_recursive(folder_id)

    return file_count, folder_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count files and folders in a Google Drive folder.")
    parser.add_argument("--source_id", required=True, type=str, help="The source Google Drive folder ID")

    args = parser.parse_args()

    # Authenticate with Google Drive API
    drive_service = get_api_services()

    # Get the counts for files and folders in the specified folder
    file_count, folder_count = count_files_and_folders(drive_service, args.source_id)

    print(f"Total number of files: {file_count}")
    print(f"Total number of folders: {folder_count}")
