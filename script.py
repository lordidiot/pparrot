import sys
from time import sleep
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

for i in range(10):
    cprint(i, 'magenta', end=' ')

frames = []
for i in xrange(10):
	with open("frames/{}.txt".format(i), "r") as f:
		frames.append(f.read())


colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
for color, frame in izip(cycle(colors), cycle(frames)):
	print chr(27) + "[2J"
	if len(sys.argv) > 2:
		cprint(frame, color, sys.argv[2])
	else:
		cprint(frame, color)
	sleep(float(sys.argv[1]))
