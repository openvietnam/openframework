from paste import httpserver
from paste.deploy import loadapp
import os



INI_PATH = "config:{}".format(os.path.abspath("openframework_paste.ini"))
wsgi_app = loadapp(INI_PATH, name="common")

httpserver.serve(wsgi_app, host='0.0.0.0', port=8080)