import web
from models import sign_upM
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile','Profile',
	'/profile/sign_up','Sign_up',
	'/post-sign-up','Sign_up_user'
)
rende=web.template.render("views/resources/", base="base_layout")
class Welcome:
	"""docstring for home"""
	def GET(self):
		return rende.welcome()
class Profile:
	"""docstring for home"""
	def GET(self):
		print('profile')
		return rende.profile()
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
		print("reached")
		data=web.input()
		print(data.username)
		return data.username
if __name__ == "__main__" :
	app=web.application(urls,globals())
	app.run()
		
