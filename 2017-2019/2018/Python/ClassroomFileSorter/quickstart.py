from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

GDOC = "application/vnd.google-apps.document"
GSHEET = "application/vnd.google-apps.spreadsheet"
GFOLDER = "application/vnd.google-apps.folder"
GFORM = "application/vnd.google-apps.form"


def get_folder_id(parent, foldername):
    print(f"SEARCHING FOR {foldername}...")
    folders_list={}
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            folders_list.append(f)
    return folders_list

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)



folder_classroom = get_folder_id('root', "Classroom")