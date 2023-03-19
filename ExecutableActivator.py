###
### Module containing class (DExecutableActivtor) to activate an arbitrary cmd and retrieve it's output
###

import subprocess

class ExecutableActivator():
    def __init__(self,cmd):		# optional params
        self.cmdStruct = "%s" % cmd	
	
    def Execute(self):
        result = subprocess.run([self.cmdStruct], shell=True, capture_output=True, text=True)
        return result.stdout

    def ExecuteReturnOutput(self):
        return self.Execute()
		
    async def AsyncExecute(self):
        return self.Execute()
        
    async def AsyncExecuteReturnOutput(self):
        return await self.AsyncExecute()
		
