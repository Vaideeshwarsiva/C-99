import os
import shutil
import time

def main():
  deletedFolders = 0
  deletedFiles = 0

  path = input("Enter path to be deleted: ")
  days = 30
  seconds = time.time() - (days * 24 * 60 * 60)

  if os.path.exists(path):
    for root_folder, folders, files in os.walk(path):
      if True:
        removeFolder(path)
        deletedFolders += 1
  
  print(deletedFolders)

def getFileOrFolderAge(path):
  ctime = os.stat(path).st_ctime
  return ctime

def removeFolder(path):
  if not shutil.rmtree(path):
    print(f"{path} is removed successfully!")
  else:
    print("Unable to delete " + path + "!")


main()