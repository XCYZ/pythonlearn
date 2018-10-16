import shutil
import os
src ="../djangolearn"
backup = "bak"
#shutil.copytree(src,backup)
print os.listdir(backup)
shutil.rmtree(backup)
print os.listdir(backup)