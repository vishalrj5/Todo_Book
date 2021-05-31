# lst=[]
# class employee:
#     def __init__(self,eid,ename,desig):
#         self.eid=eid;
#         self.ename=ename;
#         self.desig=desig;
#     def __str__(self):
#         return self.ename +" "+self.desig;
#     def display(self):
#         print(self.eid,self.ename,self.desig)
# i=0
# asd=True
# while asd:
#     eid=int(input("Enter the id\n"))
#     ename=input("Enter name\n")
#     desig=input("Enter Desig\n")
#     ob=employee(eid,ename,desig)
#     # ob.display()
#     lst.append(ob)
#     design = list(filter(lambda emp: emp.desig == "developer", lst))
#     for emp in design:
#         print(emp, "IS A DEVELOPER", "\n")
#     i=int(input("o to Exit and 1 to input"))
#     if(i==1):
#         asd=False

st={10,20,30,40,40,30}
st1={40,50,60,70,80,90}

un=st.union(st1)
print(un)

inter=st.intersection(st1)
print(inter)

diff=st.difference(st1)
print(diff)