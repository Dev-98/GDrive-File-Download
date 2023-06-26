import gdown
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.discovery import build


def download_files_from_folder(folder_name, service):
    # Retrieve the folder ID based on the folder name
    folder_id = get_folder_id(folder_name, service)

    # Check if the folder ID is valid
    if folder_id is None:
        print(f"Folder '{folder_name}' not found.")
        return
    
    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false", pageSize=1000).execute()
    files = results.get('files', [])

    for file in files:
        file_name = file['name']
        file_id = file['id']
        prefix = 'https://drive.google.com/uc?/export=download&id='

        gdown.download(prefix+file_id)

        print(f"Downloaded file: {file_id} , file name = {file_name}")

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
# destination_path = '/GDrive_data'

# Call the function to download files
download_files_from_folder(folder_name, CRENDENTIALS)
