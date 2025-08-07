# import os
# root_dir = "C:\workspace\learning\lmn_tools"

# list = os.walk(root_dir)
# print(list)


## using os.walk, that showing all the 

#Import os Library
# import os

# #Travers all the branch of a specified path
# def getDirectory(apaLhoo):
#     for (root,dirs,files) in os.walk('C:\workspace\learning\lmn_tools',topdown=True):
        
#         return get
    
# get = getDirectory(3)
# print(get)

import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('C:\workspace\learning\lmn_tools', topdown=True):
        print (root)
        # print (dirs)
        # print (files)
        # print ('--------------------------------')