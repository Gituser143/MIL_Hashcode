with open('density.txt','r') as f:
    l=f.readlines()
    l1,l2,l3,l4,i=[int(x.strip()) for x in l]
    t=1+l1+l2+l3+l4
    l=[l1,l2,l3,l4]
    ti=(float(l[i])/float(t))*60+10
#    print(l[i],ti)
with open('t.txt','w') as o:
    o.write(str(i)+' '+str(ti)+' ')
