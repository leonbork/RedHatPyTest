import os
import sys
from inspect import currentframe, getframeinfo

print("Hello World")
# Can be changed to any other folder location,
# I have used my local machine Desktop dir
current_dir = os.path.dirname('/Users/my/Desktop/RedHatPyTask/')
print('The current path is: %s' % os.curdir)
print("abspath = %s" % os.path.abspath(path='/Users/my/Desktop/RedHatPyTask/'))

frameinfo = getframeinfo(currentframe())

for item in os.listdir(current_dir):
    if not os.path.isfile(item):
        for file in os.listdir(item):
            print(frameinfo, file)

