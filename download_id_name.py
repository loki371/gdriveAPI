from __future__ import print_function
import io

from googleapiclient import discovery
from googleapiclient.http import MediaIoBaseDownload

from httplib2 import Http
from oauth2client import file, client, tools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', action='store', help='File id')
parser.add_argument('--name', action='store', help='File name')
args = parser.parse_args()


# 'https://www.googleapis.com/auth/drive'
# 'https://www.googleapis.com/auth/drive.file'
# 'https://www.googleapis.com/auth/drive.readonly'
# https://www.googleapis.com/auth/drive.metadata.readonly
# https://www.googleapis.com/auth/drive.appdata
# https://www.googleapis.com/auth/drive.metadata
# https://www.googleapis.com/auth/drive.photos.readonly
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


file_id = args.id
filename = args.name
request = DRIVE.files().get_media(fileId=file_id)
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
