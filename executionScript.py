''' LibraryReload '''
#from MayaLibrary import setCurves as ml; reload(ml);
''' Run '''
#from mainEdit import skinPaintValue as ps
from MayaExecute import setCurves_antenna as ps
reload(ps); ps.main()

#import pymel.core as pm
#import maya.cmds as cmds