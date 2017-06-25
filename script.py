import csv, os
import xml.etree.ElementTree as ET
import subprocess

f = open("Book2.csv")
csvf = csv.reader(f)
for row in csvf:
    prev = os.getcwd()
    os.chdir(row[0])
    tree = ET.parse("config.xml")
    ET.register_namespace('', "http://www.w3.org/ns/widgets")
    ET.register_namespace('intelxdk', "http://xdk.intel.com/ns/v1")
    root = tree.getroot()
    root.find("{http://www.w3.org/ns/widgets}name").text = row[1]
    root.find("{http://www.w3.org/ns/widgets}content").set("src", row[2]) 
    path1 = row[3]
    path2 = row[4]
    dirs1 = os.listdir(path1)
    dirs2 = os.listdir(path2)
    platform = ET.SubElement(root, "platform")
    platform.set("name", "android")
    for files in dirs1:
        icon = ET.SubElement(platform, "icon")
    c=0
    paths = []
    for files in dirs1:
        var = os.listdir(path1 + "/" + dirs1[c])
        paths.append(path1 + "/" + dirs1[c] + "/" + var[0])
        c = c+1
    c=0
    for icon in root.iter("icon"):
        icon.set("src", paths[c])
        c = c+1
    for files in dirs2:
        splash = ET.SubElement(platform, "splash")
    c=0
    paths1 = []
    for files in dirs2:
        var = os.listdir(path2 + "/" + dirs2[c])
        paths1.append(path2 + "/" + dirs2[c] + "/" + var[0])
        c = c+1
    c=0
    for splash in root.iter("splash"):
        splash.set("src", paths1[c])
        c =c+1
    tree.write("config.xml")
    with open(row[5], "r") as rf:
        data = rf.read()
        data = data.replace(row[11], row[12])
    with open(row[5], "w") as wf:
        wf.write(data)
    with open(row[6], "r") as rf:
        data = rf.read()
        data = data.replace(row[7], row[8])
        data = data.replace("../images" + "/" + row[9], "../images" + "/" + row[10])
    with open(row[6], "w") as wf:
        wf.write(data)  
    subprocess.call("cordova build", shell = True)
    os.chdir(prev)
f.close()               
                
     