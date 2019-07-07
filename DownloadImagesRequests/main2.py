import requests
from PIL import Image
from StringIO import StringIO

r = requests.get('http://server.com/1.jpg')
r.content
i = Image.open(StringIO(r.content))