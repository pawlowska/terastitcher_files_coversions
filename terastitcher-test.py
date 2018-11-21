# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:41:58 2018

@author: MPawlowska
"""

import subprocess
import sys

dataDir=r'"D:\usuwanie_tla\test_pythona\imageSeries"'
terastitcher="C:/TeraStitcher-portable-1.11.6-win64/terastitcher.exe"

volin = " --volin="+dataDir
params=" --ref1=-X --ref2=Y --ref3=Z --vxl1=1.45 --vxl2=1.45 --vxl3=10"

#process = subprocess.Popen([terastitcher, "--help"], stdout=subprocess.PIPE)
process = subprocess.Popen([terastitcher, "--test"+ volin+ params], stdout=subprocess.PIPE)

for line in iter(process.stdout.readline, b''):  # replace '' with b'' for Python 3
    sys.stdout.write(line)
