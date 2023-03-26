###
# Module containing class (IqdvtCliActivator, derived from ExecutableActivtor) to activate IQDVT-CLI.exe with a specific flag
###

from ExecutableActivator import ExecutableActivator


class IqdvtCliActivator(ExecutableActivator):
    
    def __init__(self, flags, isBinFolder, installLocation):
        # print('CTOR IqdvtCliActivator')

        self.iqdvtCli = f"{installLocation}{'Bin' if isBinFolder else ''}\\IQDVT-CLI.exe"
        self.currentWorkingDir = self.iqdvtCli.split('IQDVT-CLI.exe')[0]
        
        self.execArgs = [self.iqdvtCli] + flags

        super().__init__(self.execArgs, self.currentWorkingDir) # passing the args to be execute to ExecutableActivator ctor
        # super().__init__(self.iqdvtCli, self.currentWorkingDir, flags) # passing the iqdvtCli, currentWorkingDir and flags to ExecutableActivator ctor
        
        # self.flags = flags        
    

    # def printFlags(self):
    #     # print(f'IqdvtCliActivator, currentWorkingDir: {self.currentWorkingDir}')
    #     print(f'IqdvtCliActivator, flags: {self.flags}')

    def Execute(self):
        return super().Execute()

    def ExecuteReturnOutput(self):
        execResponse = super().ExecuteReturnOutput()
        # tbd - set here the checks for false result and raise exeception if necessary
        # print(f'{execResponse.stdout}')
        return execResponse

    async def AsyncExecute(self):
        await super().AsyncExecute()

    async def AsyncExecuteReturnOutput(self):
        response = await super().AsyncExecuteReturnOutput()
        self.AnalyzeResponse(response)
