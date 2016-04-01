import os.path
from waitress import serve

TOP =  "<div class='top'>Middleware TOP</div>"
BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"
openBody = '<body>'
closeBody = '</body>'

class my_middle_ware(object):
 	def __init__(self, my_app):
 		self.my_app = my_app
 	def __call__(self, environment, startResponce):
 		response = self.my_app(environment, startResponce)[0].decode()

 		if response.find(openBody) > -1:
 			header,body = response.split(openBody)
 			bodycontent,htmlend = body.split(closeBody)
 			bodycontent = openBody+ TOP + bodycontent + BOTTOM + closeBody
 			return [header.encode() + bodycontent.encode() + htmlend.encode()]
 		else:
 			return [TOP + response.encode() + BOTTOM]
 		
def my_app(environment, startResponce):
 	response = environment['PATH_INFO']
 	if response == '/' or response == '/index.html':
 		filePath = './index.html'
 		print('Page index')
 	if response == '/about/aboutme.html':
 		filePath = './about/aboutme.html'
 		print('Page about')
 	else:
 		filePath = './index.html'
		
 	file = open(filePath,'r')
 	fileContent = file.read()
 	file.close() 	
 	startResponce('200 OK', [('Content-Type', 'text/html')])
 	return [fileContent.encode()]

my_app = my_middle_ware(my_app)
serve(my_app, host='localhost', port=8000)
