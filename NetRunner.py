#NetRunner.py
import ping
from netmiko import ConnectHandler
import getpass
import os
import time

def menu():
	os.system('cls')
	print('* * * * * * * * * * * * * * * * * * * * * * * * *')
	print('                                                 ')
	print('                 NetRunner v0.01                 ')
	print('                                                 ')
	print('* * * * * * * * * * * * * * * * * * * * * * * * *')

	print('\n\n')

	print('Menu Selection')
	print('- - - - - - - - - - - - - - - - - - - - - - - - -')
	print('1. Run Commands Across a Single Device')
	print('2. Run Commands Across Multiple Devices')
	print('- - - - - - - - - - - - - - - - - - - - - - - - -')
	choice = input('Choice: ')
	os.system('cls')
	details = getSwitch(choice)


def getSwitch(choice):
	switch = []
	username = input("Username: ")
	password = getpass.getpass()

	if choice == 1:
		switch.append(input("Hostname or IP Address: "))

	else:
		file = input('Please Enter the Name of the .txt File Containing the Device IP/Hostname Details: ')
		
		#Add the .txt in case the user does not
		if '.txt' not in file:
			file += '.txt'

		with open(file) as f:
			d = f.read().splitlines()

		for ip in d:
			switch.append(ip)

	commands = getCommands()
	netRun(switch, username, password, commands)

def getCommands():
	os.system('cls')
	commands = []
	t = ''

	print('Commands To Run:')
	print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	print('Please note that each command should be separated by a "," in between each command')
	print('(ie. conf t, default int Gi1/0/1, shut int Gi1/0/1)')
	print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	c = input('Please Enter Commands to Run: ')
	c += ','

	for i in c:
		if i == ',':
			commands.append(t)
			t = ''
		else:
			t += i

	return commands

def netRun(host, username, password, commands):
	os.system('cls')
	for entry in host:
		if ping.ping_device(entry):
			remote_connection = {
				'device_type': 'cisco_ios',
				'host': entry,
				'username': username,
				'password': password
			}

			for command in commands:
				print(f'Running: {command}')
				net_connect.send_command(command)



if __name__ == '__main__':
	menu()