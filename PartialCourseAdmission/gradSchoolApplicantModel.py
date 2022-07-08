# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:16:51 2020

@author: Jelly Ann Pananganan #BSIT-2B
"""

import connectionUtility
import pandas as pd
host = '127.0.0.1'
user = 'root'
password = ''
db = 'partialcourseadmission'
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.

class gradSchoolModel():
    
    def __init__(self):
        self.cnx = connectionUtility.getConnection()
        
    def extract_data_from_database(self):
        sql = ("Select id, IDNumber, LastName, FirstName, MI, DesiredCourse from tbl_gradschool")
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def read_data(self):
        sql = ("Select id from tbl_gradschool where id = (select MAX(id) from tbl_gradschool") 
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def insertStudentData(self):
        # create CSV in excel file
        infile = ('D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission/gradSchoolApplicantsInfo.csv') # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
        from sqlalchemy import create_engine
        
        df = pd.read_csv(infile,na_values = " NaN", delimiter = ',', encoding = 'latin-1')
        df['id'] = pd.read_sql_query('select ifnull(MAX(id),0)+1 from tbl_gradschool',self.cnx).iloc[0,0]+range(len(df))
        engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user,password,host,db),pool_recycle = 1,pool_timeout = 57600).connect()
        
        df.to_sql(con = engine, name = 'tbl_gradschool', if_exists = 'append', index = False, chunksize = 1)
        return

    '''def update_Data(self):
        cursor = db.cursor()
        sql = 
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        
        db.close()
        return

    def delete_Data(self):
        return'''
    
    
    def main(self):
        c = self.read_data()
        #b = self.update_Data()
        #d = self.delete_Data()
        print(c)
         
if __name__ == "__main__":
    s = gradSchoolModel()
    s.insertStudentData()

