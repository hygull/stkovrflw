Try this and please comment if this does not satisfy your problem with some additional information.

	date =[];

	response = get('http://www.example.com');

	page_html = BeautifulSoup(response.text, 'html.parser');

	for date in range(2018, 2014, -1):
		result_containers = page_html.find_all('div', id = 'played-' + str(date) +'-data');

		for container in result_containers:
			played_date = result_containers[0].findAll('td', class_ = 'plays');
			for i in played_date:
				date.append(i.text);

	print(data);