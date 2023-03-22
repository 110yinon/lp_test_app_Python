###
# Module containing class (DExecutableActivtor) to activate an arbitrary cmd and retrieve it's output
###

import subprocess
# from iqdvt.AnalyzeResponse import AnalyzeResponse

class ExecutableActivator():
    def __init__(self, execArgs, cwd=None):
    # def __init__(self, iqdvtCli, flags, cwd):
        # print('CTOR ExecutableActivator')
        # super().__init__(flags)        
        self.execCommand = execArgs
        self.currentWorkingDir = cwd
        
    # def __init__(self, cmd):
        # self.cmdStruct = "%s" % cmd
        # self.cmd = cmd

    def printMe(self):
        print(
            f'ExecutableActivator, execCommand: {self.execCommand}')

    def Execute(self):
        try:
            result = subprocess.run(
                self.execCommand, shell=True, capture_output=True, text=True, cwd=self.currentWorkingDir)
            
            return result
        
        except:
            print('Error')
            return False
        

    def ExecuteReturnOutput(self):
        execResponse = self.Execute()
        # print(f'{execResponse}')
        return execResponse

    async def AsyncExecute(self):
        return self.Execute()

    async def AsyncExecuteReturnOutput(self):
        return await self.AsyncExecute()
