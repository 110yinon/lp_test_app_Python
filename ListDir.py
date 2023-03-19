###
### Module containing class (ListDir) to extract list-of-files in a given directory
###

import glob

import SwitchToDir

class ListDir():
    def __init__(self,folder,fileMask):	
        self.folder = folder
        self.fileMask = fileMask
        self.switchToDirObj = SwitchToDir.SwitchToDir()
		
    def ListDir(self,fineTunedFileMask = None):
        self.switchToDirObj.Push(self.folder)
        if (fineTunedFileMask == None):
            fileList = glob.glob(self.fileMask)
        else:	
            fileList = glob.glob(fineTunedFileMask)	#TBD This is not a real-cascading as meant to be
        self.switchToDirObj.Pop()
        return fileList
		
