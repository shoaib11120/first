import web
urls = (
	'/','home'
)
rende=web.template.render("views/resources/")
css=web.template.render("views/resources/css/")
class home:
	"""docstring for home"""
	def GET(self):
		home_css=str(css.home())
		return rende.home(home_css)


if __name__ == "__main__" :
	app=web.application(urls,globals())
	app.run()
		
