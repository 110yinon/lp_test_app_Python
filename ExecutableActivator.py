###
# Module containing class (DExecutableActivtor) to activate an arbitrary cmd and retrieve it's output
###

import subprocess


class ExecutableActivator():
    def __init__(self, iqdvtCli, flags):
        print('CTOR ExecutableActivator')		# optional params
        self.execCommand = [iqdvtCli] + flags

    # def __init__(self, cmd):
        # self.cmdStruct = "%s" % cmd
        # self.cmd = cmd

    def printMe(self):
        print(f'ExecutableActivator, flags: {self.flags}, execCommand: {self.execCommand}')

    def Execute(self):
        try:
            result = subprocess.run(
                self.execCommand, shell=True, capture_output=True, text=True)
        except:
            print('Error')
            retStatus = False
        return retStatus

    def ExecuteReturnOutput(self):
        return self.Execute()

    async def AsyncExecute(self):
        return self.Execute()

    async def AsyncExecuteReturnOutput(self):
        return await self.AsyncExecute()
