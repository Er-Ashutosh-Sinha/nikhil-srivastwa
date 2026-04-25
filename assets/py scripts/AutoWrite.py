import os
import nuke
# Nuke helper: after the script is saved and Read1 exists, derive a render folder from the plate path
# and the script filename suffix, prompt for an output extension, create the folder if needed, and set a new Write node's file path.
def AutoWrite():
    scriptPath = nuke.root().name()
    ######## check for script save #############
    # Unsaved scripts report name 'Root'; require a saved .nk before continuing.
    if scriptPath == 'Root':
        nuke.message('Please save Nuke script')
    else:
        pass
    ######## check for Read Availablity #############
    # Require at least one Read node anywhere in the script (Read1 is used later for the plate path).
    allnodes = []
    for i in nuke.allNodes():
       allnodes.append(i.Class())
    if 'Read' not in allnodes:
        nuke.message('Please import Read')
    else:
        pass
    # Plate file path comes from the node named Read1 (must exist and point at the plate).
    filePath = nuke.toNode('Read1').knob('file').value()
    print (filePath)
    # Last path segment of the .nk file; strip extension; last five characters of that stem are treated as the version token.
    splitSPath = scriptPath.split('/')[-1]
    split_ext = splitSPath.split('.nk')[0]
    version = split_ext[-5:]
    path = os.path.split(filePath)[0]
    filename = os.path.split(filePath)[1]
    # Split plate directory at '/plate' so the render path can be built as prefix + '/Render' + extension branch.
    pathSplit = path.split('/plate')
    Pulldown = "exr jpg mov dpx png tiff tga "
    # User chooses output container / extension from a Nuke panel.
    p = nuke.Panel("Extension")
    p.addEnumerationPulldown("Extension:", Pulldown)
    result = p.show()
    enumVal = p.value("Extension:")
    try:
        if enumVal is not None:
            print ('none')
    except ValueError:
        raise 'Please select any Extension'
    #print 'filePath=', filePath
    #print 'path=',path
    #print 'filename=',filename
    #print 'pathSplit=',pathSplit
    #ext = filename.split('.')[1]
    ext = enumVal
    #print ext
    # Folder name segment: parent directory name of the plate, underscore, extension, then version suffix from script name.
    dir = path.split('/')[-2]
    #print dir
    mkdir = '/' + str(dir) + '_' + str(ext) + str(version)
    #print mkdir
    # Full write directory: path before '/plate' + Render/<ext> + suffix folder; create if missing.
    wpath = '' .join(pathSplit) + '/Render' + '/' + ext
    writepath = wpath + mkdir
    try:
        os.stat(writepath)
    except:
        os.makedirs(writepath)
    # New Write node: sequence path with #### frame padding and chosen extension.
    nuke.createNode('Write').knob('file').setValue(writepath+'/'+ split_ext  + '.' + '####.'+ ext)
