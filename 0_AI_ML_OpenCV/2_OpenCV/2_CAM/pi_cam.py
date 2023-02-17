import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import serial
from datetime import timedelta
import csv
from os.path import join as pjoin
import datetime
import time


EIPath = 'try'
ListImgs = []
ListNames = []
ListEmployees = os.listdir(EIPath)
print(ListEmployees)


for Employee in ListEmployees:
    ImgsEmployee = cv2.imread(f'{EIPath}/{Employee}')
    ListImgs.append(ImgsEmployee)
    ListNames.append(os.path.splitext(Employee)[0])

print(ListNames)


def findEncodings(ListImgs):
    #Write an empty list that will have the encoding in the end
    encodeList = []
    #Looping imgs
    for eImgs in ListImgs:
        #Convert it to RGB
        eImgs = cv2.cvtColor(eImgs, cv2.COLOR_BGR2RGB)
        #Finding the encoding
        encodeEImgs = face_recognition.face_encodings(eImgs)[0]
        encodeList.append(encodeEImgs)
    return encodeList

encodeKnown = findEncodings(ListImgs)
print('Encoding Complete')



def timeIn(BARCODE):
    while True:
        path = 'DO NOT DELETE NOR OPEN'
        filename = '{}.csv'.format(time.strftime("%Y%m%d"))
        path_filename = pjoin(path, filename)
        with open(path_filename, 'a+') as a:
            #fieldnames = csv.writer(f)
            #fieldnames.writerow(["BARCODE", "DATE", "TIME-IN", "TIME-OUT"])
            files_by_day_list = a.readlines()
            nameList = []
            for line in files_by_day_list:
                entry = line.strip().split(',')
                nameList.append(entry[0])

            if BARCODE not in nameList:

                now = datetime.datetime.now()
                hrs = now.hour;
                mins = now.minute;
                secs = now.second;
                zero = timedelta(seconds=secs + mins * 60 + hrs * 3600)
                st = now - zero  # this take me to 0 hours.
                ref_time = st + timedelta(seconds=12 * 3600 + 0 * 60)
                time_in = now < ref_time

                if time_in:
                    with open(path_filename, 'r') as c:
                        cc = c.readlines()
                        remove_files()
                        if BARCODE not in (line.split(',')[0] for line in cc):
                            with open(path_filename, 'a') as d:
                                time_In = now.strftime("%b-%d-%Y-%H:%M")
                                d.writelines(f'\n{BARCODE},{time_In},')
                                print(cc)


                        else:
                            time_In = now.strftime("%b-%d-%Y-%H:%M")
                            data = [f'{BARCODE},{time_In},' if BARCODE in x else x for x in cc]
                            print(data)
                            with open(path_filename, 'w+') as e:
                                e.writelines(data)
                                print(data)


                else:
                    with open(path_filename, 'r') as f:
                        existing_files_by_day = f.readlines()
                        print(existing_files_by_day)
                        if BARCODE in (line.split(',')[0] for line in existing_files_by_day):
                            print("TRUE")
                            time_Out = now.strftime("%b-%d-%Y-%H:%M\n")
                            timeOut_data = [a for a in existing_files_by_day if BARCODE in a]
                            if timeOut_data:
                                s = timeOut_data.append(time_Out)
                                print(s)

                                path_I = 'ATTENDANCE'
                                filename_I = '{}_UPDATED.csv'.format(time.strftime("%Y%m%d"))
                                path_filename_I = pjoin(path_I, filename_I)
                                with open(path_filename_I, 'a+') as files_by_day_append:
                                    with open(path_filename_I, 'r') as i:
                                        ii = i.readlines()
                                        if BARCODE not in (line.split(',')[0] for line in ii):
                                            print("true")
                                            files_by_day_append.writelines(timeOut_data)
                                        else:
                                            print("false")
                        else:
                            print("FALSE")
            break

def remove_files():
    path = 'DO NOT DELETE NOR OPEN'
    max_date = 1
    today = datetime.datetime.now()
    for each_file in os.listdir(path):
        each_fileI = os.path.join(path, each_file)
        if os.path.isfile(each_fileI):
            file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_fileI))
            dif_microsec = (today - file_cre_date).days
            if dif_microsec > max_date:
                os.remove(each_fileI)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
print(cv2.CAP_PROP_FPS)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

arduino = serial.Serial('COM9', 115200, timeout=.1)
fix_con_print = ""
TIMEOUT = .025
old_timestamp = time.time()
prevTime = 0
while True:

    success, eImgs = cap.read()
    if success:
        curTime = time.time()
        sec = curTime - prevTime
        prevTime = curTime
        fps = 200/ (sec)
        display_FPS = "FPS : %0.1f" % fps

        font = cv2.FONT_HERSHEY_PLAIN
        frame = cv2.putText(eImgs, display_FPS, (10, 50), font, 1, (0, 0, 128), 1, cv2.LINE_AA)
        eImgs_v1 = cv2.cvtColor(eImgs, cv2.COLOR_BGR2RGB)
        facesWebcam = face_recognition.face_locations(eImgs_v1)
        encodesWebcam = face_recognition.face_encodings(eImgs_v1, facesWebcam)

        for encodeKnown_v2, faceLoc in zip(encodesWebcam, facesWebcam):
            facesCompared = face_recognition.compare_faces(encodeKnown, encodeKnown_v2)
            faceDistance = face_recognition.face_distance(encodeKnown, encodeKnown_v2)
            faceIndex = np.argmin(faceDistance)


            if facesCompared[faceIndex]:
                eName = ListNames[faceIndex]
                employeeName = eName

                p1, p2, p3, p4 = faceLoc
                cv2.rectangle(eImgs, (p4, p1), (p2, p3), (0, 255, 0), 2)
                cv2.rectangle(eImgs, (p4, p3 - 35), (p2, p3), (0, 255, 0), cv2.FILLED)
                cv2.putText(eImgs, employeeName, (p4-20, p3-7), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                if fix_con_print == "" or fix_con_print != employeeName:
                    fix_con_print = employeeName

                #Will detect if the person is Employee or not
                    if employeeName:
                        print("AUTHORIZED")

                        # You can't scan your barcode unless the system confirms that you are an Employee of the NW.
                        # If the system confirms you as 'AUTHORIZED', this part will tell if your ID is yours or not.
                        time.sleep(1)
                        print("The system is ready!")
                        while True:
                            barcode = arduino.readline()[:-2]
                            strbarcode = barcode.decode('utf-8')
                            if strbarcode:
                                
                                BARCODE = strbarcode
                                print(BARCODE)


                                # Will detect if the Employee is the owner of the barcode
                                if employeeName == BARCODE:
                                    print('Have a nice day!')
                                    timeIn(BARCODE)


                                    print("Next Employee please!")
                                    time.sleep(2)
                                    break

                                else:
                                    print('This is not yours!')
                                    break

                    else:
                        print("UNAUTHORIZED")
                        break

    if (time.time() - old_timestamp) > TIMEOUT:
        cv2.imshow('EMPLOYEE', eImgs)
        cv2.waitKey(1)
        old_timestamp = time.time()

cap.release()
cv2.destroyAllWindows()