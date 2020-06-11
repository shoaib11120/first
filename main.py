import web
import random
from models import sign_up_user,log_in_user
urls = (
	'/','Welcome',
	'/home','Home',
	'/(.*)/profile','Profile',
	'/profile','Profilep',
	'/profile/sign_up','Sign_up',
	'/profile/log_in','Log_in',
	'/post-sign-up','Sign_up_user',
	'/post-log-in','Log_in_user'
)
img=["/static/assets/img(1).jpg", "/static/assets/img(2).jpg","/static/assets/img(3).jpg","/static/assets/img(4).jpg","/static/assets/img(5).jpg","/static/assets/img(6).jpg","/static/assets/img(7).jpg"]
web.config.debug=True
rende=web.template.render("views/resources/", base="base_layout")

class Welcome:
	"""docstring for home"""
	def GET(self):
		imG=img[random.randrange(0,7)]
		print(imG)
		return rende.welcome(imG)
class Profile:
	"""docstring for home"""
	def GET(self,name):
		return rende.profile()
class Profilep:
	"""docstring for home"""
	def GET(self):
		return rende.profile()
class Home:
	"""docstring for home"""
	def GET(self):
		return rende.home()
class Sign_up:
	"""docstring for home"""
	def GET(self):
		return rende.sign_up()
class Log_in:
	"""docstring for home"""
	def GET(self):
		return rende.log_in()
class Sign_up_user:
	def POST(self):
		data=web.input()
		obj=sign_up_user.user()
		return obj.setUser(data.username,data.full_name,data.email,data.password,data.c_password)
class Log_in_user:
	def POST(self):
		data=web.input()
		obj=log_in_user.user()
		return obj.getUser(data.username,data.password)

if __name__ == "__main__" :
	app=web.application(urls,globals())
	app.run()
		
