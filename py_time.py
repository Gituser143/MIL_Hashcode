with open('density.txt','r') as f:
    l=f.readlines()
    l1,l2,l3,l4=[int(x.strip()) for x in l]
    t=l1+l2+l3+l4
    t1=(l1/t)*60+10
    t2=(l2/t)*60+10
    t3=(l3/t)*60+10
    t4=(l4/t)*60+10
with open('t.txt','a+') as o:
    o.write(str(t1)+' ')
    o.write(str(t2)+' ')
    o.write(str(t3)+' ')
    o.write(str(t4)+' ')
