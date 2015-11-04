import evdev
import struct
import sys
import urllib2
import json

FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

in_file = open("/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd", 'rb')

def contactServer(c):
	URL = "http://core.foundry.bio/access/check?control=Front%20Door&match="+c
	response = urllib2.urlopen(URL)
	data = json.load(response)
	if data["access"] == "allow":
		print "Access granted."
		print "Welcome", data["firstname"], data["lastname"]
		response2 = urllib2.urlopen("http://core.foundry.bio/events/api/453fd2a/enqueue?category=frontdoor&data=default")

def getRFIDCode():
	"Reads characters till the input device puts in a newline"
	currentBuffer = ''
	event = in_file.read(EVENT_SIZE)
	while event:
	    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

	    if type != 0 or code != 0 or value != 0:
		if type == 1 and code >= 2 and code <= 10 and value == 1:
			currentBuffer += str(code-1)
		elif type == 1 and code == 11 and value == 1:
			currentBuffer += '0'
		elif type == 1 and code == 28 and value == 0:
			return currentBuffer
		else:
			pass
		        #print("Event type %u, code %u, value: %u at %d, %d" % \
        	        #      (type, code, value, tv_sec, tv_usec))

	    event = in_file.read(EVENT_SIZE)


try:
	while True:
		code = getRFIDCode()
		contactServer(code)
except Exception as e:
	print(e)
finally:
	in_file.close()

