import nuke
def flipNodes():
    nodes_selected = nuke.selectedNodes()
    if len(nodes_selected)<2:
        nuke.message('select at least 2 nodes.')
    else:
        ref_pos = nuke.selectedNode().xpos()
    for i in nodes_selected:
        i.setXpos(ref_pos+(ref_pos-i.xpos()))
