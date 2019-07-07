# https://stackoverflow.com/questions/56568303/i-need-to-write-a-program-to-print-the-following-pattern/56568747#56568747
# --- 13 JUNE 2019 ---
	def print_num_triangle(n=6):
		"""
		1 2 3 4 5 6
		  1 2 3 4 5
		    1 2 3 4
		      1 2 3
		        1 2
		          1
		"""

		pattern = '\n'.join((' ' * 2 * i) + ' '.join(str(n) for n in range(1, num + 1)) for i, num in enumerate(range(n, -1, -1)))
		print(pattern)


	if __name__ == "__main__":
		print_num_triangle(10)

		# 1 2 3 4 5 6 7 8 9 10
		#   1 2 3 4 5 6 7 8 9
		#     1 2 3 4 5 6 7 8
		#       1 2 3 4 5 6 7
		#         1 2 3 4 5 6
		#           1 2 3 4 5
		#             1 2 3 4
		#               1 2 3
		#                 1 2
		#                   1
		#                     

		print_num_triangle(7)
		# 1 2 3 4 5 6 7
		#   1 2 3 4 5 6
		#     1 2 3 4 5
		#       1 2 3 4
		#         1 2 3
		#           1 2
		#             1

		print_num_triangle() # default -> 6
		# 1 2 3 4 5 6
		#   1 2 3 4 5
		#     1 2 3 4
		#       1 2 3
		#         1 2
		#           1