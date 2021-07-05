import random
import time

class Node :
  def __init__(self, data, next_num=None,next_name=None,):
      self.data = data
      self.next_num=next_num
      self.next_name = next_name
class LinkedList:
    def __init__(self):
        self.head_num = None
        self.head_name=None
    def getNode_name(self, pos):
        if pos < 0 : return None
        node = self.head_name
        while pos > 0 and node != None :
            node = node.next_name
            pos -= 1
        return node
    def getNode_num(self, pos):
        if pos < 0 : return None
        node = self.head_num
        while pos > 0 and node != None :
            node = node.next_num
            pos -= 1
        return node
    def insert_sort(self,elem):
        if self.head_num==None:
            self.head_num=elem
        else:
            before=self.head_num
            if before.data[0]<elem.data[0]:
                cur=before.next_num
                while cur != None:
                    if cur.data[0]<elem.data[0]:
                        cur=cur.next_num
                        before=before.next_num
                    else:
                        break
                elem.next_num=cur
                before.next_num=elem
            else:
                elem.next_num=self.head_num
                self.head_num=elem
        if self.head_name==None:
            self.head_name=elem
        else:
            before=self.head_name
            if before.data[1]<elem.data[1]:
                cur=before.next_name
                while cur != None:
                    if cur.data[1]<elem.data[1]:
                        cur=cur.next_name
                        before=before.next_name
                    else:
                        break
                elem.next_name=cur
                before.next_name=elem
            else:
                elem.next_name=self.head_name
                self.head_name=elem

    def display_name(self):
        num=1
        node = self.head_name
        while node is not None:
            if num%100==0:
                print(num,':',node.data, end="->")
            node = node.next_name
            num+=1
        print()    
    def display_num(self):
        num=1
        node = self.head_num
        while node is not None:
            if num%100==0:
                print(num,':',node.data, end="->")
            node = node.next_num
            num=num+1
        print()
    def check_sort_name(self):
        flag=1
        node=self.head_name
        while node.next_name is not None:
            if node.data[1]>node.next_name.data[1]:
                flag=0
            node=node.next_name
        return flag
    def check_sort_num(self):
        flag=1
        node=self.head_num
        while node.next_num is not None:
            if node.data[0]>node.next_num.data[0]:
                flag=0
            node=node.next_num
        return flag
alphabet='abcdefghijklmnopqrstuvwxyz'
a=[]
student_id=LinkedList()

for i in range(9):
    a.append([])
    for j in range(1000):
        a[i].append([0,0,0,0,0,0,0,0,0,0])
start=time.time()
for i in range(10000):
    num=random.randint(13,21)
    idx=num-13
    while(1):
        thousands=random.randint(0,9999)
        in_idx=thousands//10
        compare=thousands-in_idx*10
        if a[idx][in_idx][compare]==1:
            continue
        break
    a[idx][in_idx][compare]+=1
    if thousands>=1000:
        number='20'+str(idx+13)+str(thousands)
    elif thousands>=100:
        number='20'+str(idx+13)+'0'+str(thousands)
    elif thousands>=10:
        number='20'+str(idx+13)+'00'+str(thousands)
    else:
        number='20'+str(idx+13)+'000'+str(thousands)
    name=''
    for j in range(10):
        alpha_idx=random.randint(0,25)
        name+=alphabet[alpha_idx]
    phone_num='010-'
    for k in range(8):
        if k==4:
            phone_num+='-'
        phone_num+=str(random.randint(0,9))
    student=Node([number,name,phone_num])
    student_id.insert_sort(student)
    print(i+1,'번째 학생 추가중')
while(1):
    print('(1) 학번순')
    print('(2) 이름순')
    ans=input('메뉴 선택(0: 종료) : ')
    if ans=='0':
        break
    elif ans=='1':
        if student_id.check_sort_num():
            print('학번순으로 출력해드립니다.')
            student_id.display_num()
    elif ans=='2':
        if student_id.check_sort_name():
            print('이름순으로 출력해드립니다.')
            student_id.display_name()
    else:
        print('입력 다시하세용')
