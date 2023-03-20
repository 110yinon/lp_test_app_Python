
###
# Module containing class (HelpResponse, derived from IqdvtCliActivator) to analyze/process the execution output
###

# from IqdvtCliActivator import IqdvtCliActivator

class HelpResponse():
    def __init__(self, flags):		# optional params
        self.flags = flags

    def printHelpFlags(self):
        print(f'HelpResponse, flags {self.flags}')

    def AnalyzeResponse(self, response):
        if ('--help' in self.flags):
            retStatus = 'IQDVT-CLI.exe [options]' in response.stdout
            # print(f'the return status is: {retStatus}')
            return retStatus
