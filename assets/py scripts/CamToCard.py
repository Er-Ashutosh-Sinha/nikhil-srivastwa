import nuke
# Nuke helper: from a selected Camera2 and Card2, build four corner samples via Axis2 + Reconcile3D, bake them, drive a CornerPin2D, then delete temp nodes.
def cardtotrack():
    # Walk selection to capture camera and card node names; deselect each node as you go.
    sel = nuke.selectedNodes()
    for node in sel:
        if node.Class()=="Camera2":
            cam = nuke.selectedNode()
            camera = node.name()
        node['selected'].setValue(False)
        if node.Class()=="Card2":
            card = node.name()
        node['selected'].setValue(False)
    # Corner 1: axis follows card with translate/pivot offsets; reconcile samples camera vs axis; render writes r3d1 output.
    nuke.createNode("Axis2", inpanel=False).knob('name').setValue('ax1')
    ax_1 = nuke.selectedNodes()
    a1 = nuke.selectedNode()
    for value in ax_1:
        value['translate'].setExpression('parent.%s.translate-0.5' %(card),0)
        value['translate'].setExpression('parent.%s.translate-0.38' %(card),1)
        value['translate'].setExpression('parent.%s.translate' %(card),2)
        value['rotate'].setExpression('parent.%s.rotate' %(card))
        value['scaling'].setExpression('parent.%s.scaling' %(card))
        value['uniform_scale'].setExpression('parent.%s.uniform_scale' %(card))
        value['skew'].setExpression('parent.%s.skew' %(card))
        value['pivot'].setExpression('parent.%s.pivot+0.5' %(card),0)
        value['pivot'].setExpression('parent.%s.pivot+0.38' %(card),1)
        value['pivot'].setExpression('parent.%s.pivot' %(card),2)
        value['selected'].setValue(False)
    nuke.createNode('Reconcile3D', inpanel=False).knob('name').setValue('r3d1')
    r3d = nuke.selectedNode()
    r3d_1 = nuke.selectedNodes()
    for inputs in r3d_1:
        inputs.setInput(1, cam)
        inputs.setInput(2, a1 )
    nuke.render("r3d1")
    ################################################################
    # Corner 2: same pattern with different translate/pivot offsets, then render r3d2.
    nuke.createNode("Axis2", inpanel=False).knob('name').setValue('ax2')
    ax_2 = nuke.selectedNodes()
    a2 = nuke.selectedNode()
    for value in ax_2:
        value['translate'].setExpression('parent.%s.translate+0.5' %(card),0)
        value['translate'].setExpression('parent.%s.translate-0.38' %(card),1)
        value['translate'].setExpression('parent.%s.translate' %(card),2)
        value['rotate'].setExpression('parent.%s.rotate' %(card))
        value['scaling'].setExpression('parent.%s.scaling' %(card))
        value['uniform_scale'].setExpression('parent.%s.uniform_scale' %(card))
        value['skew'].setExpression('parent.%s.skew' %(card))
        value['pivot'].setExpression('parent.%s.pivot-0.5' %(card),0)
        value['pivot'].setExpression('parent.%s.pivot+0.38' %(card),1)
        value['pivot'].setExpression('parent.%s.pivot' %(card),2)
        value['selected'].setValue(False)
    nuke.createNode('Reconcile3D', inpanel=False).knob('name').setValue('r3d2')
    r3d2 = nuke.selectedNode()
    r3d_2 = nuke.selectedNodes()
    for inputs in r3d_2:
        inputs.setInput(1, cam)
        inputs.setInput(2, a2 )
    nuke.render("r3d2")
    ##################################################################
    # Corner 3: axis + reconcile + render r3d3.
    nuke.createNode("Axis2", inpanel=False).knob('name').setValue('ax3')
    ax_3 = nuke.selectedNodes()
    a3 = nuke.selectedNode()
    for value in ax_3:
        value['translate'].setExpression('parent.%s.translate+0.5' %(card),0)
        value['translate'].setExpression('parent.%s.translate+0.38' %(card),1)
        value['translate'].setExpression('parent.%s.translate' %(card),2)
        value['rotate'].setExpression('parent.%s.rotate' %(card))
        value['scaling'].setExpression('parent.%s.scaling' %(card))
        value['uniform_scale'].setExpression('parent.%s.uniform_scale' %(card))
        value['skew'].setExpression('parent.%s.skew' %(card))
        value['pivot'].setExpression('parent.%s.pivot-0.5' %(card),0)
        value['pivot'].setExpression('parent.%s.pivot-0.38' %(card),1)
        value['pivot'].setExpression('parent.%s.pivot' %(card),2)
        value['selected'].setValue(False)
    nuke.createNode('Reconcile3D', inpanel=False).knob('name').setValue('r3d3')
    r3d3 = nuke.selectedNode()
    r3d_3 = nuke.selectedNodes()
    for inputs in r3d_3:
        inputs.setInput(1, cam)
        inputs.setInput(2, a3 )
    nuke.render("r3d3")
    ##################################################################
    # Corner 4: axis + reconcile + render r3d4.
    nuke.createNode("Axis2", inpanel=False).knob('name').setValue('ax4')
    ax_4 = nuke.selectedNodes()
    a4 = nuke.selectedNode()
    for value in ax_4:
        value['translate'].setExpression('parent.%s.translate-0.5' %(card),0)
        value['translate'].setExpression('parent.%s.translate+0.38' %(card),1)
        value['translate'].setExpression('parent.%s.translate' %(card),2)
        value['rotate'].setExpression('parent.%s.rotate' %(card))
        value['scaling'].setExpression('parent.%s.scaling' %(card))
        value['uniform_scale'].setExpression('parent.%s.uniform_scale' %(card))
        value['skew'].setExpression('parent.%s.skew' %(card))
        value['pivot'].setExpression('parent.%s.pivot+0.5' %(card),0)
        value['pivot'].setExpression('parent.%s.pivot-0.38' %(card),1)
        value['pivot'].setExpression('parent.%s.pivot' %(card),2)
        value['selected'].setValue(False)
    nuke.createNode('Reconcile3D', inpanel=False).knob('name').setValue('r3d4')
    r3d4 = nuke.selectedNode()
    r3d_4 = nuke.selectedNodes()
    for inputs in r3d_4:
        inputs.setInput(1, cam)
        inputs.setInput(2, a4 )
    nuke.render("r3d4")
    ###################################################################
    # Build CornerPin2D and copy baked point animations from each Reconcile3D output into to1–to4.
    nuke.createNode('CornerPin2D', inpanel=False)
    crpin = nuke.selectedNodes()
    for trace in crpin:
        trace.setInput(0, None)
        trace['to1'].copyAnimations(r3d['output'].animations())
        trace['to2'].copyAnimations(r3d2['output'].animations())
        trace['to3'].copyAnimations(r3d3['output'].animations())
        trace['to4'].copyAnimations(r3d4['output'].animations())
    # Remove temporary reconcile and axis nodes by name.
    for ers in nuke.allNodes():
        if ers.name()=='r3d1':
            nuke.delete(ers)
        elif ers.name()=='r3d2':
            nuke.delete(ers)
        elif ers.name()=='r3d3':
            nuke.delete(ers)
        elif ers.name()=='r3d4':
            nuke.delete(ers)
        elif ers.name()=='ax1':
            nuke.delete(ers)
        elif ers.name()=='ax2':
            nuke.delete(ers)
        elif ers.name()=='ax3':
            nuke.delete(ers)
        elif ers.name()=='ax4':
            nuke.delete(ers)
