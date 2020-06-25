import time

def maxdensity(dic): #density of subgraph
    a=0
    if(len(dic)==0):
        return a
    for i in dic.keys():
        a+=len(dic[i])
    a=a/(2.0*len(dic))
    return a

# counter is minimum degree in subgraph
def f_pop(counter):
    tobedel=[]
    for i in deg.keys():
        if(deg[i]==counter):
            tobedel.append(i)
    for k in tobedel:
        for j in dic[k]:
            (dic[j]).remove(k)
            deg[j]=deg[j]-1
        del dic[k]
        del deg[k]


edges = []
deg={}
dic={}
start_time = time.clock()
file = open("edges.txt","r")
edges=file.readlines()
for i in edges:
    edge=list(map(int,i.split()))
    if edge[0] not in dic.keys():
        dic[edge[0]]=[]
        deg[edge[0]]=0
    dic[edge[0]].append(edge[1])
    deg[edge[0]]+=1

    if edge[1] not in dic.keys():
        dic[edge[1]]=[]
        deg[edge[1]]=0
    dic[edge[1]].append(edge[0])
    deg[edge[1]]+=1

file.close()

#main
start_time = time.clock()
maxdens=0
maxdensf=0
subgraph=[]
while(len(deg)>0):
    mindeg=float('inf')
    for i in deg.keys():
        mindeg= min(deg[i],mindeg)
    f_pop(mindeg)
    list = []
    for key in dic.keys():
        list.append(key)

    print('Subgraph after deletion of least degree node: ',list)
    maxdens=maxdensity(dic)

    print('Density of this subgraph is: ', maxdens,'\n')

    if(maxdens>maxdensf):
        maxdensf=maxdens
        subgraph=list

print('\nTime elapsed: ',time.clock() - start_time)
print('\nThe densest subgraph is: ',subgraph)
print('The density of the subgraph is: ', maxdensf)