from PIL import Image
from os import listdir
from os.path import join, isfile


def get_paths_of_dir(path):
    return [join(path, f) for f in listdir(path)
            if isfile(join(path, f))]


all_dirs = get_paths_of_dir("./Plots")

for dir in all_dirs:
  images = get_paths_of_dir("./Plots" + dir)
  
  for img in images:
