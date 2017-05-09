#********************************************************
# FILE: make_xy_event.py
# AUTHOR: Melinda Pullman
# EMAIL: mkp0015@uah.edu
# MODIFIED BY: n/a
# ORGANIZATION: UAH/ATS Dept.
# CREATION DATE: 03/25/2017
# LAST MOD DATE: n/a
# PURPOSE: This will convert the joined XY event and counties shapefile layers
#          within the storm events file geodatabase and convert the feature data
#          to point data. Because the join function automatically creates a field
#          that contains the number of storm events per county (Join Count field),
#          This same count field will be associated with the point layer and can
#          be used for a hot spot analysis.
# DEPENDENCIES: arcpy
#********************************************************

#import dependencies (packages)
import arcpy

#declare variables
workspace = arcpy.GetParameterAsText(0)

#set environmental settings
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True

try:

    #loop through joined files in the storm_events file geodatabase 
    for input_feats in arcpy.ListFeatureClasses('*_join*'):

        #set local variables for the feature to point layer
        out_fc = input_feats.split('\\')[-1] + '_point'

        #convert the feature join layer to a point layer
        arcpy.FeatureToPoint_management(input_feats, out_fc) 

except Exception as err:
    print (err.args[0])
