###
# Module containing class (DExecutableActivtor) to activate an arbitrary cmd and retrieve it's output
###

import subprocess
from iqdvt.HelpResponse import HelpResponse

class ExecutableActivator(HelpResponse):
    def __init__(self, iqdvtCli, flags):
        print('CTOR ExecutableActivator')		# optional params
        super().__init__(flags)        
        self.execCommand = [iqdvtCli] + flags

    # def __init__(self, cmd):
        # self.cmdStruct = "%s" % cmd
        # self.cmd = cmd

    def printMe(self):
        print(
            f'ExecutableActivator, flags: {self.flags}, execCommand: {self.execCommand}')

    def Execute(self):
        try:
            result = subprocess.run(
                self.execCommand, shell=True, capture_output=True, text=True)
            return result
        
        except:
            print('Error')
            return False
        

    def ExecuteReturnOutput(self):
        execResponse = self.Execute()
        retStatus = self.AnalyzeResponse(execResponse)
        return retStatus

    async def AsyncExecute(self):
        return self.Execute()

    async def AsyncExecuteReturnOutput(self):
        return await self.AsyncExecute()
