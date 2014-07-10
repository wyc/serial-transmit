#!/usr/bin/python

import os
import time
from sys import argv
from pydub import AudioSegment

sound = AudioSegment.from_mp3(argv[1])
step = 5000
for i in range(0, int(len(sound) / step)):
    segment = sound[i*step:(i+1)*step]
    d = os.path.dirname(os.path.realpath(argv[1])) 
    f = "audio%05d.mp3" % (i) 
    path = "%s/%s" % (d, f)
    segment.export(path, format="mp3")
    print("writing to %s" % (path))
    os.system("./pysend.py %s" % (path))
    os.remove(path)
    time.sleep(0.3)

