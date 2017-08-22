__author__ = 'crystal'

import pandas as pd
from sklearn.ensemble import IsolationForest
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

#data = pd.read_csv('data/data.csv', index_col="id")
#data = pd.read_csv('/Users/crystal/Documents/iForest/data.csv')
#data = pd.read_csv('data/logon.csv', index_col="employee")
data = pd.read_csv('data/dataforperiod/deviceDisconnect.csv', index_col="employee")
#data = pd.read_csv('data/onehour/connect/connectmax1.csv', index_col="id")
#data = pd.read_csv('data/avgresult.csv', index_col="user")
#connectmaxfile = 'data/onehour/logoff/logoffmode1.csv'
#data = pd.read_csv(connectmaxfile, index_col="id")
data = pd.read_csv('data/dataforperiod/Allfeatures.csv', index_col="id")
print (data.values)
traindata =[]
statelist = []
for item in data.values:
    statelist.append(item[-1])
    traindata.append(item[0:-2])
print(traindata)
print(statelist)

pca=PCA(n_components=2)
newData=pca.fit_transform(traindata)
features =[]
for item in newData:
    for i in item:


data['newfeature'] =newData
print(newData)
#print (data.values[1][1])
'''
n_estimators:样本的数量，默认为100
n_jobs:m默认为1，“fit”和“predict”两个并行运行的作业数，如果为-1，则将作业书设置为核心数
verbose：默认为0，控制建树过程的冗长度
'''


ilf = IsolationForest(n_estimators=100,
                      n_jobs=-1,
                      verbose=2,
    )


#缺少数据填充0
data = data.fillna(0)
# select features
#X_cols = ["age", "salary", "sex"]
#X_cols = ["max(12am-6am)", "mode(12am-6am)", "max(6am-12pm)", "mode(6am-12pm)", "max(12pm-6pm)", "mode(12pm-6pm)", "max(6pm-12am)", "mode(6pm-12am)"]
#X_cols = ["avgresult"]

#max
#X_cols = ["max(12am-6am)", "max(6am-12pm)", "max(12pm-6pm)",  "max(6pm-12am)",]
#mode
#X_cols = [ "mode(12am-6am)", "mode(6am-12pm)",  "mode(12pm-6pm)",  "mode(6pm-12am)"]


#allfeatures
#X_cols = [str(i+1) for i in range(40)]

#all_max（单数）
'''
tem = []
for i in range(20):
        tem.append(str(i*2+1))
print (tem)
X_cols = tem

#all_mode（复数）

tem = []
for i in range(21):
    if i>0:
        tem.append(str(i*2))   
print (tem)
X_cols = tem

print( data.shape)
'''
X_cols = ['newfeature']
# train
print("train begain")
'''
fit(self,x,y=none,sample_weight = none):x:输入的样本；sampleweight：样本的权重，如果没有，则等权重
return self
'''
ilf.fit(data[X_cols])
shape = data.shape[0]
print (shape)
batch = 10**6
print("train over")


all_pred = []
anormal_score = []
for i in range(int(shape/batch+1)):
    start = i * batch
    end = (i+1) * batch
    print(start,end)
    test = data[X_cols][start:end]
    print ("test len:",len(test))
    # predict
    anormalscore = ilf.decision_function(test)
    #print("anormalscore:",anormalscore)
    pred = ilf.predict(test)
    all_pred.extend(pred)
    anormal_score.extend(anormalscore)

data['pred'] = all_pred
data['anormalscore'] = anormal_score
#print (data)
true = 0
false = 0
trueT = 0
trueF = 0
falseT = 0
falseF = 0
print ("all_pred:",all_pred)
normal = []
abnormal = []

i  = 0
#for item in data.values:
#for i in range(len(all_pred)):
for item in statelist:
    state = item
    prestate = all_pred[i]
    i =i+1
    print(state, prestate)

    if state==0:
        #normal.append(item[10])
        true = true+1
        if prestate==1:
            trueT = trueT+1
        if prestate == -1:
            trueF= trueF+1
    if state==1:
        #abnormal.append(item[10])
        false = false+1
        if prestate ==1:
            falseT = falseT+1
        if prestate ==-1:
            falseF = falseF+1

print ("true:",true,"false:",false)
print ('TP:',falseF,'FP:',trueF,'FN:',falseT,'TN:',trueT)
Accuracy = (trueT+falseF)/(false+true)
Precision =falseF/(falseF+trueF)
Recall = falseF/false

print("Accuracy:",Accuracy,"Precision:",Precision,"Recall:",Recall)

print("outlier detect")

#plt.figure("logoff")
figure,ax = plt.subplots()
ax.set_title("logoff")


x1 = [i for i in range(len(normal))]

plt.subplot(121)
plt.title("normal")
plt.xlabel('users')
plt.ylabel('anormalscore')
plt.plot(x1,normal,'b')

x2 = [i for i in range(len(abnormal))]
plt.subplot(122)
plt.title("abnormal")
plt.xlabel('users')
plt.ylabel('anormalscore')
plt.plot(x2,abnormal,'r')

#plt.show()

#data.to_csv('data/outliers.csv', columns=["pred","anormalscore"], header=False)
data.to_csv('data/dataforperiod/outallfeatures.csv', columns=["state","pred","anormalscore"], header=False)
