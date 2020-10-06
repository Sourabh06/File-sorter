import os
import re

import shutil
# import time

rex = re.compile(r'''
(^IMG|^VID)		#file type
(.*?)
(
(\d{4})			#year
(\d{2})			#month
(\d{2})			#date
)
(.*?)
''', re.VERBOSE)

currentPath = os.getcwd()

for fname in os.listdir(currentPath):                    
# 	m = time.strftime('%m', time.gmtime(os.path.getctime(fname)))
# 	y = time.strftime('%Y', time.gmtime(os.path.getctime(fname)))

    name, ext = os.path.splitext(fname) 

# Check extension
    if ext[1:] == '' or ext[1:] == 'py': 
        continue

    names = []
    types = []
    year = []
    month = []
    day = []
    match = re.search(rex,fname)
    if(match):
        types.append(match.group(1))	#name
        year.append(match.group(4))		#type
        month.append(match.group(5))	#year
        day.append(match.group(6))		#month
        names.append(match.group(0))	#day

    print(names, types, year, month, day)

    temp_path = currentPath+"\\"+year[len(year)-1]+"\\"+month[len(month)-1]

    if os.path.exists(temp_path):
        shutil.move(currentPath+'\\'+fname, temp_path+'\\'+fname) 
    # Create new directory 
    else:
        try:
            os.makedirs(temp_path)
            shutil.move(currentPath+'\\'+fname, temp_path+'\\'+fname)
        except OSError:
            print("Creation of directory %s failed" %temp_path) 

print("Sorted successfully")