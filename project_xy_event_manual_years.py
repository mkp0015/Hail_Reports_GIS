#********************************************************
# FILE: make_xy_event.py
# AUTHOR: Melinda Pullman
# EMAIL: mkp0015@uah.edu
# MODIFIED BY: n/a
# ORGANIZATION: UAH/ATS Dept.
# CREATION DATE: 03/25/2017
# LAST MOD DATE: n/a
# PURPOSE: This script will take imported XY event layers and will project
#          each layer by iterating through the file geodatabase that contains
#          the XY event layers and applying the ArcGIS Project tool.
# DEPENDENCIES: arcpy
#********************************************************

#import dependencies (packages)
import arcpy

#declare variables
source_workspace = arcpy.GetParameterAsText(0)

#set environmental settings
arcpy.env.workspace = source_workspace
arcpy.env.overwriteOutput = True

try:

    #loop over feature classes in workspace
    for infcList in arcpy.ListFeatureClasses():

        #set local variables for project tool
        out_fc = infcList.split('\\')[-1] + '_proj'
        out_cs = arcpy.SpatialReference('North America Albers Equal Area Conic')

        #project feature classes in workspace
        arcpy.Project_management(infcList, out_fc, out_cs)

except Exception as err:
    print(err.args[0])

    


