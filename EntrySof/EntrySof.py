# \section{Listings Package}
# %
# This tool uses the \textit{listings} package, consequently all the
# standard listings environments are available. You may need to install the
# listings package, see:
# \begin{verbatim}
# ftp://ftp.tex.ac.uk/tex-archive/macros/latex/.../listings/listings.pdf
# \end{verbatim}
# for details.

# Complete MATLAB files can be included in the final documentation if
# desired using the listings package, for example,

# \begin{verbatim}
# \lstinputlisting[caption=test]{Listings/fitLine.m}
# \end{verbatim}
# Code inserted in this manner is not executed by this tool.

# Inline code can be implemented using,
# \begin{verbatim}
# \lstinline{for k=1:n}
# \end{verbatim}
# to generate \lstinline{for k=1:n}

# if __name__ == '__main__':
# n = int(input())
# if n in range(2,11):
#     student_marks = {}
#     for _ in range(n):
#         line = input().split()
#         name = line[0]
#         scores =  line[1:]
#         scores = list(map(float, scores))

#         truth,x,y = 0,0,0
#         y = len(scores)
#         for x in scores:
#             if 0<=x<=100:
#                 truth = truth+1

#         if(truth == y):
#             student_marks[name] = scores
#         else:
#             print("Marks out of range")

#     query_name = input()

#     add = 0
#     m=0
#     for s in student_marks[query_name]:
#         m = m+1
#     if x in student_marks:
#         if x == query_name :
#             for y in student_marks[query_name]:
#                 add = add + y
#             average = float(add/m)
#         else:
#             print("Name doesnt exist.Enter correct name and start again")
#     else:
#          print("The person not ideally linked,since incorrect marks entered,Enter properly and try again")

#     print("%.2f" % average)

import json 

def get_averages():
	student_marks = {};
	successful_trials = 0; # IT IS NOT REQUIRED, JUST TO MAKE PROGRAM USER FRIENDLY

	while True:
		try:
			# CREATE A LIST 
			# ['Rishikesh', '90', '95', '90', '80', '85', '70']
			line = input('\n('+ str(successful_trials + 1) + ') ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> ').split(); 
			if len(line) > 0: 
				# NAME OF STUDENT  => 'Rishikesh'
				name = line[0]; 

				if name.lower() == 'exit': # IF USER ENTERS ANYTHING STARTING WITH exit (stop iteration)
					break

				# SCORES OF A STUDENT (INTEGERS) => [90, 95, 90, 80, 85, 70]
				scores = [int(number) if (int(number) >= 0 and int(number) <= 100) else -1 for number in line[1:]] 
				
				if not scores:
					print("\nERROR: INPUT SHOULD HAVE  AT LEAST 1 OR MORE SCORES (SPACE SEPARATED)")
					continue	
			else:
				print("\nERROR: INPUT SHOULD HAVE NAME FOLLOWED BY AT LEAST 1 OR MORE SCORES (SPACE SEPARATED)")
				continue

			if -1 not in scores: # SCORES ARE IN RANGE MEANS IT IS NOT LIKE [90, -1, 90, -1, 85, 70]
				student_marks[name] = {
					"scores": scores,
					"average": sum(scores) / len(scores) # AVERAGE
				}
			else:
				print("\nERROR: ENTERED SCORES ARE NOT IN RANGE")
				continue	

			successful_trials += 1; # IF EVERYTHING PASSED
		except Exception as error:
			print('\nERROR OCCURED: ', error)
			print("\nPLEASE ENTER CORRECT VALUE")
			continue

	return student_marks; # DICTIONARY OF DICTIONARIES

if __name__ == "__main__":
	# CALL TO get_averages()
	student_marks = get_averages();

	# PRETTY PRINTING DICTIONARY USING json MODULE
	print(json.dumps(student_marks, indent=4));

"""
(py3.6) H:\RishikeshAgrawani\Projects\Sof\EntrySof>python EntrySof.py

(1) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student1 56 67 35 45

(2) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> Mahantesh 67 45  35 24

(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student3 101 56

ERROR: ENTERED SCORES ARE NOT IN RANGE

(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student3 100 0 90

(4) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student4 ok new

ERROR OCCURED:  invalid literal for int() with base 10: 'ok'

PLEASE ENTER CORRECT VALUE

(4) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> Rishikesh 70 40 50 70

(5) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> exit
{
    "student1": {
        "scores": [
            56,
            67,
            35,
            45
        ],
        "average": 50.75
    },
    "Mahantesh": {
        "scores": [
            67,
            45,
            35,
            24
        ],
        "average": 42.75
    },
    "student3": {
        "scores": [
            100,
            0,
            90
        ],
        "average": 63.333333333333336
    },
    "student4": {
        "Rishikesh": [
            70,
            40,
            50,
            70
        ],
        "average": 57.5
    }
}
"""

# print(calculate_average())
# \section{Listings Package}
# %
# This tool uses the \textit{listings} package, consequently all the
# standard listings environments are available. You may need to install the
# listings package, see:
# \begin{verbatim}
# ftp://ftp.tex.ac.uk/tex-archive/macros/latex/.../listings/listings.pdf
# \end{verbatim}
# for details.

# Complete MATLAB files can be included in the final documentation if
# desired using the listings package, for example,

# \begin{verbatim}
# \lstinputlisting[caption=test]{Listings/fitLine.m}
# \end{verbatim}
# Code inserted in this manner is not executed by this tool.

# Inline code can be implemented using,
# \begin{verbatim}
# \lstinline{for k=1:n}
# \end{verbatim}
# to generate \lstinline{for k=1:n}
