import sys, traceback
import json
# temp = sys.stdout;
# sys.stdout = open("Errors.txt", "w")

def func3(a, b, c):
	a/0

# disp(['First command => ', 'latex -interaction=nonstopmode', latexFileName{:}]);
# system(['latex -interaction=nonstopmode ', latexFileName{:}]);

# disp(['Second command (3 times) => ', 'bibtex', basename{:}]);
# system(['bibtex ', basename{:}]);
# system(['bibtex ', basename{:}]);
# system(['bibtex ', basename{:}]);

# disp(['Third command => ', 'latex -interaction=nonstopmode ', latexFileName{:}]);
# system(['latex -interaction=nonstopmode ', latexFileName{:}]);

# disp(['Fourth command => dvips -R2 -Ppdf -o ', basename{:}, '.ps', ' ', basename{:}, '.dvi']);
# system(['dvips -R2 -Ppdf -o ', basename{:}, '.ps', ' ', basename{:}, '.dvi']);

# disp(['Fifth command => ', 'ps2pdf14', basename{:}, '.ps']);
# system(['ps2pdf14 ', basename{:}, '.ps']);
def func2(a, b, c):
	func3(a, b, c)



# disp(['First command => ', 'latex -interaction=nonstopmode', latexFileName{:}]);
# system(['latex -interaction=nonstopmode ', latexFileName{:}]);

# disp(['Second command (3 times) => ', 'bibtex', basename{:}]);
# system(['bibtex ', basename{:}]);
# system(['bibtex ', basename{:}]);
# system(['bibtex ', basename{:}]);

# disp(['Third command => ', 'latex -interaction=nonstopmode ', latexFileName{:}]);
# system(['latex -interaction=nonstopmode ', latexFileName{:}]);

# disp(['Fourth command => dvips -R2 -Ppdf -o ', basename{:}, '.ps', ' ', basename{:}, '.dvi']);
# system(['dvips -R2 -Ppdf -o ', basename{:}, '.ps', ' ', basename{:}, '.dvi']);

# disp(['Fifth command => ', 'ps2pdf14', basename{:}, '.ps']);
# system(['ps2pdf14 ', basename{:}, '.ps']);




def func1(a, b, c):
	func2(a, b, c)








if __name__ == "__main__":
	try:
		func1(12, 67, 89)
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		print("*** print_tb:")
		traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
		print("\n\n")
		print("*** print_exception:")
		# exc_type below is ignored on 3.5 and later
		traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stdout) # limit = 2

		print('\n\n')
		print("*** format_exception:")
		# exc_type below is ignored on 3.5 and later
		exception_messages = traceback.format_exception(exc_type, exc_value,
                                          exc_traceback)

		print(type(exception_messages))
		for exception_message in exception_messages:
			print(exception_message)
			print("---------------------------------------------------------------")


