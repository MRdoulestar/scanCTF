#coding:utf-8
import requests
import os
import sys
def getFuzzUrl():
	try:
		f = open('./dictionary/default.txt','r')
		lines = f.readlines()
		f.close()
		data=[]
		for line in lines:
			data.append(line.strip('\n'))
		return data
	except:
		print("ERROR:::Can't open the dictionary.")

def run(url):
	r = requests.get(url,timeout=0.8)
	return r.status_code

if __name__ == '__main__':
	try:
		baseUrl = sys.argv[1]
	except:
		print("ERROR:::Please input the baseurl.")
		sys.exit(1)
	try:
		code = run(baseUrl)
	except:
		print("ERROR:::The baseurl is not valid.")
		sys.exit(1)

	extUrls = getFuzzUrl()
	# Start scanning
	for extUrl in extUrls:
		code = run(baseUrl+extUrl)
		if code!=404:
			print(str(code)+"-------"+baseUrl+extUrl)