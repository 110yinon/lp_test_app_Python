import DirCmdFramework
import FilterFiles
# from iqdvt.HelpResponse import HelpResponseFile
# from iqdvt.IqdvtCliActivator import IqdvtCliActivator
from iqdvt.IqdvtCliHelpActivator import IqdvtCliHelpActivator
from iqdvt.IqdvtCliFlowActivator import IqdvtCliFlowActivator
from iqdvt.IqdvtInstallActivator import IqdvtInstallActivator
from iqdvt.IqdvtUninstallActivator import IqdvtUninstallActivator
import json
# from config import configJSONFile

# demo code:
with open('./config/installationFile.json', 'r') as installationJSONFile:
    installationFile = json.load(installationJSONFile)['installationFile']
    # print(installationFile)

with open('./config/config.runner.json', 'r') as configJSONFile:
    configObject = json.load(configJSONFile)
    # print(configObject['tests'])

isBinFolder = configObject['isBinFolder']

# tbd - allow relative path from the json config !!!!!
# determines the installLocation value from the json config file
installLocation = configObject['installLocation'] if 'installLocation' in configObject.keys() else 'C:\\IQDVT_TEST_PYTHON\\'

# station = 'C:\\LitePoint\\stations\\celeno_16_02_2023.sta'
# flow = 'C:\\LitePoint\\flows\\txCal.flow'

# installationFile = 'C:\\Users\\ybarhum\\Downloads\\IQDVT-CL_8XXX_1.0.9_x64 uninst broken.exe'
# installationFile = 'C:\\Users\\ybarhum\\Desktop\\lp_test_app\\executions\\IQDVT-Celeno-6XXX_1.1.2_Eng1_x64.exe'
# installLocation = 'C:\\IQDVT_TEST_PYTHON\\'
# isBinFolder = False
# filesToVerify = ['IQTest.dll', 'IQTestAPI.dll', 'IQDVT.exe', 'IQDVT-CLI.exe', 'exports.txt']

try:
    for test in configObject['tests']:
         
            if test['command'] == 'install':
                installationObject = IqdvtInstallActivator(installationFile, test['filesToVerify'], isBinFolder, installLocation)
                result  = installationObject.Execute() is test['expectPass']
                print(f'~~ installation pass: {result}')
                
                if result is False:
                    raise Exception('installation test failed')

            elif test['command'] == 'uninstall':
                uninstallObject = IqdvtUninstallActivator(installLocation)
                result = uninstallObject.Execute() is test['expectPass']
                print(f'~~ uninstallation pass: {result}')
                # tbd - break/return in case of uninstall failed ??
                # tbd- return to install automatically ??

            elif test['command'] == 'help':
                helpCliObject = IqdvtCliHelpActivator(isBinFolder, installLocation)
                result = helpCliObject.Execute() is test['expectPass']
                print(f'~~ cli contain help flag: {result}')
            

            elif test['command'] == 'cli':                
                flowCliObject = IqdvtCliFlowActivator(test['station'],test['flow'], isBinFolder, installLocation)
                # checks for iterate option
                iterates = test['iterates'] if 'iterates' in test.keys() else 1
                
                # runs the flow in iterates
                for iterate in range(iterates):
                    result = flowCliObject.Execute() is test['expectPass']
                    # print(f'~~ your flow name is pass: {result}')

                    # an improved log to the user
                    flowName = test['flow'].split('\\')[1]
                    passOrFailed = 'Pass' if test['expectPass'] else 'Failed'
                    iterateSign = f' (iterate-{iterate})' if iterates > 1 else ''
                    print(f'~~ {flowName} to {passOrFailed}{iterateSign}: {result}')



except Exception as e:
    print('demo.py - Error:',{e},'\nCanceling test suite, Bye Bye...','\n--------------')



# installationObject = IqdvtInstallActivator(installationFile, installLocation, filesToVerify ,isBinFolder)
# print(f'~~ installation pass: {installationObject.Execute()}')

# uninstallObject = IqdvtUninstallActivator(installLocation)
# print(f'~~ uninstallation pass: {uninstallObject.Execute()}')


# ExecutableFrameworkObj = IqdvtCliHelpActivator();
# print(f'~~ contain help flag: {ExecutableFrameworkObj.ExecuteReturnOutput()}')

# ExecutableFrameworkObj = IqdvtCliFlowActivator(station, flow)
# print(f'~~ txCal.flow to pass: {ExecutableFrameworkObj.ExecuteReturnOutput()}')

# ExecutableFrameworkObj = IqdvtCliActivator(['--v1',f'--station={station}',f'--flow={flow}'])
# ExecutableFrameworkObj = IqdvtCliActivator(['--help'])
# ExecutableFrameworkObj.printFlags()
# ExecutableFrameworkObj.printMe()
# ExecutableFrameworkObj.printAnalyzeFlags()
# print(f'~~ contain help flag: {ExecutableFrameworkObj.ExecuteReturnOutput()}')
# print(f'~~ txCal.flow is pass: {ExecutableFrameworkObj.ExecuteReturnOutput()}')

# ExecutableFrameworkObj = HelpResponseFile.HelpResponse()
# ExecutableFrameworkObj.Execute()

# print('dir cmd output <%s>' % ExecutableFrameworkObj.ExecuteReturnOutput())

# filesListObj = FilterFiles.FilterFiles('C:\\Users\\rzolti\\Development\\Automation','*.py','*i*.py')
# filteredFileList = filesListObj.FilterFiles()
