**@Mahantesh**, as I read and understood from your code, I've tried to implement your problem in my way. I have taken varible names same as you've taken. 

> I've also used `json` module for pretty printing the dictionary.

Please check the below code and let me know if you need any changes.

> Don't forget to check the output.

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

### &raquo; Output1

	(py3.6) H:\RishikeshAgrawani\Projects\Sof\EntrySof>python EntrySof.py

	(1) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student1 56 67 35 45

	(2) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student2 67 45  35 24

	(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student3 101 56

	ERROR: ENTERED SCORES ARE NOT IN RANGE

	(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student3 100 0 90

	(4) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student4 ok new

	ERROR OCCURED:  invalid literal for int() with base 10: 'ok'

	PLEASE ENTER CORRECT VALUE

	(4) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> student4 70 40 50 70

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
	    "student2": {
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
	        "scores": [
	            70,
	            40,
	            50,
	            70
	        ],
	        "average": 57.5
	    }
	}

### &raquo; Output2

	(py3.6) H:\RishikeshAgrawani\Projects\Sof\EntrySof>python EntrySof.py

	(1) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> hygull 50 60 70

	(2) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> gurudev 78 22 50 55 45

	(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> user1 60 -5 9

	ERROR: ENTERED SCORES ARE NOT IN RANGE

	(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> user2 100 40 kite

	ERROR OCCURED:  invalid literal for int() with base 10: 'kite'

	PLEASE ENTER CORRECT VALUE

	(3) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> user3 90 90 100 50

	(4) ENTER NAME SEPARATED BY 1 OR MORE SCORES SPACE SEPARATED (TYPE exit TO STOP) >>> exit
	{
	    "hygull": {
	        "scores": [
	            50,
	            60,
	            70
	        ],
	        "average": 60.0
	    },
	    "gurudev": {
	        "scores": [
	            78,
	            22,
	            50,
	            55,
	            45
	        ],
	        "average": 50.0
	    },
	    "user3": {
	        "scores": [
	            90,
	            90,
	            100,
	            50
	        ],
	        "average": 82.5
	    }
	}
