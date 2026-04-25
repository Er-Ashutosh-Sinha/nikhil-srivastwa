import os
import nuke
def AutoWrite():
    scriptPath = nuke.root().name()
    if scriptPath == 'Root':
        nuke.message('Please save Nuke script')
    else:
        pass
    allnodes = []
    for i in nuke.allNodes():
       allnodes.append(i.Class())
    if 'Read' not in allnodes:
        nuke.message('Please import Read')
    else:
        pass
    filePath = nuke.toNode('Read1').knob('file').value()
    print (filePath)
    splitSPath = scriptPath.split('/')[-1]
    split_ext = splitSPath.split('.nk')[0]
    version = split_ext[-5:]
    path = os.path.split(filePath)[0]
    filename = os.path.split(filePath)[1]
    pathSplit = path.split('/plate')
    Pulldown = "exr jpg mov dpx png tiff tga "
    p = nuke.Panel("Extension")
    p.addEnumerationPulldown("Extension:", Pulldown)
    result = p.show()
    enumVal = p.value("Extension:")
    try:
        if enumVal is not None:
            print ('none')
    except ValueError:
        raise 'Please select any Extension'
    ext = enumVal
    dir = path.split('/')[-2]
    mkdir = '/' + str(dir) + '_' + str(ext) + str(version)
    wpath = '' .join(pathSplit) + '/Render' + '/' + ext
    writepath = wpath + mkdir
    try:
        os.stat(writepath)
    except:
        os.makedirs(writepath)
    nuke.createNode('Write').knob('file').setValue(writepath+'/'+ split_ext  + '.' + '####.'+ ext)
