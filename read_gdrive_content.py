import io, os
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def download_files_from_folder(folder_name, destination_path, service):
    # Retrieve the folder ID based on the folder name
    folder_id = get_folder_id(folder_name, service)

    # Check if the folder ID is valid
    if folder_id is None:
        print(f"Folder '{folder_name}' not found.")
        return
    
    os.makedirs(destination_path, exist_ok=True)

    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false", pageSize=1000).execute()
    files = results.get('files', [])

    for file in files:
        file_name = file['name']
        file_id = file['id']
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(destination_path, file_name), 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download progress: {0}".format(status.progress() * 100))

        print(f"Downloaded file: {file_name}")

def get_folder_id(folder_name, service):
    results = service.files().list(q="mimeType='application/vnd.google-apps.folder' and trashed=false", pageSize=1000).execute()
    folders = results.get('files', [])

    for folder in folders:
        if folder['name'] == folder_name:
            return folder['id']

    return None

SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

# Authenticate and create the Drive API service
# Make sure you have set up the credentials correctly
CRENDENTIALS = build('drive', 'v3', http=creds.authorize(Http()))

folder_id = '1C33bZ9qDpP03jdTAbfYK6BCSI6GONmGN'
folder_name = 'kreate-share'
destination_path = '/GDrive_data'

# Call the function to download files
download_files_from_folder(folder_name, destination_path, CRENDENTIALS)

files = CRENDENTIALS.files().list().execute().get('files', [])
