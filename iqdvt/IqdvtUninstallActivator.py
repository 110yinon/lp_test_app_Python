from ExecutableActivator import ExecutableActivator
import os
import time


class IqdvtUninstallActivator(ExecutableActivator):
    
    def __init__(self, installLocation):
        self.execArgs = [f'{installLocation}\\uninst.exe', '/S']
        super().__init__(self.execArgs)
        self.installLocation = installLocation

    
    def Execute(self):
        
        # checks if the iqdvt installation folder is exist
        if (not os.path.isdir(self.installLocation)):
            # print('the installation folder does not exist !') # tbd - work via logger
            return False
        
        # calling the uninstall and checks it's success:
        res = super().ExecuteReturnOutput()
        # print(res)
        # if uninst.exe fail - return false
        if(res is False): 
                return False
        

        time.sleep(1)

        # checks if the iqdvt installation folder been removed
        isIqdvFolderRemoved = not os.path.isdir(self.installLocation)
        # print(isIqdvFolderRemoved) # tbd - work via logger
        return isIqdvFolderRemoved

    def Verify():
        return True
