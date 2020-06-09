import web
from models import user_data
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile','Profile',
	'/profile/sign_up','Sign_up',
	'/post-sign-up','Sign_up_user'
)
web.config.debug=True
rende=web.template.render("views/resources/", base="base_layout")
class Welcome:
	"""docstring for home"""
	def GET(self):
		return rende.welcome()
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
		
