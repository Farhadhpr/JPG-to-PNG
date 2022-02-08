import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# to check if new exits, if not creat it

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through entire folder (Pokedex), andd
# we want to convert images to png
# save them to new folder.
for filename in os.listdir(image_folder):
	img = Image.open(f'./{image_folder}{filename}')
	clean_name = os.path.splitext(filename)
	img.save(f'./{output_folder}{clean_name[0]}.png', 'png')
	print('Conversion is done!')	