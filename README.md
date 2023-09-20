# Google Drive Tools

Google Drive Tools is a Python CLI tool to build basic reports and perform basic actions against the Google Cloud Platform.

## Installation

### Step 1: Clone This Repository
```bash
git clone https://github.com/thegnarwhal/google_drive_tools.git
```

### Step 2: Install Required Python Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements to run Google Cloud Tools.

```bash
pip install -r requirements.txt
```

### Step 3: Configure Google Service Account
Create a Project and Service Account. Follow:
* [Create Project](https://developers.google.com/workspace/guides/create-project) 
* [Create Service Account](https://developers.google.com/workspace/guides/create-credentials) 

You will need to save the .json output to a new file later on.

Make sure to enable the Google Cloud Resource Manager API for your project.

Grant access to your drive or folders in your drive to your newly created Service Account user, using the `client_email` value from your Service Account's .json file.

## How to Use
Please note: all script files identify a `source_id`. To find your folder's source id:
1. Navigate to the folder in Google Drive.
2. Copy the `source id` found in the URL. This is everything that comes after “folder/” in the URL. For example, if the URL was “https://drive.google.com/drive/folders/1dyUEebJaFnWa3Z4n0BFMVAXQ7mfUH11g”, then the `source_id` would be "1dyUEebJaFnWa3Z4n0BFMVAXQ7mfUH11g”

### count_files_and_folders.py
Finds a count of files and folders any given folder, using the folder's source ID.

```bash
python count_files_and_folders.py --source_id <source ID> --credentials_path <path/to/service.json>
```

### count_files_and_folders_recursive.py
Finds a count of all files and folders that are children of a given source ID.

```bash
python count_files_and_folders_recursive.py --source_id <source ID>  --credentials_path <path/to/service.json>
```

### copy_files_and_folders.py
This script will create folders in the destination directory corresponding to the structure in the source directory and copy all files and subfolders recursively. 

```bash
python copy_files_and_folders.py --source_id <source ID> --destination_id <destination ID>  --credentials_path <path/to/service.json>
```
