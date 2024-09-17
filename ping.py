#Ping.py
import subprocess

def ping_device(ip):
	#Ping a device and return true or false

	print(f'Attempting to ping {ip} to ensure it is reachable...')
	r = subprocess.run(['ping', ip, '-n', '2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

	if r.returncode == 0:
		print('Device Pings, OK to Proceed')
		return True
	else:
		print(f'No Ping Response from {ip}')
		return False