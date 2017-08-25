from evidence.theory import dst # load dempster-shafer functions
#from evidenec.tests.assets import INPUT
'''
print INPUT['bba1'] # path for the bba example
bba = []
with open(INPUT['bba1'], 'r') as f:
    N = int(f.readline())
    for _  in range(N):
        bba += [ float(f.readline()) ]

print bba # verify a table with values between 0 and 1
'''
#bba = [0.0, 0.35, 0.25, 0.0, 0.35, 0.25, 0.06, 0.15, 0.05, 0.04, 0.1]
bba = [0.0, 0.3]
print len(bba)
bel1 = dst.Bel(m=bba)
#print bel1(0)
#print type(bel1)

for i in range(len(bba)):
    print i
    print (bel1(i)) # i is a set represents in binary form.