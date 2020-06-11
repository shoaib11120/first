import web
import random
from models import sign_up_user,log_in_user
web.config.debug=False
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile','Profilep',
	'/profile/sign_up','Sign_up',
	'/profile/log_in','Log_in',
	'/post-sign-up','Sign_up_user',
	'/post-log-in','Log_In_user'
)

app=web.application(urls,globals())
session=web.session.Session(app,web.session.DiskStore("session"),initializer={'user':None})
session_data=session._initializer

rende=web.template.render("views/resources/", base="base_layout",globals={'session':session_data,'current_user':session_data["user"]})

class Welcome:
	"""docstring for home"""
	def GET(self):
		imG=img[random.randrange(0,7)]
		print(imG)
		return rende.welcome(imG)

class Profilep:
	"""docstring for home"""
	def GET(self):
		return rende.profile1()
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
		rValue=obj.setUser(data.username,data.full_name,data.email,data.password,data.c_password)
		if rValue!='' and rValue!='PError'  and rValue!='EUError':
			session_data["user"]=rValue
		return rValue
class Log_In_user:
	def POST(self):
		data=web.input()
		obj=log_in_user.user()
		print('reached')
		rValue=obj.getUser(data.username,data.password)
		print('reached')
		print(str(rValue))
		if rValue!='' and rValue!='PError'  and rValue!='UError':
			print(str(rValue))
			session_data["uiser"]=None
			session_data["user"]=rValue
		return rValue

if __name__ == "__main__" :
	
	app.run()
		
