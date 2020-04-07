from __future__ import print_function
import io

from googleapiclient import discovery
from googleapiclient.http import MediaIoBaseDownload

from httplib2 import Http
from oauth2client import file, client, tools
import argparse

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

files = DRIVE.files().list().execute().get('files', [])
for f in files:
    print('id: ',f['id'],'|| name: ', f['name'],'       || mime type:', f['mimeType'])


