import json
import sys
import glob
import os
import shutil
import zipfile
import subprocess


spec= json.loads(open('package.json').read())

if (len(sys.argv) < 4 or not sys.argv[1]):
	exit(-1)

package = sys.argv[2] 
version = sys.argv[3]

zipname = sys.argv[1] + '.zip'
zf = zipfile.ZipFile(zipname, "w")

for pat in spec[sys.argv[1]]:
	for file in glob.glob(pat[0]):
		dst = pat[1] + '/' + os.path.basename(file)
		print file + " -> " + dst
		# dstdir = os.path.dirname(dst)
		# if (not os.path.exists(dstdir)):
		# 	os.makedirs(dstdir)
		# shutil.copy(file,dst)
		zf.write(file,dst)


vars = [
	'curl',
	'-X',
	'PUT',
	'-H',
	'Content-Type: application/octet-stream',
	'--data-binary',
	'@' + zipname,
	'http://a1.ayxia.com:8881/post/%s/%s/%s' % (package,version,zipname)
	]

print vars

subprocess.call(vars, shell=True)
