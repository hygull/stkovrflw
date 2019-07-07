```bash
H:\RishikeshAgrawani\Projects\Sof\BitFields>pip install bitstruct
Collecting bitstruct
  Downloading https://files.pythonhosted.org/packages/f1/20/ce0e9cbfe93614f18b5cd760a092b068abf552d27d9e3bfe50c9c3ad4deb/bitstruct-3.9.0-py2.py3-none-any.whl
Installing collected packages: bitstruct
Successfully installed bitstruct-3.9.0
```

```bash
H:\RishikeshAgrawani\Projects\Sof\BitFields>python
Python 2.7.14 |Anaconda custom (64-bit)| (default, Oct 15 2017, 03:34:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from bitstruct import pack, unpack, calcsize
>>> import sys
>>>
>>> # 3 bits counter
... # 29 bits encoding
... # both unsigned, so format string will be "u3u29"
... # total 32 bits means total storage occupied will be 4 bytes
...
>>> counter = 4;    # counter occupies 24 bytes
>>> encoding = 15;  # encoding occupies 24 bytes
>>>
>>> sys.getsizeof(counter)
24
>>> sys.getsizeof(encoding)
24
>>>
>>> # Let's store counter into 3 bits field and encoding into 29 bits field
... # We can check the occupied space using bitstruct.calcsize()
... # which returns size occupied in bits
... # unlike sys.getsizeof() which returns size in bytes
...
>>> packed_data = pack("u3u29", counter, encoding)
>>>
>>> packed_data
'\x80\x00\x00\x0f'
>>>
>>> calcsize("u3u29")
32
>>>
>>> data = unpack("u3u29", packed_data);
>>> data
(4, 15)
>>>
```