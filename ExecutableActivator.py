###
# Module containing class (DExecutableActivtor) to activate an arbitrary cmd and retrieve it's output
###

import subprocess
import sys
import traceback
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
        print(f'ExecutableActivator, execCommand: {self.execCommand}')


    def Execute(self):
        try:
            result = subprocess.run(
                self.execCommand, shell=True, capture_output=True, text=True, cwd=self.currentWorkingDir)
            
            # this check is indeed, else - subprocess.run stil doesnt throw execption even if returnCode isnt 0
            # if check=True would select in subprocess.run - the method throw just CalledProcessError exception
            # with no extra info from the stderr's subprocess.run
            if(result.returncode > 0):
                raise Exception(result)
            
            # exec done successfully, return True/False
            return result
        
        except Exception as e:
                print(f'ExecutableActivator - Error:')
                traceback.print_exc()
                print('------------------------------')
                return False
        

    def ExecuteReturnOutput(self):
        execResponse = ExecutableActivator.Execute(self) # replaced with self.Execute() that cause initfite loop
        # print(f'the exec response is: {execResponse}') # containts the stdout & stderr if needed
        return execResponse

    async def AsyncExecute(self):
        return self.Execute()

    async def AsyncExecuteReturnOutput(self):
        return await self.AsyncExecute()
