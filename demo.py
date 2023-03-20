import DirCmdFramework
import FilterFiles
# from iqdvt.HelpResponse import HelpResponseFile
from iqdvt.IqdvtCliActivator import IqdvtCliActivator

# demo code:


station='C:\\LitePoint\\stations\\celeno_16_02_2023.sta'
flow='C:\\LitePoint\\flows\\txCal.flow'

ExecutableFrameworkObj = IqdvtCliActivator(['--v1',f'--station={station}',f'--flow={flow}'])
# ExecutableFrameworkObj = IqdvtCliActivator(['--help'])
# ExecutableFrameworkObj.printFlags()
# ExecutableFrameworkObj.printMe()
# ExecutableFrameworkObj.printAnalyzeFlags()
# print(f'~~ contain help flag: {ExecutableFrameworkObj.ExecuteReturnOutput()}')
print(f'~~ txCal.flow is pass: {ExecutableFrameworkObj.ExecuteReturnOutput()}')

# ExecutableFrameworkObj = HelpResponseFile.HelpResponse()
# ExecutableFrameworkObj.Execute()

# print('dir cmd output <%s>' % ExecutableFrameworkObj.ExecuteReturnOutput())

# filesListObj = FilterFiles.FilterFiles('C:\\Users\\rzolti\\Development\\Automation','*.py','*i*.py')
# filteredFileList = filesListObj.FilterFiles()
