import web
import random
from models import user_data
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile','Profile',
	'/profile/sign_up','Sign_up',
	'/post-sign-up','Sign_up_user'
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
	def GET(self):
		obj=user_data.user()
		return rende.profile(obj.getUName(),obj.getFName(),obj.getEmail())
class Home:
	"""docstring for home"""
	def GET(self):
		return rende.home()
class Sign_up:
	"""docstring for home"""
	def GET(self):
		return rende.sign_up()
class Sign_up_user:
	def POST(self):

		data=web.input()
		obj=user_data.user()
		return obj.setUser(data.username,data.full_name,data.email,data.password,data.c_password)

if __name__ == "__main__" :
	app=web.application(urls,globals())
	app.run()
		
