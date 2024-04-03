# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:37:19 2021

@author: arodriguezs
"""

from pathlib import Path
from datetime import datetime
import shutil
import os

# Create a path object
our_files = Path("G:") # "G:/Test"
#your_files = Path("C:/Users/arodriguezs/Documents/TestWaterRep")

your_files = Path("//CDJPRO.com/Fileserver/PNSA_Stecnicos_Water/2024/_Datos Periodicos")


for file in our_files.iterdir():
    print(file)                                                                # G:\Test\WaterCNT_Friday, February 19, 2021.txt

    # 1) Check if the file is a file and not a folder
    if file.is_file() and file.stem != ".DS_Store":
        
        # 2) Create helpful variables
        directory = file.parent
        extension = file.suffix
        print(directory, extension)                                            # G:\Test .txt

        old_name = file.stem
        print(old_name)                                                        # WaterCNT_Friday, February 19, 2021
        if "-" in old_name:
            continue                  
        reporte, monthDay, year = old_name.split(', ')
        month, day = monthDay.split(' ')
        old_date = month + day + year

        # 3) Change date format and label the new file
        old_date = datetime.strptime(old_date, "%B%d%Y")
        date = datetime.strftime(old_date, '%Y-%m-%d')
        new_file = f'{reporte} - {date}{extension}'
        #print(new_file)                                                        # WaterCNT_Friday - 2021-02-19.txt
        
        # 4) Create a new name at the same path
        new_file_path = our_files.joinpath(new_file)
        #print(new_file_path)                                                   # G:\Test\WaterCNT_Friday - 2021-02-19.txt
        
        # 5) Rename file
        os.rename(file,new_file_path)

        # 6) Calculate the month and create a new path with it
        month = datetime.strftime(old_date, "%B")
        #print(month)                                                           # February
        new_path = your_files.joinpath(month)
        #print(new_path)                                                        # \\CDJPRO.com\FileserverPNSA\WaterCNT\2021\TEST\February

        # 7) Check if the folder exists. If not, create it
        if not new_path.exists():
            new_path.mkdir()
        
        path_dest = new_path.joinpath(new_file)                                # Nuevo path con el nuevo nombre del archivo

        # 8) Move the files        
        shutil.move(new_file_path, path_dest)                                  # Cut & paste action. In external folder
        
        
        