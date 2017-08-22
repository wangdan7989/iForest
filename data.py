import CSVFile
import pandas as pd

data_disconnect = pd.read_csv('data/dataforperiod/deviceDisconnect.csv')
data_connect = pd.read_csv('data/dataforperiod/deviceConnect.csv')
data_file = pd.read_csv('data/dataforperiod/filecount.csv')
data_logon = pd.read_csv('data/dataforperiod/logon.csv')
data_logoff = pd.read_csv('data/dataforperiod/logoff.csv')
#print (type(data))
allinfo=[]
for item_connect in data_connect.values:
    user_connect = item_connect[0]

    for item_disconnect in data_disconnect.values:
        user_disconnect = item_disconnect[0]
        if user_connect !=user_disconnect:
            continue

        for item_file in data_file.values:
            user_file = item_file[0]
            if user_file !=user_disconnect:
                continue

            for item_logon in data_logon.values:
                user_logon = item_logon[0]
                if user_logon!=user_file:
                    continue

                for item_logoff in data_logoff.values:
                    user_logoff = item_logoff[0]
                    if user_logoff != user_logon:
                        continue
                    tem = []
                    tem.extend(item_connect[0:9])
                    tem.extend(item_disconnect[1:9])
                    tem.extend(item_file[1:9])
                    tem.extend(item_logon[1:9])
                    tem.extend(item_logoff[1:10])
                    allinfo.append(tem)
print (len(allinfo))
print (allinfo)
CSVFile.Writecsvtofile('data/dataforperiod/Allfeatures.csv',allinfo)
for item in allinfo:
    print (item)
    #print(item[0])