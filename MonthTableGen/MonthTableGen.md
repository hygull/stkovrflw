**@Blooper**, I've written the below code in which the function **show_formatted_calendar()** that takes 5 parameters. 

First 2 are required parameters & last 3 are optional parameters that you can pass if you want to change the look of your table.

In the code, I've called the **show_formatted_calendar()** 3 times. 

> **show_formatted_calendar()** returns a formatted calendar string that you can print on console, save in file or store in variable for reuse.

If you run it, it will ask you to enter the values of first 2 required parameters and uses default values for last 3 parameters (in first call).

In 2nd and 3rd calls, it overrides the default values of the function parameters to  change the look of table that you can see in the output provided at the bottom.

Please have a look at the below code. 

	def show_formatted_calendar(no_of_days, sun_starts_from, spaces=1, fill_char='-', corner_char='+'):
		days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
		blank_fields = 0; # Blank fields in first row(may vary in range [1, 6])

		if not(no_of_days >= 28 and no_of_days <= 31):
			print 'Input Error: Number of days should be in interval [28, 31].';
			return;

		if not(sun_starts_from >= 1 and sun_starts_from <= 7):
			print 'Input Error: Sunday should be inin interval [1, 7].'
			return;
		
		string = fill_char*spaces; # -
		decorator_line = string + 3 * fill_char + string; # -----
		separator_line = (corner_char + decorator_line) * 7 + corner_char; # +-----+-----+-----+-----+-----+-----+-----+
		
		# First line
		formatted_calendar = separator_line + '\n'; 

		# Second line
		line_spaces = ' ' * spaces;
		days_string = "|" + line_spaces + (line_spaces + '|' + line_spaces).join(days) + line_spaces + '|';
		formatted_calendar += days_string + '\n';

		# Third line
		formatted_calendar += separator_line + '\n';

		# Fourth line (No of possible blank fields at the begining)
		blank_fields = (8 - sun_starts_from) % 7; # 1=>0, 2=>6, 3=>5, 4=>4, 5=>5, 6=>2
		blank_string  = (('|' + line_spaces) + (3 * ' ') + line_spaces) * blank_fields;
		date_string = '';

		i = blank_fields + 1;
		day = 1;
		while day <= no_of_days:
			date_string += '|' + line_spaces + '%-3s' % (day) + line_spaces;

			if i % 7 == 0:
				date_string += '|\n';

			i += 1;
			day += 1;

		# No of possible blank fields in last line 
		last_blank_fields = 7 - ((no_of_days - (7 - blank_fields)) % 7); 
		last_blank_string = ('|' + line_spaces + 3 * ' ' + line_spaces) * last_blank_fields + '|';

		formatted_calendar += (blank_string + date_string) + last_blank_string + '\n';
		formatted_calendar += separator_line + '\n'; 

		return	formatted_calendar;

	# Starts here
	if __name__ == "__main__":
		try:
			no_of_days = int(raw_input('Enter number of days of month(>=28 & <=31) : ').strip());
			sun_starts_from = int(raw_input('Sunday starts from which date(>=1 & <=7)   : ').strip());

			# First call
			formatted_calendar = show_formatted_calendar(no_of_days, sun_starts_from);
			print formatted_calendar;

			# Second call (static input)
			print "\nFor Days 31 days where sunday starts from 4:-\n"
			formatted_calendar = show_formatted_calendar(31, 4, 2, '*', '.');
			print formatted_calendar;

			# Third call (static input)
			print "\nFor Days 29 days where sunday starts from 2:-\n"
			formatted_calendar = show_formatted_calendar(29, 2, 3, '~');
			print formatted_calendar;
		except Exception as error:
				print 'Error occurred. ', error;


Output &raquo;

	H:\RishikeshAgrawani\Projects\Sof\MonthTableGen>python MonthTableGen.py
	Enter number of days of month(>=28 & <=31) : 31
	Sunday starts from which date(>=1 & <=7)   : 6
	+-----+-----+-----+-----+-----+-----+-----+
	| SUN | MON | TUE | WED | THU | FRI | SAT |
	+-----+-----+-----+-----+-----+-----+-----+
	|     |     | 1   | 2   | 3   | 4   | 5   |
	| 6   | 7   | 8   | 9   | 10  | 11  | 12  |
	| 13  | 14  | 15  | 16  | 17  | 18  | 19  |
	| 20  | 21  | 22  | 23  | 24  | 25  | 26  |
	| 27  | 28  | 29  | 30  | 31  |     |     |
	+-----+-----+-----+-----+-----+-----+-----+


	For Days 30 days where sunday starts from 4:-

	.*******.*******.*******.*******.*******.*******.*******.
	|  SUN  |  MON  |  TUE  |  WED  |  THU  |  FRI  |  SAT  |
	.*******.*******.*******.*******.*******.*******.*******.
	|       |       |       |       |  1    |  2    |  3    |
	|  4    |  5    |  6    |  7    |  8    |  9    |  10   |
	|  11   |  12   |  13   |  14   |  15   |  16   |  17   |
	|  18   |  19   |  20   |  21   |  22   |  23   |  24   |
	|  25   |  26   |  27   |  28   |  29   |  30   |  31   |
	|       |       |       |       |       |       |       |
	.*******.*******.*******.*******.*******.*******.*******.


	For Days 29 days where sunday starts from 2:-

	+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+
	|   SUN   |   MON   |   TUE   |   WED   |   THU   |   FRI   |   SAT   |
	+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+
	|         |         |         |         |         |         |   1     |
	|   2     |   3     |   4     |   5     |   6     |   7     |   8     |
	|   9     |   10    |   11    |   12    |   13    |   14    |   15    |
	|   16    |   17    |   18    |   19    |   20    |   21    |   22    |
	|   23    |   24    |   25    |   26    |   27    |   28    |   29    |
	|         |         |         |         |         |         |         |
	+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+~~~~~~~~~+




