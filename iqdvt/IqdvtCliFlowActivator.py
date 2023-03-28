from iqdvt.IqdvtCliActivator import IqdvtCliActivator
import sys
import os
import traceback

class IqdvtCliFlowActivator(IqdvtCliActivator):

    def __init__(self, station, flow, isBinFolder, installLocation):
        # gets the station and flow relative and builds the paths for them
        self.station = os.path.join(os.getcwd(),'stations', station)
        self.flow = os.path.join(os.getcwd(),'flows', flow)

        self.flags = ['--v1',f'--station={self.station}',f'--flow={self.flow}']
        
        # passing the self.flags, isBinFolder, installLocation to the IqdvtCliActivator ctor
        super().__init__(self.flags, isBinFolder, installLocation)

    
    def Execute(self):      
        try:
            execResponse = super().ExecuteReturnOutput()
            # checks the status of execution for failed
            if(execResponse is False):
                return False

            # split the Summary section from the total output:
            summarySection = execResponse.stdout.split('Summary:')[1]
            # print(summarySection)

            # checks for 'faild' in summary section:
            return 'FAILED' not in summarySection
        
        except Exception as e:            
            print(f'IqdvtCliFlowActivator - Error:')
            traceback.print_exc()
            print(f'>> the stdout is:\n{execResponse.stdout}')
            print('-------------------')            
            return False
