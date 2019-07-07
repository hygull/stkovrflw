def update_dict(items, d, output_format=1):
	for k, v in d.items():
		if k in items:
			# if output_format == 1:
				k2 = k + "_1"
				count = 0
				while k2 in items:
					count += 1
					k2 += "_1"

				items.update({k2: v})
			# else:
			# 	k2 
		else:
			items.update({k: v})


items = {"A":1,"B":2, "C":3}
u_items = {"D":4, "B":4, "E":8, "C":4}
n_items = {"C":7, "B":9}

# items.update((k + "_1", v) if k in items else (k, v) for k, v in u_items.items())
# keys = items.keys()

update_dict(items, u_items)
print(items)

update_dict(items, n_items)
print(items)
