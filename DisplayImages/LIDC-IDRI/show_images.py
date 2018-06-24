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
import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def show_images(image_file_name):
	print("Displaying ", image_file_name)
	img=mpimg.imread(image_file_name)
	imgplot = plt.imshow(img)
	plt.show()

def main():
	files = os.listdir('.');
	for file in files:
		file = file.strip()
		if os.path.isdir(file) and 'LIDC-IDRI-' in file:
			print(file)


if __name__ == "__main__":
	main();

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