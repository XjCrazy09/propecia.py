#!/usr/bin/python
#############################################################################################
# This program is meant to check Class C's for a small amount of ports.  In no way is this  #
# supposed to replace nmap which is very well optimized for a large amount of IPs and Port  #
# ranges.  This is good for doing a couple of Class C's at a time looking for 1 or 2 ports. #
#                                                                                           #
# Author: Ryan Villarreal                                                                   #
# Date: 2.24.17                                                                             #
#############################################################################################
import sys, socket, threading, argparse, re

# define argument parser #
parser = argparse.ArgumentParser()
parser.add_argument('--port','-p',dest="port",help='port help', required=True, nargs="+", type=int)
parser.add_argument('-V', '--version', action='version', version='%(prog)s (version 0.1)')

# define mutually exclusive group
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--multi','-m',dest="multi",help='Address List help', nargs="?")
group.add_argument('--addr','-a',dest="addr",help='address help', nargs="+")
args = parser.parse_args()


# Check if a port is open or not.
def test_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((str(ip), int(port)))
        s.close
        screenLock.acquire()
        print ip,port
        screenLock.release()
        return True
    except:
        return False


# multi-threading function
def start_thread(ip, port):
    t = threading.Thread(target=test_port, args=(ip, port))
    t.start()


# iterate through a class C address space
def class_c(ip_prefix, port):
	#print "Trying Clas C: %s:%i" % (ip_prefix,port)  #uncomment to debug
	for n in range(0,256):
    		ip = ip_prefix + "." + str(n)
    		start_thread(ip, port)


# make sure that the IP is entered in correct format
def ip_check(ip_prefix, port):
	try:
		parts = ip_prefix.split('.')
		answer = len(parts) == 3 and all(0 <= int(part) < 256 for part in parts)
		if answer:
			# if passes the regex send it to the class c function
			class_c(ip_prefix,port)
		else:
			print "%s input should be formated as [X.X.X]" % (ip_prefix)
	except ValueError:
		print "One Part is not a convertible to integer"
	except (AttributeError, TypeError):
		print "IP address is not a string"

if __name__ == "__main__":
	# Create screenlock to handle the multi-threading count
	screenLock = threading.Semaphore(value=1)

	# if text file is passed in parse it.  Otherwise just add the address to the list
	addresses = []
	if args.multi is not None:
		file = open(args.multi, 'r')
		addresses = [line.rstrip().split(',') for line in file.readlines()]
	else:
		addresses = args.addr

	#### Logic time.  Let's go through each port and check the Class C ###
	for port in args.port:
		for ip in addresses:
			ip = ''.join(ip)
			ip_check(ip, port)
