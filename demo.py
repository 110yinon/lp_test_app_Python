import DirCmdFramework
import FilterFiles

#demo code:		
		
ExecutableFrameworkObj = DirCmdFramework.DirCmdFramework()		
# ExecutableFrameworkObj.Execute()

print('dir cmd output <%s>' % ExecutableFrameworkObj.ExecuteReturnOutput())

# filesListObj = FilterFiles.FilterFiles('C:\\Users\\rzolti\\Development\\Automation','*.py','*i*.py')
# filteredFileList = filesListObj.FilterFiles()

