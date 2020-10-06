import os
import time
import shutil
import numpy

currentPath = os.getcwd()

for fname in os.listdir(currentPath):                    
	m = time.strftime('%m', time.gmtime(os.path.getmtime(fname)))
	y = time.strftime('%Y', time.gmtime(os.path.getmtime(fname)))
	temp_path = currentPath+"\\"+y+"\\"+m

	name, ext = os.path.splitext(fname) 
  
    # Check extension
	if ext[1:] == '' or ext[1:] == 'py': 
		continue

	if os.path.exists(temp_path): 
		shutil.move(currentPath+'\\'+fname, temp_path+'\\'+fname) 
    # Create new directory 
	else:
		try:
			os.makedirs(temp_path)
			shutil.move(currentPath+'\\'+fname, temp_path+'\\'+fname)
		except OSError:
			print("Creation of directory %s failed" %temp_path) 

print("File Sorted successfully")
