# Google Drive File Downloader

This project provides Python code for downloading files from Google Drive using the Google Drive API. It also includes instructions on how to authenticate with the API.
There are various way one can acces the file, you can just download the file or write its content in a txt file (not so clean though).

## Prerequisites

- Python 3.x
- Google Drive API credentials (OAuth 2.0 client ID)

## Installation

1. Clone the repository or download the source code files.

2. Install the required Python packages by running the following command:

   cmd:
   pip install -r requirements.txt
3. Now for Google Drive API refer to this site :-

      https://codelabs.developers.google.com/codelabs/gsuite-apis-intro/#5

4. For "gdown_downloader.py" file simply type this in your terminal or command line:

  python gdown_downloader.py https://drive.google.com/drive/u0/id=   (path to your google drive file, you want to download)

## Authenticating with Google Drive API
1. Go to the Google Cloud Console.
2. Create a new project or select an existing project.
3. Enable the Google Drive API for the project.
4. Create OAuth 2.0 credentials:  
  -Go to the "Credentials" page.
  -Click on "Create Credentials" and select "OAuth client ID".
  -Configure the OAuth consent screen with the required information.
  -Select "Desktop app" as the application type.
  -Download the credentials JSON file.
  
5. Rename the downloaded credentials JSON file to client_secret.json.
6. Move the client_secret.json file to the root folder of this project.
7. Run the file and complete the authentication to gain storage.json file, which will help you to access gdrive easily onwards 

## Downloading Files from Google Drive
To download a file from Google Drive, follow these steps:
1. Obtain the name of the folder from which you want to download file from Google Drive.
2. Change the variable "folder_name" value with yours folder name ( make sure the folder is in your drive)
3. Run the file "download.py"
   
#### That's it! The file will be downloaded and saved to your local machine.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request

##License
This project is licensed under the MIT License.
