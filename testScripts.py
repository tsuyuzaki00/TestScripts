import maya.cmds as cmds
import pymel.core as pm

def main():
    sels = pm.ls(sl = True, dag=True)

    for sel in sels:
        print sel
