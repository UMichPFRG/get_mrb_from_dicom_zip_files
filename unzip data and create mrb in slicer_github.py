# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:57:33 2023

@author: Mariana Masteling, PhD
        mastelin@umich.edu
        University of Michigan
    
"""

import pandas as pd
import numpy as np
import glob
import zipfile
import re

#%% Unzip folder 14 for each subject

directory = "your directory"

folder_names = glob.glob('*.zip')

for i in range(len(folder_names)):
    folder = folder_names[i]
    archive =  zipfile.ZipFile(folder, 'r')
    
    sequence_name_list = ['SER00014', 'SER00010']
    for sequence_name in sequence_name_list:
        file_list = [x for x in archive.namelist() if sequence_name in x]
        for file in file_list:
            archive.extract(file, path = directory+'/'+folder.split('.zip')[0])
    #f = archive.open(excel_name)
    

#%% Get from folder to .mrb for each subject 

# Load code from:  https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMUtils.py

## ************************* IN 3D SLICER ***************************
## copy to the 3D Slicer python iterator



# LOAD DICOMS INTO 3D SLICER MANUALLY

from DICOMLib import DICOMUtils
db = slicer.dicomDatabase
patientList = db.patients()
directory = "your directory"
for patient in patientList:
   studyList = db.studiesForPatient(patient)
   seriesList = db.seriesForStudy(studyList[0])
   fileList = db.filesForSeries(seriesList[0])
   id_ = db.fileValue(fileList[0], "0010,0020")
   print(id_)
   if 'C' in id_:
      id_ = id_.split('_')[1]
   elif 'SOMMA' in id_:
      id_ = id_.split('_')[1]
   else:
      id_  = id_.split('_')[0]

   loadPatientByUID(patient)
   sceneSaveFilename = directory+'/'+id_+'.mrb'
   slicer.util.saveScene(sceneSaveFilename)
   slicer.mrmlScene.Clear(0)
