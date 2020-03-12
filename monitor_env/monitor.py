import os
import smtplib
import requests 
# linode is where he set his environment variable called LinodeClient, and the specific instance 
# from linode_api4 import LinodeClient, Instance

# how to get environment variables
# how to set environment variables in Windows 10 here: https://www.onmsft.com/how-to/how-to-set-an-environment-variable-in-windows-10
# add the token/acctName, password that will connect you to the server

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# you need to restart everything afterwards, in order for the changes to take effect 
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def notify_user():
	# use a mail server. need to know how to connect to the mail server. find out what the port is
	with smtplib.SMTP('localhost', 2525) as smtp:
	# ehlo method identifies ourselves with the server we're using
		smtp.ehlo()
		# encrypt our traffic
		# smtp.starttls()
		# re-identify ourselves
		# smtp.ehlo()
		
		# put login info in a config file/environment variables
		# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		
		subject = 'URL ERROR'
		body = 'URL has either a client error(4xx status code) or server error(5xx status code)'
		msg = f'Subject: {subject}\n\n{body}'
		
		# smtp.sendmail(SENDER, RECEIVER, msg) - where SENDER, RECEIVER are described below
		smtp.sendmail(EMAIL_ADDRESS, 'jnp775@gmail.com', msg)
		
def reboot_server():
	# keep this code if we want to reboot the server whenever the server goes down	
	# client = LinodeClient(LINODE_TOKEN)

	# replace the number with the actual ID of the server
	# my_server = client.load(Instance, 376715)
	print ('rebooting')

	# reboot the server
	# my_server.reboot()
	
# this 	will catch any other type of problem(ie, Apache stopping or some other service)
try:
	# if you do use 2-factor authentication, you need to configure it to accept your password, https://myaccount.google.com/apppasswords
	r = requests.get('http://10.56.46.16/SF-ML/Services/WSEmail/WSEmail.asmx', timeout=5)
	
	# to run the script: from git bash from th working folder, type 'python monitor.py'
	# use 'if not r.ok:' if you're checking for responses that are not only 200 - in our case either 100-200 responses
	if r.status_code != 200: 
		notify_user()
		reboot_server()
except Exception as e:
	notify_user()
	reboot_server()
	
# Remove once you've got the server name & ID.  
# to print the server name: server ID	
# def print_servername_and_id():
	# for Linode in client.linode.instances():
	#	print(f'{linode.label}: {linode.id}')
	
# to run this script automatically on a schedule, you can use Windows task scheduler
# if you create a virtual environment for this, remember to have the necessary packages installed in the appropriate environment are active when 
# running the script. This will make everything you need available on a routine basis.
