###
# Module containing class (IqdvtCliActivator, derived from ExecutableActivtor) to activate IQDVT-CLI.exe with a specific flag
###

from ExecutableActivator import ExecutableActivator


class IqdvtCliActivator(ExecutableActivator):
    def __init__(self, flags):
        print('CTOR IqdvtCliActivator')		# optional params
        self.iqdvtCli = 'C:\\IQDVT_TEST\\Bin\\IQDVT-CLI.exe'
        super().__init__(self.iqdvtCli, flags)
        self.flags = flags

    # def AnalyzeResponse(self,response): should be a virtual method
    #     pass

    def printFlags(self):
        print(f'IqdvtCliActivator, flags: {self.flags}')

    def Execute(self):
        return super().Execute()

    def ExecuteReturnOutput(self):
        response = super().ExecuteReturnOutput()
        self.AnalyzeResponse(response)
        return response

    async def AsyncExecute(self):
        await super().AsyncExecute()

    async def AsyncExecuteReturnOutput(self):
        response = await super().AsyncExecuteReturnOutput()
        self.AnalyzeResponse(response)
