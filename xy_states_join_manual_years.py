#********************************************************
# FILE: make_xy_event.py
# AUTHOR: Melinda Pullman
# EMAIL: mkp0015@uah.edu
# MODIFIED BY: n/a
# ORGANIZATION: UAH/ATS Dept.
# CREATION DATE: 03/25/2017
# LAST MOD DATE: n/a
# PURPOSE: This script will iterate through join features in
#          a file geodatabase and join these features to a
#          specified target feature.
# DEPENDENCIES: arcpy
#********************************************************

#import dependencies (packages)
import arcpy

#declare variables
target_features = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

#set environmental settings
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True

try:
    #loop through all files in storm_events_manual.gdb that contain '_proj' in the file name
    for join_features in arcpy.ListFeatureClasses('*_proj*'):

        #set local variables for joined layer
        out_fc = join_features.split('\\')[-1] + '_join'

        #join the XY event layer to the counties shapefile
        arcpy.SpatialJoin_analysis(target_features, join_features, out_fc)

except Exception as err:
    print (err.args[0])
