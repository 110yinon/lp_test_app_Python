###
### Module containing class (SwitchToDir) to extract list-of-files in a given directory
###

import os

class SwitchToDir():
    def __init__(self):	
        self.storedFolder = None #place holder

    def Change2Dirctory(self,newFolder):
        self.storedFolder = os.getcwd()
        os.chdir(newFolder)
		
    def Push(self,newFolder):
        self.Change2Dirctory(newFolder)
		
    def Pop(self):
        assert(self.storedFolder != None)#, 'SwitchToDir error. Invalid Pop. self.storedFolder == None')
        self.Change2Dirctory(self.storedFolder)
		
        self.storedFolder = None #clear stored folder
		
		
