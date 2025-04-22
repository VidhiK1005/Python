l=[(101,'amit',35,'HR',60000),(102,'vidhi',34,'HR',20000),(103,'manya',33,'marketing',30000)]

def filterbydept():
    nd=[]
    n=str(input('enter department:'))
    for i in l:
        if i[3]==n:
            nd.append(i[1])
    print(nd)

filterbydept()

def sortbysalary():
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][4]<l[j][4]:
               l[i],l[j]=l[j],l[i]
    print(l)
sortbysalary() 