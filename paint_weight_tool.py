'''
- 21.12.17 by kims
- ver 1.0

'''

import maya.cmds as mc
from sys import stdout


#==================================================================
#  Set BlendShape Targets Weight of single mesh about all vertex
#==================================================================
# ex) 
# paintTargetL= ['Smile','Frown','UpArm_Side_90']
# Set_BlendTargetWeight('bodyMesh','blendShape1', paintTargetL, 0)

def Set_BlendTargetWeight(mesh, bl, paintTargetL, val):

    print ("Set_BlendTargetWeight execute..")
    print (' targets number : '+ str(len(paintTargetL)))
    print (mesh, bl, paintTargetL, val)

    # paintTargetL - Targets to set user weight value     
    
    # val - user weight value     
    
    # Get Targets Name and weight[index] Name 
    allTargetL=mel.eval('aliasAttr -q "'+bl+'";') 
    print (allTargetL)
    
    # Get as { paintTarget : weight[index] }
    indexL={}
    for n, e in enumerate(allTargetL):    
        if n%2==0: # when e is target name
           if e in paintTargetL: # if e exist in paintTargetL
               # get index number from weight[index] as string        

               indexE = allTargetL[n+1].find(']') 
               indexS = allTargetL[n+1].find('[') 
               indexL[e] = allTargetL[n+1][indexS+1:indexE]
               
    vtxNum=mc.polyEvaluate(mesh, v=1)
    
    # set target blendShape weight ( all vtx )
    for target in paintTargetL:
        print (target , indexL[target])
        for i in range(vtxNum):                  
            mc.setAttr(bl+'.inputTarget[0].inputTargetGroup['+indexL[target]+'].tw['+str(i)+']', val)
            
            
            
#=======================================================#
#   apply Set_BlendTargetWeight Function 
#   from selected mesh and selected attributes
#=======================================================#
# ex)
# first, select mesh.
# and select input blendshape's target attributes in channel box
# execute Set_SelectTargetAttrs_BlendShapeWeight(0)

def Set_SelectTargetAttrs_BlendShapeWeight(val):

    sels=mc.ls(sl=1) # get blendshape node, mesh 
    mesh = sels[1]
    bl = sels[0]
    paintTargetL = mel.eval('selectedChannelBoxAttributes')
    
    Set_BlendTargetWeight(mesh, bl, paintTargetL, val)
    
    stdout.write('Complete !!')            