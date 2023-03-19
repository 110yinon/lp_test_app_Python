###
### Module containing class (DirCmdFramework, derived from ExecutableActivtor) to activate a specific cmd ('dir') and process it's output
###

import ExecutableActivator

class DirCmdFramework(ExecutableActivator.ExecutableActivator):
    def __init__(self):		# optional params
        super().__init__('dir')
	
    def AnalyzeResponse(self,response):
        pass
	
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
		
