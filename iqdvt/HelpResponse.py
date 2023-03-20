
###
### Module containing class (HelpResponse, derived from IqdvtCliActivator) to analyze/process the execution output
###

# from IqdvtCliActivator import IqdvtCliActivator

class HelpResponse():
    def __init__(self):		# optional params
        super().__init__()
	
    def AnalyzeResponse(self,response):
        retStatus = 'IQDVT-CLI.exe [options]' in response.stdout
        return retStatus
    
		
