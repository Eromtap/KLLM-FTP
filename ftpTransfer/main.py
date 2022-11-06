#! /home/markpatmore/QuestPrograms/QuestEnv/bin/python3


"""
Created on Sat Sep 10 20:15:05 2022

@author: Mark Patmore FMDJP

"""

import logging
import sys
from datetime import datetime
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")

import xlsx_to_ods as xl

from definitions import ROOT_DIR

# from TK_imports import tkImport

platform = sys.platform




def main():
    
    
    
    
    
    
    now = datetime.now()
    now = str(now)
    
    
    ## Check for platform and format file paths accordingly
    
    if platform == 'linux':
    
        logging.basicConfig(filename=f'{ROOT_DIR}/logging.log',
                        level=logging.ERROR,
                        filemode='w',
                        force=True)   
        
        
        try:
            
            xl.collect_xlsx_data(f'{ROOT_DIR}/temp/Tractor Hub Report - notification.xlsx',3,2,'2',5,3,4,today)
            
            xl.collect_stupid_TK_data(f'{ROOT_DIR}/temp/tk_hrs.xlsx', 5, 1,'R',5,11,today)        
               
            xl.collect_xlsx_data(f'{ROOT_DIR}/temp/Reefer Hours Report - notification.xlsx', 3, 2,'R',5,3,4,today)   
             
        except Exception as Argument:
            logging.error(str(Argument) + '\n' + now)
            logging.shutdown()
            sys.exit()
            
            
        xl.create_combined_ODS(f'{ROOT_DIR}/temp/Expedited_Meter_Import.ods')
            
        logging.shutdown()
        
    else:
        
        logging.basicConfig(filename=f'{ROOT_DIR}\\logging.log',
                        level=logging.ERROR,
                        filemode='w',
                        force=True)   
        
        
        try:
            
            xl.collect_xlsx_data(f'{ROOT_DIR}\\temp\\Tractor Hub Report - notification.xlsx',3,2,'2',5,3,4,today)
            
            xl.collect_stupid_TK_data(f'{ROOT_DIR}\\temp\\tk_hrs.xlsx', 5, 1,'R',4,11, today)        
               
            xl.collect_xlsx_data(f'{ROOT_DIR}\\temp\\Reefer Hours Report - notification.xlsx', 3,2,'R',5,3,4,today)   
             
        except Exception as Argument:
            logging.error(str(Argument) + '\n' + now)
            logging.shutdown()
            sys.exit()
            
            
        xl.create_combined_ODS(f'{ROOT_DIR}\\temp\\Expedited_Meter_Import.ods')
            
        logging.shutdown()        
        
        
        
        
if __name__ == "__main__":
    main()        
        
        
        
        
        
        
        
        
        
        
        