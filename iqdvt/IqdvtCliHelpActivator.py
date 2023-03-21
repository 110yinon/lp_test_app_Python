from iqdvt.IqdvtCliActivator import IqdvtCliActivator


class IqdvtCliHelpActivator(IqdvtCliActivator):

    def __init__(self):
        self.flags = ['-- help']
        super().__init__(self.flags) # passing the self.flags to the IqdvtCliActivator ctor


    def ExecuteReturnOutput(self):

        execResponse = super().ExecuteReturnOutput()

        if ('--help' in self.flags):
            retStatus = 'IQDVT-CLI.exe [options]' in execResponse.stdout
            # print(f'the return status is: {retStatus}')
            return retStatus

        return False
    
        
