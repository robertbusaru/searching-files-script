import fileinput
import json
import os
import platform
import os.path, time
import datetime
import io

#Here you can change your path! :)
basePath = ('C:\Program Files\Git')

#print(os.getpid())

def getOsInfo():
    os_name = platform.platform()
    os_release = platform.release()
    os_vers = platform.version()
    os_arh = platform.architecture()
    os_pm = platform.processor()

    info = {

        "OS": os_name,
        "OS release": os_release,
        "OS Version": os_vers,
        "OS Arhitecture": os_arh,
        "Processor": os_pm,

    }
    return json.dumps(info, indent = 4)

def sizeOf(fileFor):
    return os.path.getsize(fileFor)

def timeConverter(myTime):
    return datetime.datetime.fromtimestamp(myTime).strftime('%c')



for path, dirName, files in os.walk(basePath):
    for file in files:

            #our variables who represent useful data:
            folderRoad = os.path.join(path) #folder where data is located
            fileName = ("{}".format(os.path.join(file.split(".")[0]))) #file name, for example: "audio"
            fileExtension = ("{}".format(os.path.join(file.split(".")[-1]))) # extension of a file, for example: ".exe" -> audio.exe
            pathLocation = ("{}".format(os.path.join(path))) #path of a file, for example: "C:\Program Files"
            dateOfCreation = ("{}".format(timeConverter(os.path.getctime(path)))) #get the creation date of a file
            sizeOfFile = ("{}".format(sizeOf(os.path.abspath(os.path.join(path, file))))) #size of a file -> byte

            #our main dictionary is builded using this model:
            values = {

                "name": fileName,
                "extension": fileExtension,
                "path": pathLocation,
                "creation": dateOfCreation,
                "size": sizeOfFile
            }

            key = {

               folderRoad: values

            }

            if os.path.isfile(os.path.join(path)) and (os.accessos.path.join(path), os.R_OK):
                pass
                print("File already exists!")
            else:
                print("File is missing or is not readable, creating file...")
                with open('files.json', 'a') as insert:
                        insert.write('\n')
                        insert.write("{}".format(json.dumps(key, indent = 4)))
                        insert.close()


#OS Info:
with open("os_info.json", 'w') as input:
    input.write(getOsInfo())


print("Finished!")
