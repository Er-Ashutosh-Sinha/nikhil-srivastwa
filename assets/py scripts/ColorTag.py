# Nuke menu helpers: set Read (or any selected node) tile_color for review status; each function is bound to a hotkey under nikhil.s/Review_Tool/tag/.
def for_dailies():
    # Dailies review tag (F2).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4194303)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Dialies', 'for_dailies()','F2')
def InternalKickback():
    # Internal kickback tag (F3).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4284416255)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Internal Kickback', 'InternalKickback()','F3')
def Internaldoubt():
    # Internal doubt tag (F4).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4290707711)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Internal doubt', 'Internaldoubt()','F4')
def SenttoClient():
    # Sent to client tag (F5).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(16728063)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Sent to Client','SenttoClient()','F5')
def clientKickback():
    # Client kickback tag (F6).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4278190335)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Client Kickback', 'clientKickback()','F6')
def default():
    # Reset tile color and frame expression to defaults (F1).
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(0)
        i['frame_mode'].setValue('expression')
        i['frame'].setValue('')
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Default','default()','F1')
