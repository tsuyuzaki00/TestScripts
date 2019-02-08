import maya.cmds as cmds
import pymel.core as pm

def main():
    sel = pm.ls(sl = True, dag=True)

    for jntname in sel:
        if jntname.find('jnt') > -1:
            print jntname
            #pm.orientConstraint( , )
