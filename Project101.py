import dropbox
import os

class TransferData:
    def __init__(self, access_token):

        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            readFile = f.read()
            dbx.files_upload(readFile, file_to)


def main():
    access_token = 'sl.A8BSl6P6p34J7P7Hf18b-obMDGh5iaUuvhaPzQmh_OJw-AIdqdA9r8nPogNJuRV5mZZtZ9tK4l3wkrD1xO9BlHO4y9qURkKCo97D2NnubdmKzy2LjxGeR8SgkWZys3_Rw1Luwn4'
    transferData = TransferData(access_token)

    file_from = input("type here the path of the file you want to upload ")
    file_to = '/test_dropbox/Test1.png'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()           
