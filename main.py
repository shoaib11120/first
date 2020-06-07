import web
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile','Profile',
	'/profile/sign_up','Sign_up'
)
rende=web.template.render("views/resources/", base="base_layout")
class Welcome:
	"""docstring for home"""
	def GET(self):
		return rende.welcome()
class Profile:
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
if __name__ == "__main__" :
	app=web.application(urls,globals())
	app.run()
		
