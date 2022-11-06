# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:30:37 2022

@author: Mark Patmore
"""

import logging




logging.basicConfig(filename='example.log',
                    level=logging.ERROR,
                    filemode='w',
                    force=True)



try:
    print(0/0)
    
except Exception as Argument:
    logging.exception(str(Argument))