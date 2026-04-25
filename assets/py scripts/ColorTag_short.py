def for_dailies():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4194303)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Dialies', 'for_dailies()','F2')
def InternalKickback():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4284416255)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Internal Kickback', 'InternalKickback()','F3')
def Internaldoubt():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4290707711)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Internal doubt', 'Internaldoubt()','F4')
def SenttoClient():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(16728063)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Sent to Client','SenttoClient()','F5')
def clientKickback():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(4278190335)
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Client Kickback', 'clientKickback()','F6')
def default():
    n = nuke.selectedNodes()
    for i in n:
        i['tile_color'].setValue(0)
        i['frame_mode'].setValue('expression')
        i['frame'].setValue('')
nuke.menu("Nuke").addCommand('nikhil.s/Review_Tool/tag/Default','default()','F1')
