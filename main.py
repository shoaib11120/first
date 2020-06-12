import web
import random
from models import sign_up_user,log_in_user
web.config.debug=True
urls = (
	'/','Welcome',
	'/home','Home',
	'/profile/sign_up','Sign_up',
	'/profile/log_in','Log_in',
	'/profile/log_out','Log_out',
	'/post-sign-up','Sign_up_user',
	'/post-log-in','Log_In_user',
	'/profile','Profile'
)

app=web.application(urls,globals())
if web.config.get('_session') is None:
	session=web.session.Session(app,web.session.DiskStore("session"),initializer={'user':None})
	
	web.config._session=session
else:
	session=web.config._session

session_data=session._initializer
rende=web.template.render("views/resources/", base="base_layout",globals={'session':session_data})

class Welcome:
	"""docstring for home"""
	def GET(self):
		return rende.welcome()

class Profile:
	"""docstring for home"""
	def GET(self):
		print('profiler')
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
class Log_out:
	"""docstring for home"""
	def GET(self):
		session["user"]=None
		session_data["user"]=None
		#session.kill()
		return "success"
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
		print('reached')
		data=web.input()
		obj=log_in_user.user()
		rValue=obj.getUser(data.username,data.password)
		if rValue!='' and rValue!='PError'  and rValue!='UError':
			print(str(rValue))
			session_data["user"]=rValue
		return rValue

if __name__ == "__main__" :
	
	app.run()
		
