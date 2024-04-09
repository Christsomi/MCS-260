import os
import os.path
def filesearch(path, filename):
  if (os.path.isfile(filename) == True):
    return True
  L = os.listdir()
  folders = []
  for s in L:
    if(os.path.isdir(s) == True):
      folders.append(s)
    if len(folders) == 0:
      return False
    for f in folders:
      if (filesearch(f, filename)) == True:
        return True
    return False

