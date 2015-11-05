import json
import sys
import glob
import os


spec= json.loads(open('package.json').read())

for pat in spec[sys.argv[1]]:
	for file in glob.glob(pat[0]):
		dst = pat[1] + '/' + os.path.basename(file)
		print os.path.basename(file) + " -> " + dst

