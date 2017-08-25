import CSVFile
import pandas as pd
import matplotlib.pyplot as plt

def GetallfeaturesUsers():
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


def GetPCA_PR():
    data_list = pd.read_csv('data/dataforperiod/outallfeatures.csv')
    TPR = []
    FPR = []
    RECALL = []
    PRE = []
    thr = -0.4

    for i in range(20000):
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        for item in data_list.values:
            state = item[2]
            presta = item[4]
            #print (state,presta)
            #print (presta,thr)
            if state == 0:
                if presta>thr:
                    tn = tn+1
                else:
                    fp = fp+1

            if state == 1:
                if presta > thr:
                    fn = fn + 1
                else:
                    tp = tp + 1
        #print (tp,fp,fn,tn)
        thr = thr + 0.0001
        #if (tp+fn) == 0 or (fp+tn) == 0:
        if(tp+fn)==0  or (tp + fp) == 0:
            print ('*********')
            continue
        tpr = float(tp)/(float(tp)+float(fn))
        #fpr = float(fp)/(float(fp)+float(tn))
        #print(fpr,tpr)
        recall = tpr
        pre = float(tp)/(float(tp)+float(fp))
        #print(fpr,tpr)
        #print(recall,pre)
        #TPR.append(tpr)
        #FPR.append(fpr)
        RECALL.append(recall)
        PRE.append(pre)


    data = pd.DataFrame()
    #data['FPR'] = FPR
    #data['TPR'] = TPR
    data['RECALL'] = RECALL
    data['PRE'] = PRE
    #data.to_csv('data/dataforperiod/pcarocXY.csv')
    data.to_csv('data/dataforperiod/pcaPRXY.csv')
    #print (thr)
    plt.figure()
    #plt.plot(FPR,TPR,'r')
    plt.plot(RECALL, PRE, 'c')
    x=[0,1]
    y=[1,0]
    plt.plot(x,y,'b')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.show()

def GetPCA_Roc():
    data_list = pd.read_csv('data/dataforperiod/outallfeatures.csv')
    TPR = []
    FPR = []
    RECALL = []
    PRE = []
    thr = -0.4

    for i in range(20000):
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        for item in data_list.values:
            state = item[2]
            presta = item[4]
            #print (state,presta)
            #print (presta,thr)
            if state == 0:
                if presta>thr:
                    tn = tn+1
                else:
                    fp = fp+1

            if state == 1:
                if presta > thr:
                    fn = fn + 1
                else:
                    tp = tp + 1
        #print (tp,fp,fn,tn)
        thr = thr + 0.0001
        if (tp+fn) == 0 or (fp+tn) == 0:
        #if(tp+fn)==0  or (tp + fp) == 0:
            print ('*********')
            continue
        tpr = float(tp)/(float(tp)+float(fn))
        fpr = float(fp)/(float(fp)+float(tn))
        print(fpr,tpr)
        #recall = tpr
        #pre = float(tp)/(float(tp)+float(fp))
        #print(fpr,tpr)
        #print(recall,pre)
        TPR.append(tpr)
        FPR.append(fpr)
        #RECALL.append(recall)
        #PRE.append(pre)


    data = pd.DataFrame()
    data['FPR'] = FPR
    data['TPR'] = TPR
    data.to_csv('data/dataforperiod/pcarocXY.csv')
    print (thr)
    plt.figure()
    plt.plot(FPR,TPR,'r')
    #plt.plot(RECALL, PRE, 'y')
    x=[0,1]
    y=[0,1]
    plt.plot(x,y,'b')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.show()
if __name__ == '__main__':
    #test = pd.read_csv('./data/datatest.csv')
    #print(test.values)
    #GetPCA_Roc()
    GetPCA_PR()
