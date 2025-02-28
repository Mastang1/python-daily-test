import zipfile

def listZipFile():
    with zipfile.ZipFile('./test.zip', 'r') as zipInfo:
        # print([name for name in zipInfo.namelist() if not '/'in name])
        print(zipInfo.namelist())

if __name__ == "__main__":
    listZipFile()
