"""
%
\documentclass[12pt]{article}

\title{Merging a \LaTeX \, and an m-File to\\ Generate Professional Documentation\\
\textbf{merge2latex}\\ Version 1.0}

\author{Matthew Harker and Paul O'Leary\\
Institute for Automation\\
University of Leoben\\
A-8700 Leoben,
Austria\\
URL: automation.unileoben.ac.at\\
"""

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

"""
\\
Original: January 9, 2013\\
$\copyright$ 2013\\
\\
Last Modified: \today}

%-----------------------------------------------------------------
% Pre defined definitions section of the file
%
% (c) Paul O'Leary 2013
%
% This portion is automatically added to the file
\date{}
%
%
"""