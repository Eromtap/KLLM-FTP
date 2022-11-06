# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:39:17 2022

@author: Mark Patmore JMDJP
"""

import os
import sys
from datetime import date
today = date.today()
today = today.strftime("%m/%d/%Y")


sys.path.append("..")


from ftpTransfer import xlsx_to_ods as xl


xlRowsInitial = [['EQCompanyCode',
                  'EQFleetCode',
                  'EQUnitCode',
                  'EQType',
                  'EQVIN',
                  'MeterReadingDate',
                  'PrimaryMeterType',
                  'PrimaryMeterReading',
                  'PrimaryMeterLifeToDateUsage',
                  'SecondaryMeterType',
                  'SecondaryMeterReading',
                  'SecondaryMeterLifeToDateUsage',
                  'Latitude',
                  'Longitude']]

# Test initialization of xlsx_rows list

if xl.xlsx_rows == xlRowsInitial:
    print("Initialized xlsx_rows data:            Passed")

else:
    print("Initialized xlsx_rows data:            Failed")


xl.xlsx_rows = []


xlRowsTrucks = [
                ['', '', '43014', '', '', '09/03/2022', '', '89', '', '', '', '', '', ''],
                ['', '', '43015', '', '', '09/09/2022', '', '6307', '', '', '', '', '', ''],
                ['', '', '43016', '', '', '09/09/2022', '', '6426', '', '', '', '', '', ''],
                ['', '', '43017', '', '', '09/09/2022', '', '11487', '', '', '', '', '', ''],
                ['', '', '43018', '', '', '09/08/2022', '', '51', '', '', '', '', '', ''],
                ['', '', '43019', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '43022', '', '', '09/08/2022', '', '22', '', '', '', '', '', ''],
                ['', '', '43023', '', '', '', '', '', '', '', '', '', '', '']
                ]




## Test output of truck data collection

xl.collect_xlsx_data(f'testTrucks.xlsx',3,2,3,4)

if xl.xlsx_rows == xlRowsTrucks:
    print("xlsx_rows data after Trucks func:      Passed")

else:
    print("xlsx_rows data after Trucks func:      Failed")

xl.xlsx_rows = []




xlRowsCarriers = [
                 ['', '', 'U532111', '', '', '03/17/2022', '', '3807', '', '', '', '', '', ''],
                 ['', '', 'U532112', '', '', '09/05/2022', '', '3730', '', '', '', '', '', '']
                 ]










xl.collect_xlsx_data(f'mc_trailers.xlsx',3,2,3,4)



if xl.xlsx_rows == xlRowsCarriers:
    print("xlsx_rows data after Carriers func:    Passed")

else:
    print("xlsx_rows data after Carriers func:    Failed")



xl.xlsx_rows = []




xlsxRowsTK = [
              ['', '', 'U531960', '', '', '01/01/01', '', '7523', '', '', '', '', '', ''],
              ['', '', 'U531928', '', '', '01/01/01', '', '6914', '', '', '', '', '', ''],
              ['', '', 'U531951', '', '', '01/01/01', '', '6826', '', '', '', '', '', ''],
              ['', '', 'U531970', '', '', '01/01/01', '', '6843', '', '', '', '', '', ''],
              ['', '', 'U531923', '', '', '01/01/01', '', '7418', '', '', '', '', '', ''],
              ['', '', 'U531946', '', '', '01/01/01', '', '7369', '', '', '', '', '', ''],
              ['', '', 'U531943', '', '', '01/01/01', '', '6520', '', '', '', '', '', ''],
              ['', '', 'U531956', '', '', '01/01/01', '', '6936', '', '', '', '', '', '']
              ]



xl.collect_stupid_TK_data(f'test TK.xlsx', 5, 1, 11, '01/01/01') 


if xl.xlsx_rows == xlsxRowsTK:
    print("xlsx_rows data after TK func:          Passed")

else:
    print("xlsx_rows data after TK func:          Failed")



















