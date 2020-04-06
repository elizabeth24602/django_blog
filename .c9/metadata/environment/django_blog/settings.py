{"filter":false,"title":"settings.py","tooltip":"/django_blog/settings.py","undoManager":{"mark":39,"position":39,"stack":[[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":29},"action":"insert","lines":["'django_forms_bootstrap',"],"id":69}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":70},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":18,"column":14},"action":"insert","lines":["import os","import dj_database_url","","if os.path.exists('env.py'):","    import env"],"id":71}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["s"],"id":72},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["o"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":[" "]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["t"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"remove","lines":["o"],"id":73},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"remove","lines":["p"]},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"remove","lines":["m"]},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["i"]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":74}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["import os",""],"id":75}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["i"],"id":76},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":["m"]}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["p"],"id":77},{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["o"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["t"],"id":78}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":[" "],"id":79},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["o"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":9},"action":"remove","lines":["os"],"id":80},{"start":{"row":12,"column":7},"end":{"row":12,"column":9},"action":"insert","lines":["os"]}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":81}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":65},"action":"remove","lines":["'od3*7y$8q7hgfve#k=+8vd6k78h!*h#p_c*9%q4!qdxe4m@557'"],"id":82},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":[" "],"id":83}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":41},"action":"insert","lines":["os.environ.get(\"SECRET_KEY\")"],"id":84}],[{"start":{"row":79,"column":0},"end":{"row":87,"column":1},"action":"remove","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}"],"id":85},{"start":{"row":79,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","}"]}],[{"start":{"row":54,"column":61},"end":{"row":55,"column":0},"action":"insert","lines":["",""],"id":86},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":55,"column":4},"end":{"row":55,"column":49},"action":"insert","lines":["'whitenoise.middleware.WhiteNoiseMiddleware',"],"id":87}],[{"start":{"row":133,"column":0},"end":{"row":134,"column":0},"action":"insert","lines":["",""],"id":88}],[{"start":{"row":133,"column":0},"end":{"row":133,"column":51},"action":"insert","lines":["STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')"],"id":89}],[{"start":{"row":83,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","}"],"id":90},{"start":{"row":83,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {","        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","    }","else:","    print(\"Postgres URL not found, using sqlite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }",""]}],[{"start":{"row":96,"column":0},"end":{"row":97,"column":0},"action":"remove","lines":["",""],"id":91}],[{"start":{"row":31,"column":86},"end":{"row":31,"column":87},"action":"insert","lines":[","],"id":92}],[{"start":{"row":31,"column":87},"end":{"row":31,"column":88},"action":"insert","lines":[" "],"id":93}],[{"start":{"row":31,"column":88},"end":{"row":31,"column":90},"action":"insert","lines":["''"],"id":94}],[{"start":{"row":31,"column":89},"end":{"row":31,"column":90},"action":"insert","lines":["e"],"id":95},{"start":{"row":31,"column":90},"end":{"row":31,"column":91},"action":"insert","lines":["l"]},{"start":{"row":31,"column":91},"end":{"row":31,"column":92},"action":"insert","lines":["i"]},{"start":{"row":31,"column":92},"end":{"row":31,"column":93},"action":"insert","lines":["z"]}],[{"start":{"row":31,"column":93},"end":{"row":31,"column":94},"action":"insert","lines":["a"],"id":96},{"start":{"row":31,"column":94},"end":{"row":31,"column":95},"action":"insert","lines":["b"]},{"start":{"row":31,"column":95},"end":{"row":31,"column":96},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":96},"end":{"row":31,"column":97},"action":"insert","lines":["t"],"id":97},{"start":{"row":31,"column":97},"end":{"row":31,"column":98},"action":"insert","lines":["h"]}],[{"start":{"row":31,"column":98},"end":{"row":31,"column":99},"action":"insert","lines":["2"],"id":98},{"start":{"row":31,"column":99},"end":{"row":31,"column":100},"action":"insert","lines":["4"]},{"start":{"row":31,"column":100},"end":{"row":31,"column":101},"action":"insert","lines":["6"]}],[{"start":{"row":31,"column":101},"end":{"row":31,"column":102},"action":"insert","lines":["0"],"id":99},{"start":{"row":31,"column":102},"end":{"row":31,"column":103},"action":"insert","lines":["2"]},{"start":{"row":31,"column":103},"end":{"row":31,"column":104},"action":"insert","lines":["-"]}],[{"start":{"row":31,"column":104},"end":{"row":31,"column":105},"action":"insert","lines":["b"],"id":100},{"start":{"row":31,"column":105},"end":{"row":31,"column":106},"action":"insert","lines":["l"]},{"start":{"row":31,"column":106},"end":{"row":31,"column":107},"action":"insert","lines":["o"]}],[{"start":{"row":31,"column":107},"end":{"row":31,"column":108},"action":"insert","lines":["g"],"id":101},{"start":{"row":31,"column":108},"end":{"row":31,"column":109},"action":"insert","lines":["-"]},{"start":{"row":31,"column":109},"end":{"row":31,"column":110},"action":"insert","lines":["a"]}],[{"start":{"row":31,"column":110},"end":{"row":31,"column":111},"action":"insert","lines":["p"],"id":102},{"start":{"row":31,"column":111},"end":{"row":31,"column":112},"action":"insert","lines":["p"]}],[{"start":{"row":31,"column":112},"end":{"row":31,"column":113},"action":"insert","lines":["."],"id":103},{"start":{"row":31,"column":113},"end":{"row":31,"column":114},"action":"insert","lines":["h"]},{"start":{"row":31,"column":114},"end":{"row":31,"column":115},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":115},"end":{"row":31,"column":116},"action":"insert","lines":["r"],"id":104},{"start":{"row":31,"column":116},"end":{"row":31,"column":117},"action":"insert","lines":["o"]},{"start":{"row":31,"column":117},"end":{"row":31,"column":118},"action":"insert","lines":["k"]},{"start":{"row":31,"column":118},"end":{"row":31,"column":119},"action":"insert","lines":["u"]}],[{"start":{"row":31,"column":119},"end":{"row":31,"column":120},"action":"insert","lines":["."],"id":105}],[{"start":{"row":31,"column":120},"end":{"row":31,"column":121},"action":"insert","lines":["c"],"id":106},{"start":{"row":31,"column":121},"end":{"row":31,"column":122},"action":"insert","lines":["o"]},{"start":{"row":31,"column":122},"end":{"row":31,"column":123},"action":"insert","lines":["m"]}],[{"start":{"row":31,"column":119},"end":{"row":31,"column":120},"action":"insert","lines":["a"],"id":107},{"start":{"row":31,"column":120},"end":{"row":31,"column":121},"action":"insert","lines":["p"]},{"start":{"row":31,"column":121},"end":{"row":31,"column":122},"action":"insert","lines":["p"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586179579056,"hash":"7eb1460a095b73e79ba0176bad0901e457efb119"}