from ExecutableActivator import ExecutableActivator
from FilterFiles import FilterFiles


class IqdvtInstallActivator(ExecutableActivator): # tbd - use abstract class that dervived from ExecutableActivator
    def __init__(self, installationFile, installLocation, filesToVerify ,isBinFolder):
        
        self.execArgs = [installationFile, '/S', f'/D={installLocation}']
        
        super().__init__(self.execArgs)

        self.installationFile = installationFile        
        self.installationFiles2Verify = filesToVerify
        
        # attaching Bin folder to the installation location if exist
        self.installLocation = f"{installLocation}{'Bin' if isBinFolder else ''}"
        self.filterFilesObj = FilterFiles(self.installLocation, '*')

    
    def Execute(self):
        # calling the ExecutableActivator for installing the iqdvt program
        super().Execute()

        # extract list of files from the installation folder (C:\\IQDVT_TEST_PYTHON)
        listFiles = self.filterFilesObj.FilterFiles()
        # check if the verify files was installed
        isFileIncludes = all(item in listFiles for item in self.installationFiles2Verify)
        # print(isFileIncludes) # tbd - work via logger
        
        return isFileIncludes

    
    def Verify(self):
        return True
