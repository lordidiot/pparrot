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

while True:
	if time() > start_time+(order*(frame_time/3.0)):
		break

colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
for color, frame in izip(cycle(colors), cycle(frames)):
	print chr(27) + "[2J"
	cprint(frame, color)
	sleep(frame_time)
