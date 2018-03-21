#coding=utf-8

import threading
import requests
import os
import sys
import Queue

q = Queue.Queue()
thread_num = 6

def getFuzzUrl():
	try:
		f = open('./dictionary/default.txt','r')
		lines = f.readlines()
		f.close()
		for line in lines:
			q.put(line.rstrip('\n'))
	except Exception as e:
		print(e)
def request(url):
	r = requests.get(url)
	return r.status_code

def scan():
	# Start scanning
	while not q.empty():
		extUrl = q.get()
		code = request(baseUrl+extUrl)
		if code!=404:
			print(str(code)+"--------------------"+baseUrl+extUrl)
	

if __name__ == '__main__':
	try:
		baseUrl = sys.argv[1].rstrip('/')
	except Exception as e:
		print(e)
		print("ERROR:::Please input the baseurl.")
		sys.exit(1)
	try:
		code = request(baseUrl)
	except Exception as e:
		print(e)
		print("ERROR:::The baseurl is not valid.")
		sys.exit(1)
	getFuzzUrl()
	for i in range(thread_num):
		t = threading.Thread(target=scan)
		t.start()
