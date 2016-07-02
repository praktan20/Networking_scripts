import paramiko
import time
import re

def open_ssh_conn(ip):
	try:
		user_file = sys.argv[1]
		cmd_file = sys.argv[2]
		
		selected_user_file = open(user_file, 'r')
		selected_user_file.seek(0)
		username = selected_user_file.readlines()[0].split(',')[0]
		selected_user_file.seek(0)
		password = selected_user_file.readlines()[0].split(',')[1].rstrip('\n')
		
		session = paramiko.SSHClient()

		session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		session.connect(ip, username = username, password = password)
		connection = session.invoke_shell()
		
		connection.send('terminal length 0\n')
		time.sleep(1)

		connection.send('\n')
		connection.send('configure terminal \n')
		time.sleep(1)
		
		selected_cmd_file = open(cmd_file, 'r')
		selected_cmd_file.seek(0)
		for each_line in selected_cmd_file.readlines():
			connection.send(each_line + '\n')
			time.sleep(1)
		selected_user_file.close()
		selected_cmd_file.close()
		
		output = connection.recv(65535)
	except paramiko.AuthenticationException:
		print "Invalid username and password"
	
open_ssh_conn(ip)
		
