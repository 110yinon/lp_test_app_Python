from iqdvt.IqdvtCliActivator import IqdvtCliActivator
import sys

class IqdvtCliFlowActivator(IqdvtCliActivator):

    def __init__(self, station, flow):
        self.flags = ['--v1',f'--station={station}',f'--flow={flow}']
        super().__init__(self.flags)  # passing the self.flags to the IqdvtCliActivator ctor

    
    def ExecuteReturnOutput(self):
        execResponse = super().ExecuteReturnOutput()
        try:
            # split the Summary section from the total output:
            summarySection = execResponse.stdout.split('Summary:')[1]
            # print(summarySection)

            # checks for 'faild' in summary section:
            return 'FAILED' not in summarySection
        
        except:
            error = sys.exc_info()
            print(f'AnalyzeResponse - Error {error}')
            return False
