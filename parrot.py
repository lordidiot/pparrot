#!/usr/bin/python

import socket 
import argparse 
from time import sleep, time
from termcolor import colored, cprint
from itertools import cycle, izip

"""
                   .ccccccc.                      
               .ccckNKOOOOkdcc.                   
            .;;cc:ccccccc:,:c::,,.                
         .c;:;.,cccllxOOOxlllc,;ol.               
        .lkc,coxo:;oOOxooooooo;..:,               
      .cdc.,dOOOc..cOd,.',,;'....':l.             
      cNx'.lOOOOxlldOc..;lll;.....cO;             
     ,do;,:dOOOOOOOOOl'':lll;..:d:''c,            
     co..lOOOOOOOOOOOl'':lll;.'lOd,.cd.           
     co.'dOOOOOOOOOOOo,.;llc,.,dOOc..dc           
     co..lOOOOOOOOOOOOc.';:,..cOOOl..oc           
   .,:;.'::lxOOOOOOOOOo:'...,:oOOOc.'dc           
   ;Oc..cl'':lldOOOOOOOOdcclxOOOOx,.cd.           
  .:;';lxl''''':lldOOOOOOOOOOOOOOc..oc            
,dl,.'cooc:::,....,::coooooooooooc'.c:            
cNo.................................oc            
"""

def error(msg):
	cprint("Error: {}!".format(msg))
	exit(-1)

def handle_color(frame):
	global frame_cnt
	if num_colors == 1:
		return colored(frame, colors[0])
	elif args.color == "rainbow":
		return colored(frame, colors[frame_cnt])
	elif args.color == "ultra-rainbow":
		output = ""
		off = 0
		for line in frame.split('\n'):
			output += colored(line+'\n', colors[(frame_cnt+(off/3))%num_colors])
			off += 1
		return output

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="PARTY OR DIE")
	parser.add_argument("type",
						metavar="TYPE",
						help="Type of party parrot [normal, two, two-oppo, three, six]")

	parser.add_argument("color",
						metavar="COLOR",
						help="Color of party parrot [red, green, yellow, blue, magenta, cyan, rainbow, ultra-rainbow]")

	parser.add_argument("interval",
						metavar="TIME_INTVL",
						help="Time interval for each animation frame (in seconds)")

	parser.add_argument("-t", "--start-time",
						metavar="START_TIME",
						help="Time to start partying in the future (in epoch time)")

	parser.add_argument("-r", "--remote",
						metavar="HOST:PORT",
						help="Connect to remote server to receive party time!")

	args = parser.parse_args()

	frames = []
	for i in xrange(10):
		with open("frames/{}.txt".format(i), "r") as f:
			frames.append(f.read())

	# handle parrot type
	if args.type == "normal":
		pass
	elif args.type == "two":
		for i in xrange(10):
			newframe = ""
			for line in frames[i].split('\n'):
				newframe += '\t'+line+'\t'+line+'\n'
			frames.append(newframe)
		frames = frames[10:]
	elif args.type == "two-oppo":
		for i in xrange(10):
			newframe = ""
			for line in frames[i].split('\n'):
				newframe += '\t'+line+'\t'+line[::-1]+'\n'
			frames.append(newframe)
		frames = frames[10:]
	elif args.type == "three":
		for i in xrange(10):
			newframe = ""
			for line in frames[i].split('\n'):
				newframe += '\t'+line+'\t'+line+'\t'+line+'\n'
			frames.append(newframe)
		frames = frames[10:]
	elif args.type == "six":
		for i in xrange(10):
			newframe = ""
			for line in frames[i].split('\n'):
				newframe += '\t'+line+'\t'+line+'\t'+line+'\n'
			frames.append(newframe+'\n'+newframe)
		frames = frames[10:]
	else:
		error("Parrot type {} does not exist".format(args.type))

	# handle color
	colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
	if args.color in colors:
		colors = [args.color]
	elif args.color == "rainbow":
		pass
	elif args.color == "ultra-rainbow":
		pass
	else:
		error("Parrot color {} does not exist".format(args.color))

	# handle time interval
	frame_time = float(args.interval)
	num_colors = len(colors)

	# implement remote master
	if args.remote is not None:
		host, port = args.remote.split(":")
		port = int(port)
		if host is None or port is None:
			error("Something wrong with remote syntax {}".format(args.remote))

		sock = None
		print "[+] Trying to connect to master parrot {}:{} ...".format(host, port)
		while sock == None:
			try:
				print "try once"
				sock = socket.create_connection((host, port))
			except:
				sleep(0.5)
				print "dab"
		print "[+] Connected !"
		sock.sendall("PARROT HELLO")
		svr_msg = ""
		while not svr_msg.endswith("!"):
			svr_msg += sock.recv(32)
		args.start_time = int(svr_msg.lstrip("LET'S PARTY AT ").rstrip("!"))
		print "Got party time {}! Waiting to begin...".format(args.start_time)
		sock.close()

	# implement start_time
	if args.start_time is not None:
		while True:
			if time() > int(args.start_time):
				break
			
	# animation loop
	frame_cnt = 0
	for frame in cycle(frames):
		frame_start = time()
		print chr(27) + "[2J"
		print handle_color(frame)
		while frame_start+frame_time > time():
			pass
		frame_cnt += 1
		frame_cnt %= num_colors
