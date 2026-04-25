import nuke
# Nuke helper: mirror selected nodes horizontally around the x position of the primary selected node (needs at least two nodes).
def flipNodes():
    nodes_selected = nuke.selectedNodes()
    # Need a reference node plus at least one other node to mirror across the reference x.
    if len(nodes_selected)<2:
        nuke.message('select at least 2 nodes.')
    else:
        # Primary selection supplies the vertical axis of symmetry in node graph space.
        ref_pos = nuke.selectedNode().xpos()
    # New x = ref + (ref - old_x) flips each node around ref_pos.
    for i in nodes_selected:
        i.setXpos(ref_pos+(ref_pos-i.xpos()))
