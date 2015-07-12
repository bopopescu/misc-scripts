import serial
import time

devName = raw_input("Enter device name (/dev/ttyUSB0): ")
if devName in ["", None]:
	devName = "/dev/ttyUSB0"

baud = raw_input("Enter baud rate (115200): ")
if baud in ["", None]:
	baud = 115200
else:
	baud = int(baud)




com = serial.Serial(port=devName, baudrate=baud)
if not com.isOpen():
	print "Opening port...", "OK" if com.open() == None else "ERR"

try:
	while True:
		inp = raw_input(">> ")
		if inp not in ["", None]:
			com.write(inp + "\r\n")
	
		time.sleep(0.2)
		out = ""
		while com.inWaiting() > 0:
			out += com.read(1)
		if out != "":
			print out
except KeyboardInterrupt:
	print "\nClosing port...", "OK" if com.close() == None else "ERR!"
