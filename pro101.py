import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
     
        dbx = dropbox.Dropbox(self.access_token)
        for (root,dirs,files) in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(),dropbox_path,mode=riteMode('overwrite'))
def main():
    access_token = 'rnicPEKG8WkAAAAAAAAAAZK3FQMLCBd5wp_ipHFs9dz7YDZhX-_pP-0COvxh8rZv'
    transferData = TransferData(access_token)

    file_from = input("enter the name of the file to be uploaded")
    file_to = input("enter the path to upload the file")  # The full path to upload the file to, including the file 
        
    transferData.upload_file(file_from,file_to)
if __name__ == '__main__':
    main()

   