import os


def showtree(folderpath, indent=0):
    try:
        items = os.listdir(folderpath)

    except PermissionError:
        return

    folders = []
    files = []

    for item in items:
        fullpath = os.path.join(folderpath, item)

        if os.path.isfile(fullpath):
            files.append(item)
        else:
            folders.append(item)

        folders.sort(key=lambda x: x.lower())
        files.sort(key=lambda x: x.lower())

    for folder in folders:
        print(" "*indent + "📁"+folder)
        showtree(os.path.join(folderpath, folder), indent + 4)
    for file in files:
        print(" " * indent + "📄 " + file)


base_path = "/Users/chiragpatil/Downloads"
showtree(base_path)
