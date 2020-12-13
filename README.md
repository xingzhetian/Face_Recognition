# Face_Recognition
Tutorial Achievement

This is a achievement of the Tutorial from https://pythonprogramming.net/facial-recognition-python/.

Facing problems:

1) .DS_Store
Error:
(base) tianxingzhedeMacBook-Pro:test denhoshiakira$ python Face_Recognition.py
Loading known faces...
Traceback (most recent call last):
  File "Face_Recognition.py", line 27, in <module>
    for filename in os.listdir(f'{known_dir}/{name}'):
NotADirectoryError: [Errno 20] Not a directory: 'known_faces/.DS_Store'
  
Reason: Mac has the .DS_Store file to store the infomation about the directory. os.listdir defaulted read the file. 

Solution: find . -name "*.DS_Store" -type f -delete
Using the command below to delete the file

2) 
Error:
objc[88722]: Class RunLoopModeTracker is implemented in both /Users/denhoshiakira/opt/anaconda3/lib/python3.7/site-packages/cv2/.dylibs/QtCore (0x119beb7f0) and /Users/denhoshiakira/opt/anaconda3/lib/libQt5Core.5.9.7.dylib (0x1207d6a80). One of the two will be used. Which one is undefined.
QObject::moveToThread: Current thread (0x7f9a937084d0) is not the object's thread (0x7f9a937b75b0).
Cannot move to target thread (0x7f9a937084d0)

Reason: Install Qt twice in Mac system. One in brew, another in conda. Uninstall one from the conda.

Solution: 
brew install qt
brew install pyqt
conda uninstall pyqt
conda uninstall qt

3)
After uninstall Qt, Error occuried:
Error: ModuleNotFoundError: No module named 'PIL'
       ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following             dependency conflicts.
        face-recognition 1.3.0 requires numpy, which is not installed.

Reason: Pillow is a library built with Qt. Pillow and numpy are uninstalled.

Solution: pip install Pillow
          pip install numpy
          
4)Low accuracy
Cannot recognize the face correctly.

Solution:

Checkpoint.....
