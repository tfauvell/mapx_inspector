###############################################################################
# Sample code that inventories layer types in a Map in a Pro Project (.APRX).
# 
# author: Tommy Fauvell
# email: tfauvell@esri.com
#
###############################################################################
import arcpy

aprx = r'D:\GitHub Workspace\mapx_inspector\Sample.aprx'

p = arcpy.mp.ArcGISProject(aprx)
m = p.listMaps('PanunTools Sample (Utah)')[0]
m_cim = m.getDefinition('V3')
layers = m.listLayers('*')
layer_groups = {}

for l in layers:
    l_cim = l.getDefinition('V3')
    l_type = type(l_cim).__name__
    if l_type in layer_groups:
        layer_groups[l_type] += 1
    else:
        layer_groups[l_type] = 1

print(layer_groups)
