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
        
        # calling the uninstall
        super().Execute()

        time.sleep(1)

        # checks if the iqdvt installation folder been removed
        isIqdvFolderRemoved = not os.path.isdir(self.installLocation)
        # print(isIqdvFolderRemoved)
        return isIqdvFolderRemoved

    def Verify():
        return True
