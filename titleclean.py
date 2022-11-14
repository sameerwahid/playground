##################################################################
## titleclean.py
##
## PY script: remove DSS FWHM line from spectrum title
##  
## SW	20221006	file created 
##################################################################
import re, sys

#define dataset and filenames
curdat=CURDATA()
titleLocation=curdat[3]+"/"+curdat[0]+"/"+curdat[1]+"/pdata/"+curdat[2]+"/title"
#shimLocation=curdat[3]+"/"+curdat[0]+"/"+curdat[1]+"/shimvalues"


# check to see if title has an old result - if yes, delete it
# (use try to avoid errors if the file does not exist)
try:
	f = open(titleLocation, 'r')
	titleLines=f.readlines() 
	if re.match("DSS FWHM.*",titleLines[-1]):
		f.close()
		f = open(titleLocation, 'w')
		f.writelines([item for item in titleLines[:-1]])  #short way to write all lines but the last (-1)
	f.close()
except:
	pass

#f.close()
