from ExecutableActivator import ExecutableActivator
from FilterFiles import FilterFiles
import traceback

# tbd - use abstract class that dervived from ExecutableActivator
class IqdvtInstallActivator(ExecutableActivator):
    def __init__(self, installationFile, filesToVerify, isBinFolder, installLocation):
        
        self.execArgs = [installationFile, '/S', f'/D={installLocation}']

        super().__init__(self.execArgs)

        self.installationFile = installationFile
        self.installationFiles2Verify = filesToVerify

        # attaching Bin folder to the installation location if exist
        self.installLocation = f"{installLocation}{'Bin' if isBinFolder else ''}"
        # passing the installation location to FilterFiles
        self.filterFilesObj = FilterFiles(self.installLocation, '*')

    def Execute(self):
        # calling the ExecutableActivator for installing the iqdvt program
        try:            
            res = super().ExecuteReturnOutput()
            # print(res)

            # if instal.exe fail - return false
            if(res is False): 
                 return False
            

            # extract list of files from the installation folder (usually 'C:\\IQDVT_TEST_PYTHON')
            listFiles = self.filterFilesObj.Execute()
            # check if the verify files was installed
            isFileIncludes = all(item in listFiles for item in self.installationFiles2Verify)
            # print(isFileIncludes) # tbd - work via logger

            return isFileIncludes 


        except Exception as e:
                print(f'IqdvtInstallActivator - Error:')
                # print(e)
                # traceback.print_exception(e)
                traceback.print_exc()
                print('-------------------')
                # print(f'IqdvtInstallActivator - Error:\n{e}')
                return False
        



    def Verify(self):
        return True
