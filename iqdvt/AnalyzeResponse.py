
###
# Module containing class (HelpResponse, derived from IqdvtCliActivator) to analyze/process the execution output
###

import sys

class AnalyzeResponse():
    def __init__(self, flags):		# optional params
        self.flags = flags

    def printAnalyzeFlags(self):
        print(f'HelpResponse, flags {self.flags}')


    def AnalyzeResponse(self, response):
        
        # help flag use-case
        if ('--help' in self.flags):
            retStatus = 'IQDVT-CLI.exe [options]' in response.stdout
            # print(f'the return status is: {retStatus}')
            return retStatus
        
        # flow flag use-case        
        if (self.flags):
            try:
                # split the Summary section from the total output:
                summarySection = response.stdout.split('Summary:')[1]
                # print(summarySection)

                # checks for 'faild' in summary section:
                return 'FAILED' not in summarySection
            except:
                error = sys.exc_info()
                print(f'AnalyzeResponse - Error {error}')
                return False
        
        # none of the above use-cases
        return False
