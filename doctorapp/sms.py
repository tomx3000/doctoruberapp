import requests
import threading
import queue


class SendMessageThread(threading.Thread):
	def __init__(self,*args,**kargs):
		threading.Thread.__init__(self)
		self.phonenumber = kargs.get("phonenumber","0684905873")
		self.message = kargs.get("message","Welcome to Zatana")
		self.phone = kargs.get("phone","0684905873")
		self.password = kargs.get("password","Godwin0020")
	def run(self):
		SMS(phonenumber=self.phone,password=self.password).send(phonenumber=self.phonenumber,message=self.message)

class SMS:
	def __init__(self,*args,**kargs):
		print("connecting to sms gateway")
		self.url = kargs.get("url","https://devbulksms.zatana.net/api")
		response = requests.post(self.url+"/login",data={"phonenumber":kargs.get("phonenumber","0684905873") ,"password":kargs.get("password","Godwin0020")})
		self.token = response.json()["token"]
		self.available =response.json()["sms_available"]
		print("connection established")
		self.all={}
		
	def send(self,*args,**kargs):
		print("sending sms")
		response = requests.post(self.url+"/sendmessage",data={"phonenumber":kargs.get("phonenumber","0684905873") ,"message":kargs.get("message","testing")},headers={'Authorization': 'Bearer '+str(self.token)})
		return response.json()

		# send message
		pass
	def get(self):
		response = requests.get(self.url+"/sentmessages",headers={'Authorization': 'Bearer '+str(self.token)})
		self.all = response.json()
		return self
	
	def count(self):
		count = 0
		for sms in self.all:
			count+=sms["sms_count"]
		return count

	def filter(self,*args,**kargs):

		pass



if __name__ == '__main__':
	sms=SMS(email="godwinnaza@gmail.com",password="Godwin0020").send(phonenumber="0684905873",message="Thomas welcome home")
	# SendMessageThread(email="godwinnaza@gmail.com",password="1234",phonenumber="0684905873",message="12345").start()
	# print("all sma",sms.all)
	# print("sms count",sms.count())
	# print("available sms",sms.available)
	# print(sms.send(phonenumber="0684905873",message="Thomas welcome home"))

	


#  create a threading class for sending sms