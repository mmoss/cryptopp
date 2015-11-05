import json
import sys
import glob
import os
import shutil
import zipfile


spec= json.loads(open('package.json').read())

if (len(sys.argv) < 2 or not sys.argv[1]):
	exit(-1)

zf = zipfile.ZipFile(sys.argv[1] + ".zip", "w")

for pat in spec[sys.argv[1]]:
	for file in glob.glob(pat[0]):
		dst = pat[1] + '/' + os.path.basename(file)
		print file + " -> " + dst
		# dstdir = os.path.dirname(dst)
		# if (not os.path.exists(dstdir)):
		# 	os.makedirs(dstdir)
		# shutil.copy(file,dst)
		zf.write(file,dst)


