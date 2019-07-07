**@honar.cs**, based on your problem, 


> Here I want to display all the png and jpg images present inside `LIDC-IDRI-0001`, `LIDC-IDRI-0002`, `LIDC-IDRI-0003`, `LIDC-IDRI-0004` directories.

### File structure &raquo;

	H:\RISHIKESHAGRAWANI\PROJECTS\SOF\DISPLAYIMAGES
	└───LIDC-IDRI
	    │   show_images.md
	    │   show_images.py
	    │   show_images_temp.py
	    │
	    ├───LIDC-IDRI-0001
	    │       download.jpg
	    │       Hacker.jpg
	    │
	    ├───LIDC-IDRI-0002
	    │       images.jpg
	    │
	    ├───LIDC-IDRI-0003
	    │       internet.jpg
	    │       Internet.png
	    │
	    └───LIDC-IDRI-0004
	            RishikeshAgrawani-Hygull-Python.jpg
	            wallpaper-strange-funny-weird-crazy-absurd-awesome-592.jpg
	            waterfalls.jpg


### Requirements &raquo;

* numpy - `pip install numpy`

* matplotlib - `pip install matplotlib`

* Pillow - `pip install Pillow`

### &raquo; Python code (Python 3.6)

> **show_images.py**

	import os
	import json
	import glob
	import numpy as np 
	import matplotlib.image as mpimg
	import matplotlib.pyplot as plt

	image_formats = ["png", "jpg"]; # Let suppose we want to diplay png & jpg images (specify more if you want)

	def show_images(image_file_name):
		print("Displaying ", image_file_name)
		img=mpimg.imread(image_file_name)
		imgplot = plt.imshow(img)
		plt.show()

	def get_image_paths(current_dir):
		files = os.listdir(current_dir);
		paths = []; # To store relative paths of all png and jpg images

		for file in files:
			file = file.strip()
			if os.path.isdir(file) and 'LIDC-IDRI-' in file:
				for image_format in image_formats:
					image_paths = glob.glob(os.path.join(".", file, "*." + image_format))
					if image_paths:
						paths.extend(image_paths);

		return paths
				
	if __name__ == "__main__":
		image_paths = get_image_paths(".");
		print(json.dumps(image_paths, indent=4))

		# Display all images inside image_paths
		for image_path in image_paths:
			show_images(image_path);
			print('\n')

### How to run? 

Open terminal and navigate inside `LIDC-IDRI` directory using `cd` command and run the below command.

`python show_images.py`

### Output on console &raquo;

> Images will be opened one by one (once you close 1st image, 2nd image will be displayed and so on).

	"""
	[
	    ".\\LIDC-IDRI-0001\\download.jpg",
	    ".\\LIDC-IDRI-0001\\Hacker.jpg",
	    ".\\LIDC-IDRI-0002\\images.jpg",
	    ".\\LIDC-IDRI-0003\\Internet.png",
	    ".\\LIDC-IDRI-0003\\internet.jpg",
	    ".\\LIDC-IDRI-0004\\RishikeshAgrawani-Hygull-Python.jpg",
	    ".\\LIDC-IDRI-0004\\wallpaper-strange-funny-weird-crazy-absurd-awesome-592.jpg",
	    ".\\LIDC-IDRI-0004\\waterfalls.jpg"
	]
	"""