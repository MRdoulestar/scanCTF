#coding=utf-8
__author__ = yunsle
import threading
import requests
import os
import sys
import Queue
import time

q = Queue.Queue()
thread_num = 8

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
			print(str(code)+"--------------------"+baseUrl+extUrl.strip())
	

threads=[]
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

	st = time.time()
	for i in range(thread_num):
		threads.append(threading.Thread(target=scan))
	for i in range(thread_num):
		threads[i].setDaemon(True)
		threads[i].start()
	for i in range(thread_num):
		threads[i].join()
	et = time.time()
	print("Cost time %.3fs" % (et - st))
