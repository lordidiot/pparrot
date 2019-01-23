import sys
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

frame_time = float(sys.argv[1])
if len(sys.argv) > 2:
	start_time = int(sys.argv[2])
if len(sys.argv) > 3:
	order = int(sys.argv[3])
else:
	order = 0

frames = []
for i in xrange(10):
	with open("frames/{}.txt".format(i), "r") as f:
		frames.append(f.read())
for i in xrange(10):
	for line in frames[i].split('\n'):
		frames.append('\t'+line+'\t'+line+'\t'+line)
frames = frames[10:]

while True:
	if time() > start_time+(order*(frame_time/3.0)):
		break

out = ""
colors = ["red", "red", "red", "green", "green", "green", "yellow", "yellow", "yellow", "blue", "blue", "blue", "magenta", "magenta", "magenta", "cyan", "cyan", "cyan"]
for color, frame in izip(cycle(colors), cycle(frames)):
	if frame == '\t'*3:
		print out+'\n\n'+out+'\n\n'
		sleep(frame_time)
		print chr(27) + "[2J"
		out = ""
	else:
		out += colored(frame, color)+'\n'
