def  summintervals(a):


 #kataxwrw ta akra twn diasthmatwn se mia lista taxinomontas ta se auxousa seira
    edges = []

    for i in range(len(a)):

                edges.append(a[i][0])
                edges.append(a[i][-1])

    edges.sort()

#lista eswterikwn shmeiwn

    interiors=[]
    k=-1

    for i in range(len(a)):
        k = k + 1
        for j in range(a[k][0]+1,a[k][-1]):
              interiors.append(j)


#diagrafw ta akra pou epikalyptontai anamesa sthn lista twn akrwn
#kai sth lista twn eswterikwn gia na mhn yparxoyn epanalhpseis
    a=set(edges)
    b=set(interiors)

    a.difference_update(b)
    truedges=list(a)
#emfanizw to mhkos tvn diasthmatwn athroizontas tis diafores twn akrwn ana dyo

    s=0
    for i in range(0,len(truedges)-1,2):

        s= truedges[i+1]-truedges[i]+s

    print(s)
summintervals([[1,2],[6,10],[11,15]])
