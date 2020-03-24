import os
import time

currentPath = os.getcwd()

for fname in os.listdir(currentPath):                    
	m = time.strftime('%m', time.gmtime(os.path.getmtime(fname)))
	y = time.strftime('%Y', time.gmtime(os.path.getmtime(fname)))

	print(fname+": ", m, y)