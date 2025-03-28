###############################################################################
# Sample code that parses layers in a Map in a Pro Project (.APRX) for specific
# polygon label classes that use a particular maplex placement property.
# 
# author: Tommy Fauvell
# email: tfauvell@esri.com
#
###############################################################################
import arcpy

aprx = r'D:\Py_Workspace\mapx_inspector\Sample.aprx'

p = arcpy.mp.ArcGISProject(aprx)
m = p.listMaps('PanunTools Sample (Utah)')[0]
m_cim = m.getDefinition('V3')
layers = m.listLayers('*')
for l in layers:
    l_cim = l.getDefinition('V3')

    if not isinstance(l_cim, arcpy.cim.CIMVectorLayers.CIMFeatureLayer): #skip over non-feature layers: Group, Annotation, Service, Tile, etc
        # print(l.longName + str(l_cim))
        continue

    l_stats = ''
    if l_cim.visibility is True:
        l_stats = 'Layer On '
    else:
        l_stats = 'Layer Off: '
    if l.isGroupLayer is False:

        if l_cim.labelVisibility is True:
            l_stats += "Labels On: "
        else:
            l_stats += "Labels Off: "
        l_stats += l.longName

        for lc in l_cim.labelClasses:
            lc_stats = ''
            if (lc.maplexLabelPlacementProperties.featureType == "Polygon"):
                pm = lc.maplexLabelPlacementProperties.polygonPlacementMethod
                if pm in ("StraightInPolygon","CurvedInPolygon"):
                    if lc.visibility is True:
                        lc_stats = " - Label Class On: " + lc.name + " - Polygon Placement: " + pm
                    else:
                        lc_stats = " - Label Class Off: " + lc.name + " - Polygon Placement: " + pm
                    print (l_stats + lc_stats)
