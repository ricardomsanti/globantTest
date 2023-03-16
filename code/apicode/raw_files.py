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
    def matchFiles(self):
        matchList = []
        #iterating - by name - untill finding dataframes that can be compared
        for r in self.ref_list:
            r_name = r["name"]
            for o in self.origin_list:
                o_name = o["name"]
                #dataframe name match
                if (r_name in o_name):
                    #number of columns match
                    r_cols =[c["name"] for c in r["cols"]]
                    o_cols =[x for x in o["df"].columns]
                    matchList.append([r_name, o_name, len(r_cols), len(o_cols)])                                      
                    break
                else:
                    continue
        matchListDf = pd.DataFrame(matchList, columns=["REFERENCE_NAME", "ORIGIN_NAME", "NO_COLS_REF", "NO_COLS_ORIGIN"])
        return matchListDf


    
rf = RawFiles()
rf.originFiles()
m = rf.matchFiles()
print(m)