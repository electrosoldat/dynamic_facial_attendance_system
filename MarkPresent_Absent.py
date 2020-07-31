total_database = 'C:/Users/Tavish Chadha/PycharmProjects/FACIALRECOGNITION/venv/VIDEO_Database.csv'
total_present = 'C:/Users/Tavish Chadha/PycharmProjects/FACIALRECOGNITION/venv/VIDEO_Attendance_Present.csv'

def compare_Lists(present_now,database):
    nameList = []
    presentlist = []
    with open('VIDEO_Database.csv','r') as f:
        myDataList = f.readlines()

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[1])

    with open('VIDEO_Attendance_Present.csv','r') as f:
        myPresentList = f.readline()
        for line in myPresentList:
            entry = line.split(',')
            presentlist.append(entry[0])

    with open('VIDEO_Attendance_Absent.csv','w+') as f:
        count = 1
        for name in nameList:
            if name not in presentlist:
                f.writelines(f'{count},{name}')
                count += 1

compare_Lists(total_present,total_database)