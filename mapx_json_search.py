###############################################################################
# Sample code that parses an exported Map (.MAPX) JSON for specific polygon 
# label classes that use a particular maplex placement property.
#
# author: Tommy Fauvell
# email: tfauvell@esri.com
#
###############################################################################
import json

mapxPath = r'D:\Py_Workspace\mapx_inspector\PanunTools Sample (Utah).mapx'

with open(mapxPath, "r", encoding="utf-8") as j:
    mapx = json.load(j)

# Check for problematic polygon label placement
# For each layer name, find label classes. For each label class find instances of StraightInPolygon or CurvedInPolygon
for l in mapx["layerDefinitions"]:
    l_path = ""
    if l["type"] == "CIMFeatureLayer":
        for lc in l["labelClasses"]:
            mp = lc["maplexLabelPlacementProperties"]["polygonPlacementMethod"] # json object containing Straight or Curved in Polygon values
            if (lc["maplexLabelPlacementProperties"]["featureType"] == "Polygon") and (mp in ("StraightInPolygon","CurvedInPolygon")): # limit report to Polygons with the specific PlacementMethod
                # Layer visibility check:
                if ("visibility" in l) and (l["visibility"] is True):
                    l_path = "Layer On " 
                else:
                    # continue
                    l_path = "Layer Off "

                # labelVisibility check:
                if "labelVisibility" in l:
                    lv = l["labelVisibility"]
                    l_path += "Labels On: "
                else:
                    l_path += "Labels Off: "
                
                l_path += l["name"] + " - "

                # Label class visiblity check:
                if ("visibility" in lc) and (lc["visibility"] is True):
                    l_path +=  "Label Class On: " + lc["name"] + " - Polygon Placement: " + mp
                    # lc["visibility"] = False
                    # lc["maplexLabelPlacementProperties"]["polygonPlacementMethod"] = "HorizontalInPolygon"
                else:
                    # continue
                    l_path +=  "Label Class Off: " + lc["name"] + " - Polygon Placement: " + mp
                print (l_path)
