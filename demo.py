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

# with open('./config/config.runner.json','r') as configJSONFile:
#     kuni = json.load(configJSONFile)
#     print(kuni)

# station = 'C:\\LitePoint\\stations\\celeno_16_02_2023.sta'
# flow = 'C:\\LitePoint\\flows\\txCal.flow'

# installationFile = 'C:\\Users\\ybarhum\\Downloads\\IQDVT-CL_8XXX_1.0.9_x64 uninst broken.exe'
installationFile = 'C:\\Users\\ybarhum\\Desktop\\lp_test_app\\executions\\IQDVT-Celeno-6XXX_1.1.2_Eng1_x64.exe'
installLocation = 'C:\\IQDVT_TEST_PYTHON\\'
isBinFolder = False
filesToVerify = ['IQTest.dll', 'IQTestAPI.dll', 'IQDVT.exe', 'IQDVT-CLI.exe', 'exports.txt']

installationObject = IqdvtInstallActivator(installationFile, installLocation, filesToVerify ,isBinFolder)
print(f'~~ installation pass: {installationObject.Execute()}')

uninstallObject = IqdvtUninstallActivator(installLocation)
print(f'~~ uninstallation pass: {uninstallObject.Execute()}')



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
