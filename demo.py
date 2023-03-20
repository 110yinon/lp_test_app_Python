import DirCmdFramework
import FilterFiles
# from iqdvt.HelpResponse import HelpResponseFile
from iqdvt.IqdvtCliActivator import IqdvtCliActivator

# demo code:

ExecutableFrameworkObj = IqdvtCliActivator(['--help'])
# ExecutableFrameworkObj.printFlags()
# ExecutableFrameworkObj.printMe()
# ExecutableFrameworkObj.printHelpFlags()
print(f'~~ contain help flag: {ExecutableFrameworkObj.ExecuteReturnOutput()}')

# ExecutableFrameworkObj = HelpResponseFile.HelpResponse()
# ExecutableFrameworkObj.Execute()

# print('dir cmd output <%s>' % ExecutableFrameworkObj.ExecuteReturnOutput())

# filesListObj = FilterFiles.FilterFiles('C:\\Users\\rzolti\\Development\\Automation','*.py','*i*.py')
# filteredFileList = filesListObj.FilterFiles()
