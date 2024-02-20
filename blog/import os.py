import os
root_dir = "https://oldie.veriftools.ru/media/generator_item/c7786994b948869f3881dbb72c4b884b"
print("aaa")
for subdir, dirs, files in os.walk(root_dir):
    dirs[:] = (name for name in dirs if name.endswith('normal'))
    