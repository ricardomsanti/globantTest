###############################################################################
#LOCAL FILE TRANSFORMATION
###############################################################################

import pandas as pd 
import os 

class LocalWorks:
    def __init__(self, path=""):
        self.path = path
        self.local_origin = "D://GIT_CODE//GLOBANT//globantTest//01 - basic_files"
        self.local_files = [ str(f.path) for f in os.scandir(self.local_origin) if ".xls" in str(f.name)]


lo = LocalWorks()
for x in lo.local_files:
    print(x)