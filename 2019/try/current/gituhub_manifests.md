Broswer > inspect > Application > Manifest > /manifest.json > click

https://github.com/manifest.json


```python
>>> import requests
>>> 
>>> res = requests.get('https://github.com/manifest.json')
>>> res
<Response [200]>
>>> 
>>> res.status_code
200
>>> 
>>> text = res.text
>>> text
'{"name":"GitHub","icons":[{"sizes":"114x114","src":"https://github.githubassets.com/apple-touch-icon-114x114.png"},{"sizes":"120x120","src":"https://github.githubassets.com/apple-touch-icon-120x120.png"},{"sizes":"144x144","src":"https://github.githubassets.com/apple-touch-icon-144x144.png"},{"sizes":"152x152","src":"https://github.githubassets.com/apple-touch-icon-152x152.png"},{"sizes":"180x180","src":"https://github.githubassets.com/apple-touch-icon-180x180.png"},{"sizes":"57x57","src":"https://github.githubassets.com/apple-touch-icon-57x57.png"},{"sizes":"60x60","src":"https://github.githubassets.com/apple-touch-icon-60x60.png"},{"sizes":"72x72","src":"https://github.githubassets.com/apple-touch-icon-72x72.png"},{"sizes":"76x76","src":"https://github.githubassets.com/apple-touch-icon-76x76.png"}]}'
>>> 
>>> from json import dumps
>>> 
>>> from json import loads
>>> 
>>> icons = json.loads(text)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'json' is not defined
>>> 
>>> icons = loads(text)
>>> icons
{'name': 'GitHub', 'icons': [{'sizes': '114x114', 'src': 'https://github.githubassets.com/apple-touch-icon-114x114.png'}, {'sizes': '120x120', 'src': 'https://github.githubassets.com/apple-touch-icon-120x120.png'}, {'sizes': '144x144', 'src': 'https://github.githubassets.com/apple-touch-icon-144x144.png'}, {'sizes': '152x152', 'src': 'https://github.githubassets.com/apple-touch-icon-152x152.png'}, {'sizes': '180x180', 'src': 'https://github.githubassets.com/apple-touch-icon-180x180.png'}, {'sizes': '57x57', 'src': 'https://github.githubassets.com/apple-touch-icon-57x57.png'}, {'sizes': '60x60', 'src': 'https://github.githubassets.com/apple-touch-icon-60x60.png'}, {'sizes': '72x72', 'src': 'https://github.githubassets.com/apple-touch-icon-72x72.png'}, {'sizes': '76x76', 'src': 'https://github.githubassets.com/apple-touch-icon-76x76.png'}]}
>>> 
>>> g_icons = loads(text)
>>> g_icons
{'name': 'GitHub', 'icons': [{'sizes': '114x114', 'src': 'https://github.githubassets.com/apple-touch-icon-114x114.png'}, {'sizes': '120x120', 'src': 'https://github.githubassets.com/apple-touch-icon-120x120.png'}, {'sizes': '144x144', 'src': 'https://github.githubassets.com/apple-touch-icon-144x144.png'}, {'sizes': '152x152', 'src': 'https://github.githubassets.com/apple-touch-icon-152x152.png'}, {'sizes': '180x180', 'src': 'https://github.githubassets.com/apple-touch-icon-180x180.png'}, {'sizes': '57x57', 'src': 'https://github.githubassets.com/apple-touch-icon-57x57.png'}, {'sizes': '60x60', 'src': 'https://github.githubassets.com/apple-touch-icon-60x60.png'}, {'sizes': '72x72', 'src': 'https://github.githubassets.com/apple-touch-icon-72x72.png'}, {'sizes': '76x76', 'src': 'https://github.githubassets.com/apple-touch-icon-76x76.png'}]}
>>> 
>>> icons = g_icons['icons']
>>> icons
[{'sizes': '114x114', 'src': 'https://github.githubassets.com/apple-touch-icon-114x114.png'}, {'sizes': '120x120', 'src': 'https://github.githubassets.com/apple-touch-icon-120x120.png'}, {'sizes': '144x144', 'src': 'https://github.githubassets.com/apple-touch-icon-144x144.png'}, {'sizes': '152x152', 'src': 'https://github.githubassets.com/apple-touch-icon-152x152.png'}, {'sizes': '180x180', 'src': 'https://github.githubassets.com/apple-touch-icon-180x180.png'}, {'sizes': '57x57', 'src': 'https://github.githubassets.com/apple-touch-icon-57x57.png'}, {'sizes': '60x60', 'src': 'https://github.githubassets.com/apple-touch-icon-60x60.png'}, {'sizes': '72x72', 'src': 'https://github.githubassets.com/apple-touch-icon-72x72.png'}, {'sizes': '76x76', 'src': 'https://github.githubassets.com/apple-touch-icon-76x76.png'}]
>>> 
>>> icons[0]
{'sizes': '114x114', 'src': 'https://github.githubassets.com/apple-touch-icon-114x114.png'}
>>> 
>>> pretty_text = dumps(icons, indent=4, sort_keys)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> 
>>> pretty_text = dumps(icons, indent=4, sort_keys=True)
>>> print(pretty_text)
[
    {
        "sizes": "114x114",
        "src": "https://github.githubassets.com/apple-touch-icon-114x114.png"
    },
    {
        "sizes": "120x120",
        "src": "https://github.githubassets.com/apple-touch-icon-120x120.png"
    },
    {
        "sizes": "144x144",
        "src": "https://github.githubassets.com/apple-touch-icon-144x144.png"
    },
    {
        "sizes": "152x152",
        "src": "https://github.githubassets.com/apple-touch-icon-152x152.png"
    },
    {
        "sizes": "180x180",
        "src": "https://github.githubassets.com/apple-touch-icon-180x180.png"
    },
    {
        "sizes": "57x57",
        "src": "https://github.githubassets.com/apple-touch-icon-57x57.png"
    },
    {
        "sizes": "60x60",
        "src": "https://github.githubassets.com/apple-touch-icon-60x60.png"
    },
    {
        "sizes": "72x72",
        "src": "https://github.githubassets.com/apple-touch-icon-72x72.png"
    },
    {
        "sizes": "76x76",
        "src": "https://github.githubassets.com/apple-touch-icon-76x76.png"
    }
]
>>> 
>>> pretty_text2 = dumps(g_icons, indent=4, sort_keys=True)
>>> print(pretty_text2)
{
    "icons": [
        {
            "sizes": "114x114",
            "src": "https://github.githubassets.com/apple-touch-icon-114x114.png"
        },
        {
            "sizes": "120x120",
            "src": "https://github.githubassets.com/apple-touch-icon-120x120.png"
        },
        {
            "sizes": "144x144",
            "src": "https://github.githubassets.com/apple-touch-icon-144x144.png"
        },
        {
            "sizes": "152x152",
            "src": "https://github.githubassets.com/apple-touch-icon-152x152.png"
        },
        {
            "sizes": "180x180",
            "src": "https://github.githubassets.com/apple-touch-icon-180x180.png"
        },
        {
            "sizes": "57x57",
            "src": "https://github.githubassets.com/apple-touch-icon-57x57.png"
        },
        {
            "sizes": "60x60",
            "src": "https://github.githubassets.com/apple-touch-icon-60x60.png"
        },
        {
            "sizes": "72x72",
            "src": "https://github.githubassets.com/apple-touch-icon-72x72.png"
        },
        {
            "sizes": "76x76",
            "src": "https://github.githubassets.com/apple-touch-icon-76x76.png"
        }
    ],
    "name": "GitHub"
}
>>> 
>>> pretty_text2 = dumps(g_icons, indent=4, sort_keys=True, separators=('->', '#'))
>>> pretty_text3 = dumps(g_icons, indent=4, sort_keys=True, separators=('->', '#'))
>>> pretty_text3
'{\n    "icons"#[\n        {\n            "sizes"#"114x114"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-114x114.png"\n        }->\n        {\n            "sizes"#"120x120"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-120x120.png"\n        }->\n        {\n            "sizes"#"144x144"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-144x144.png"\n        }->\n        {\n            "sizes"#"152x152"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-152x152.png"\n        }->\n        {\n            "sizes"#"180x180"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-180x180.png"\n        }->\n        {\n            "sizes"#"57x57"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-57x57.png"\n        }->\n        {\n            "sizes"#"60x60"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-60x60.png"\n        }->\n        {\n            "sizes"#"72x72"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-72x72.png"\n        }->\n        {\n            "sizes"#"76x76"->\n            "src"#"https://github.githubassets.com/apple-touch-icon-76x76.png"\n        }\n    ]->\n    "name"#"GitHub"\n}'
>>> 
>>> print(pretty_text3)
{
    "icons"#[
        {
            "sizes"#"114x114"->
            "src"#"https://github.githubassets.com/apple-touch-icon-114x114.png"
        }->
        {
            "sizes"#"120x120"->
            "src"#"https://github.githubassets.com/apple-touch-icon-120x120.png"
        }->
        {
            "sizes"#"144x144"->
            "src"#"https://github.githubassets.com/apple-touch-icon-144x144.png"
        }->
        {
            "sizes"#"152x152"->
            "src"#"https://github.githubassets.com/apple-touch-icon-152x152.png"
        }->
        {
            "sizes"#"180x180"->
            "src"#"https://github.githubassets.com/apple-touch-icon-180x180.png"
        }->
        {
            "sizes"#"57x57"->
            "src"#"https://github.githubassets.com/apple-touch-icon-57x57.png"
        }->
        {
            "sizes"#"60x60"->
            "src"#"https://github.githubassets.com/apple-touch-icon-60x60.png"
        }->
        {
            "sizes"#"72x72"->
            "src"#"https://github.githubassets.com/apple-touch-icon-72x72.png"
        }->
        {
            "sizes"#"76x76"->
            "src"#"https://github.githubassets.com/apple-touch-icon-76x76.png"
        }
    ]->
    "name"#"GitHub"
}
>>> 
>>> pretty_text3 = dumps(g_icons, indent=4, sort_keys=True, separators=('#', ' => '))
>>> pretty_text3
'{\n    "icons" => [\n        {\n            "sizes" => "114x114"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-114x114.png"\n        }#\n        {\n            "sizes" => "120x120"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-120x120.png"\n        }#\n        {\n            "sizes" => "144x144"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-144x144.png"\n        }#\n        {\n            "sizes" => "152x152"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-152x152.png"\n        }#\n        {\n            "sizes" => "180x180"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-180x180.png"\n        }#\n        {\n            "sizes" => "57x57"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-57x57.png"\n        }#\n        {\n            "sizes" => "60x60"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-60x60.png"\n        }#\n        {\n            "sizes" => "72x72"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-72x72.png"\n        }#\n        {\n            "sizes" => "76x76"#\n            "src" => "https://github.githubassets.com/apple-touch-icon-76x76.png"\n        }\n    ]#\n    "name" => "GitHub"\n}'
>>> 
>>> print(pretty_text3)
{
    "icons" => [
        {
            "sizes" => "114x114"#
            "src" => "https://github.githubassets.com/apple-touch-icon-114x114.png"
        }#
        {
            "sizes" => "120x120"#
            "src" => "https://github.githubassets.com/apple-touch-icon-120x120.png"
        }#
        {
            "sizes" => "144x144"#
            "src" => "https://github.githubassets.com/apple-touch-icon-144x144.png"
        }#
        {
            "sizes" => "152x152"#
            "src" => "https://github.githubassets.com/apple-touch-icon-152x152.png"
        }#
        {
            "sizes" => "180x180"#
            "src" => "https://github.githubassets.com/apple-touch-icon-180x180.png"
        }#
        {
            "sizes" => "57x57"#
            "src" => "https://github.githubassets.com/apple-touch-icon-57x57.png"
        }#
        {
            "sizes" => "60x60"#
            "src" => "https://github.githubassets.com/apple-touch-icon-60x60.png"
        }#
        {
            "sizes" => "72x72"#
            "src" => "https://github.githubassets.com/apple-touch-icon-72x72.png"
        }#
        {
            "sizes" => "76x76"#
            "src" => "https://github.githubassets.com/apple-touch-icon-76x76.png"
        }
    ]#
    "name" => "GitHub"
}
>>> 
```