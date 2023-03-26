from iqdvt.IqdvtCliActivator import IqdvtCliActivator


class IqdvtCliHelpActivator(IqdvtCliActivator):

    def __init__(self, isBinFolder, installLocation):
        self.flags = ['--help']
        super().__init__(self.flags, isBinFolder, installLocation) # passing the self.flags to the IqdvtCliActivator ctor


    def Execute(self):
        # calling the 'iqdvt-cli.exe --help'
        execResponse = super().ExecuteReturnOutput()
        
        # checks the status of execution for failed
        if(execResponse is False): 
            return False

        # execuation done - checks for the help section in response's stdout
        retStatus = 'IQDVT-CLI.exe [options]' in execResponse.stdout
        # print(f'the return status is: {retStatus}')
        return retStatus
    
        
