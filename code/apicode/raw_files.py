###############################################################################
#LOCAL FILE TRANSFORMATION
###############################################################################

import pandas as pd 
import os 
import reference_files as ref


class RawFiles:
    def __init__(self):
        self.local_origin = "D://GIT_CODE//GLOBANT//globantTest//01-origin"
        self.ref_list = [ref.departments, ref.hired_employees, ref.jobs]
        self.origin_list = []

    def originFiles(self):    
        name = ""
        df = ""
        file_dict = {}
        for file in os.scandir(self.local_origin):
            name = file.name
            df = pd.read_excel(file.path)
            file_dict = {
                            "name": name,
                            "df":df
                        }
            self.origin_list.append(file_dict)

    #So far we gathered all the info about the reference files and the ones in the origin directory so we could
    # compare them and perform some validation in terms of the file's names, and the number of columns  
        
    
rf = RawFiles()
