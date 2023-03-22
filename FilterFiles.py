###
### Module containing class (FilterFiles) to extract chosen files inside a given directory
###

import ListDir

class FilterFiles(ListDir.ListDir):
    # def __init__(self,folder,srcGroup,targetGroup):
    def __init__(self,folder,srcGroup):
        super().__init__(folder,srcGroup)
        self.srcGroup = srcGroup
        # self.targetGroup = targetGroup
		
    def Execute(self):
        listOfFiles = super().ListDir()
        # print('\nList of files found (filter %s):' % self.srcGroup)
        # for element in listOfFiles:
        #     print(element)

        # listOfFiles = super().ListDir(self.targetGroup)
        # print('\n\nList of filtered files found (filter %s):' % self.targetGroup)
        # for element in listOfFiles:
        #     print(element)

        return listOfFiles
		
