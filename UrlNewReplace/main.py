
# >>> inp = "https://store.steampowered.com/app/286160/"
# >>>
# >>> inp_url = "https://store.steampowered.com/app/286160/"
# >>> arr = inp_url.split('://')
# >>> arr
# ['https', 'store.steampowered.com/app/286160/']
# >>>
# >>> domain = arr[1].split('.')
# >>> domain
# ['store', 'steampowered', 'com/app/286160/']
# >>>
# >>> sub_url = domain[-1].split('/')[-2]
# >>> sub_url
# '286160'
# >>>
# >>> out_url = 'stream://' + domain[0] + '/' + sub_url + '/'
# >>> out_url
# 'stream://store/286160/'
# >>>

def get_modified_url(inp_url, protocol='stream'):
	arr = inp_url.split('://')[1].split('.')
	sub_url1 = arr[0]
	sub_url2 = arr[-1].split('/')[-2]
	out_url = protocol + '://' + '/'.join([sub_url1, sub_url2])

	return out_url

if __name__ == '__main__':
	# INPUT 1 (Use default protocol as stream)
	url = 'https://store.steampowered.com/app/286160/'
	output = get_modified_url(url)
	print output

	# INPUT 2 (Override default protocol)
	url2 = 'https://store.steampowered.com/app/286160/'
	output2 = get_modified_url(url2, 'new_stream')
	print output2

	# INPUT 3 (Override default protocol)
	url3 = 'https://the_store2.steampowered.com/app/286160/'
	output3 = get_modified_url(url3, 'new_stream')
	print output3