import telnetlib
import time

def open_telnet_conn(ip):
	try:
	
		username = praktan
		password = python
	
		cmd_file = raw_input("Enter a file for configuration: ")
		
		port = 23
		connection_timeout = 5
		reading_timeout = 5

		connection = telnetlib.Telnet(ip, port, connection_timeout)
		
		output = connection.read_until("Username:", reading_timeout)
		connection.write(username + '\n')
		output = connection.read_until("word:", reading_timeout)
		connection.write(password + '\n')
		time.sleep(1)

		connection.write('\n configure teminal\n')
		time.sleep(1)

		selected_cmd_file = open(cmd_file, 'r')
		selected_cmd_file.seek(0)

		for each_line in selected_cmd_file.readlines():
			connection.write(each_line + '\n')
			time.sleep(1)

		selected_cmd_file.close()
		
		connection.close()

	except IOError:
		print "Input parameter error! please check username and pasword"

open_telnet_conn(ip)



