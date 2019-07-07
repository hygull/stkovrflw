> https://stackoverflow.com/questions/1128693/how-do-i-use-a-decimal-number-in-a-django-url-pattern/50199091#50199091

## Don't use 

	url(r"^item/value/(?P<dollar>\d+\.\d{1,2})$", views.show_item, name="show-item"),

> It will only match the **URL patterns** like `/item/value/0.01`, `/item/value/12.2` etc.

> It won't match **URLs** like `/item/value/1.223`, `/item/value/1.2679` etc.

## Better is to use

	url(r"^item/value/(?P<dollar>\d+\.\d+)$", views.show_item, name="show-item"),

> It will match **URL patterns** like  `/item/value/0.01`, `/item/value/1.22`,  `/item/value/10.223` etc.

	# Make sure you have defined Item model (this is just an example)
	# You use your own model name
	from .models import Item 

	def show_item(request, dollar):
		try:
			# Convert dollar(string) to dollar(float).
			# Which gets passed to show_item() if someone requests 
			# URL patterns like /item/value/0.01, /item/value/1.22 etc.
			dollar = float(dollar);

			# Fetch item from Database using its dollar value
			# You may use your own strategy (it's mine)
			item = Item.objects.get(dollar=dollar);

			# Make sure you have show_item.html.
			# Pass item to show_item.html (Django pawered page) so that it could be 
			# easily rendered using DTL (Django template language).
			return render(request, "show_item.html", {"item": item});
		except:
			# Make sure you have error.html page (In case if there's an error)
			return render(request, "error.html", {});