import zipfile

def listZipFile():
    with zipfile.ZipFile('./test.zip', 'r') as zipInfo:
        print([name for name in zipInfo.namelist() if not '/'in name])

if __name__ == "__main__":
    listZipFile()
