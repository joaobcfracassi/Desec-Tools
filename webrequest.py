#!/usr/bin/python

import requests

site = requests.get("http://businesscorp.com.br/huehuehu")
status = site.status_code

if (status == 200):
	print "Pagina existe"
else:
	print "Pagina inexistente"
