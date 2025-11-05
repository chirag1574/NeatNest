import os

folder_pa = "/Users/chiragpatil/Downloads"
all_items = os.listdir(folder_pa)


files = []
folders = []
for item in all_items:
    fupath = os.path.join(folder_pa, item)
    # print(f"Checking: {fupath}")
    # print("isfile:", os.path.isfile(fupath), "isdir:", os.path.isdir(fupath))
    if os.path.isfile(fupath):
        files.append(item)
    if os.path.isdir(fupath):
        folders.append(item)

subfile = []
subfolder = []

for items in folders:
    fupath2 = os.path.join(folder_pa, items)
    inside = os.listdir(fupath2)

    for i in inside:
        full_subpath = os.path.join(fupath2, i)
        if os.path.isfile(full_subpath):
            subfile.append(full_subpath)
        if os.path.isdir(full_subpath):
            subfolder.append(full_subpath)


file_path = "/Users/chiragpatil/Downloads/sample.txt"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("File-contents:", content)
# print(files)
# print(folders)
