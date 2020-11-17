# LLNW Storage Sample (Upload Implementation)
# __description__: HTTP-based LLNW Storage Implementation
# __version__: 1.0
# __author__: Sanjeev Pandey

#=====================================================================================#
# HTTP-BASED STORAGE UPLOAD IMPLEMENTATION
# © Limelight's code is Copyright of Limelight Networks
#=====================================================================================#
import requests
import filepath
import os

myusername = 'myusername' # contact account team for creds
mypassword = 'mypassword' # contact account team for creds
full_file_paths = filepath.get_filepaths("Baseball")
auth_headers = { 'X-Agile-Username': myusername, 'X-Agile-Password': mypassword}
url = 'http://your-account-url/account/login' 
r = requests.post(url, headers=auth_headers, verify=False)
token = r.headers['x-agile-token']

for file_to_upload in full_file_paths:
    # filenames are created with '\' in them when using the filepath.py so, we split at '\' when reading the file names
    upload_headers = { 'X-Agile-Authorization': token, 'X-Agile-Basename': file_to_upload.rsplit("\\",1)[1], 'X-Agile-Directory': '/spandey/margalla/hls/Baseball' }
    with open(file_to_upload, 'rb') as filesrc:
        r = requests.post('http://your-account-url/post/raw', data=filesrc, headers=upload_headers)
        print (r.headers)
        print('================================================')
        if r.headers['X-Agile-Status'] == '0':
            print('Upload Successful', 'Uploaded to',r.headers['X-Agile-Path'])
            print('Checksum: ', r.headers['X-Agile-Checksum'])
        else:
            print('upload failed')
