Make sure, you have installed **Perl** and **MikTeX** (for `latexmk` and `pdflatex` compilers support) in your system.

If not, you can download **Perl** from [https://www.perl.org/get.html](https://www.perl.org/get.html)

and **MikTeX** from [https://miktex.org/download](https://miktex.org/download).

Also do not forget to check [http://mg.readthedocs.io/latexmk.html#installation](http://mg.readthedocs.io/latexmk.html#installation) as it guides nicely about Latex compilers.

I have `document.tex` with following content.


	\documentclass{article}%
	\usepackage[T1]{fontenc}%
	\usepackage[utf8]{inputenc}%
	\usepackage{lmodern}%
	\usepackage{textcomp}%
	\usepackage{lastpage}%
	%
	%
	%
	\begin{document}%
	\normalsize%
	\section{A section}%
	\label{sec:A section}%
	Some regular text and some %
	\textit{italic text. }%
	\subsection{A subsection}%
	\label{subsec:A subsection}%
	Also some crazy characters: \$\&\#\{\}

	%
	\end{document}


Finally create any python file and paste any one of the below code and run.

### 1ST WAY

	# 1st way
	import os

	tex_file_name = "document.tex";
	os.system("latexmk " + tex_file_name + " -pdf");

### 2ND WAY

	# 2nd way
	import os

	tex_file_name = "document.tex";
	os.system("pdflatex " + tex_file_name);

For compiling complex latex files, you need to look for extra options passed with `latexmk` or `pdflatex` commands.

Thanks.
