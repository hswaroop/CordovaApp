import csv, os
import xml.etree.ElementTree as ET
import subprocess

listanicon = ["ldpi", "mdpi", "hdpi", "xhdpi"]
listansplashport = ["port-mdpi", "port-hdpi", "port-xhdpi", "port-xxhdpi", "port-xxxhdpi"] 
f = open("Book2.csv")
csvf = csv.reader(f)
tree = ET.parse("config.xml")
ET.register_namespace('', "http://www.w3.org/ns/widgets")
ET.register_namespace('gap', "http://phonegap.com/ns/1.0")
ET.register_namespace('cdv', "http://cordova.apache.org/ns/1.0")
ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
root = tree.getroot()
check = 0
for row in csvf:
    root.find("{http://www.w3.org/ns/widgets}name").text = row[0]
    attribute = root.attrib
    appid = attribute["id"]
    root.set("id", appid + str(check))
    if(check == 0):
        platform = ET.SubElement(root, "platform")
        platform.set("name", "android")
        for var in range(1, 5):
            icon = ET.SubElement(platform, "icon")
            icon.set("density", listanicon[var-1])
            icon.set("src", row[var])
        for var in range(5, 10):
            splash = ET.SubElement(platform, "splash")
            splash.set("density", listansplashport[var-5])
            splash.set("src", row[var])
    else:
        reset = 1
        for icon in root.iter("icon"):
            icon.set("src", row[reset])
            reset = reset + 1
        for splash in root.iter("splash"):
            splash.set("src", row[reset])

    tree.write("config.xml")
    
    with open(row[10], "r+") as rf:
        listfiles = rf.readlines()
        length = len(listfiles)
        for var in range(0,length):
            var1 = listfiles[var].find(row[11])
            if(var1!=-1):
                listfiles[var] = "var" + " " + row[11] + " " + "=" + " " + row[12] + ";" + "\n"
                break    
        rf.seek(0,0)
        for lines in listfiles:
            rf.writelines(lines)
        
    with open(row[13], "r+") as rf:
        listfiles = rf.readlines()
        length = len(listfiles)
        flag1=0
        flag2=0
        for var in range(0,length):
            var1 = listfiles[var].find(row[14])
            var2 = listfiles[var].find(row[16])
            if(var1!=-1):
                listfiles[var] = "--" + row[14] + ":" + " " + row[15] + ";" + "\n"
                flag1=1
            elif(var2!=-1):
                listfiles[var] = "--" + row[16] + ":" + " " + row[17] + ";" + "\n"
                flag2=1
            if(flag1==1 and flag2==1):
                break
        rf.seek(0,0)
        for lines in listfiles:
            rf.writelines(lines)
            
    subprocess.call("cordova build", shell = "True")
    check = check + 1
    os.rename("platforms/android/build/outputs/apk/android-debug.apk", "platforms/android/build/outputs/apk/android-debug" + str(check) + ".apk")
    #os.rename("platforms/android/build/outputs/apk/android-debug" + str(check) + ".apk", "platforms/android-debug" + str(check) + ".apk")
f.close()        