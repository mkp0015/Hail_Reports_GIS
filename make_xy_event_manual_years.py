#********************************************************
# FILE: make_xy_event.py
# AUTHOR: Melinda Pullman
# EMAIL: mkp0015@uah.edu
# MODIFIED BY: n/a
# ORGANIZATION: UAH/ATS Dept.
# CREATION DATE: 03/25/2017
# LAST MOD DATE: n/a
# PURPOSE: This script takes imported CSV datafiles within a folder, iterates
#          over these files, and creates an XY event layer for each file, and
#          creats a file geodatabase to store the new XY event layers.
# DEPENDENCIES: arcpy
#********************************************************

#import dependencies (packages)
import arcpy

#declare variables
source_workspace = arcpy.GetParameterAsText(0)
out_gdb = arcpy.GetParameterAsText(1)

#set environment workspace, enable file overwrite
arcpy.env.workspace = source_workspace
arcpy.env.overwriteOutput = True

#create a file geodatabase to store xy event layers
arcpy.CreateFileGDB_management(source_workspace, out_gdb)

#Get a list of all files in the storm_events folder
file_list = arcpy.ListFiles('*.csv')

try:
    
    #loop through all files in storm_events folder
    for files in file_list:
        
        #get file name without extension
        new_filename = files.split('.')[0]
     
        #set local variables for xy event layer
        longitude = 'LONGITUDE'
        latitude = 'LATITUDE'
        sr = arcpy.SpatialReference('NAD 1983')
        out_xy = new_filename + '_layer'
        saved_xy_layer = new_filename + '.lyr'
        saved_xy_shp = new_filename + '.shp'
        
        #make the xy event layer
        arcpy.MakeXYEventLayer_management(files, longitude, latitude, out_xy, sr)

        #create an output layer file (.lyr) file
        arcpy.SaveToLayerFile_management(out_xy, saved_xy_layer)

        #copy the layer file to a shapefile (.shp)
        arcpy.CopyFeatures_management(saved_xy_layer, saved_xy_shp)

        #move shapefile to file geodatabase
        arcpy.FeatureClassToGeodatabase_conversion(saved_xy_shp, out_gdb)

except Exception as err:
     print(err.args[0])


