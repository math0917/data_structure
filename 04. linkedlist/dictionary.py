
class Node :
  def __init__(self, data, next=None):
      self.data = data
      self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node
# insert sort를 새로 정의 내부 구현은 bubble sort처럼 원소 하나씩 비교해가며 자기 위치를 찾아가는 방식
    def insert_sort(self,elem):
        if self.head==None:
            self.head=elem
        else:
            before=self.head
            if before.data[0]<elem.data[0]:
                cur=before.next
                while cur != None:
                    if cur.data[0]<elem.data[0]:
                        cur=cur.next
                        before=before.next
                    else:
                        break
                elem.next=cur
                before.next=elem
            else:
                elem.next=self.head
                self.head=elem

            

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before is None:
            removed = self.head
            self.head = self.head.next
        else :
            removed = before.next
            before.next = before.next.next
        del removed

    def display(self):
        node = self.head
        while node is not None:
            print(node.data, end="->")
            node = node.next      
    def finding(self,elem):
        if self.head==None:
            return 0
        else:
            cur=self.head
            while cur!=None:
                if elem==cur.data[0]:
                    return cur.data[1]
                cur=cur.next
            return 0
file_name='randdict_utf8.TXT'
alphabet='abcdefghijklmnopqrstuvwxyz'
dictionary=[] 
num=1
#이제 dictionary를 26 * 27 * 27리스트를 만들고 그 곳에 LinkedList()객체 생성
for i in range(26):
    dictionary.append([])
    for j in range(27):
        dictionary[i].append([])
        for k in range(27):
            dictionary[i][j].append(LinkedList())
data=open(file_name,'r',encoding='UTF8')
line=data.readline()
while line:
  
    lines=(line[:-1])
    line=data.readline() 
    a=line.split(':')
    a[0]=a[0][:-1]
    if len(a)==1:
        continue
    node=Node(a)
    row=alphabet.index(a[0][0].lower())
    try:
        col=alphabet.index(a[0][1].lower())+1
    except:
        col=0
    try:
        hei=alphabet.index(a[0][2].lower())+1
    except:
        hei=0
    dictionary[row][col][hei].insert_sort(node)
    num=num+1
    print(num,'번째 단어 추가')
# 위의 작업은 과제 설명에 적어 놓겠습니다.
data.close()

'''
검색과 추가가 용이한지 판단해보겠습니다.
1. 검색 : 우선 검색 또한 연결리스트속 존재하는지 하나하나 확인 해야 하는데
이런식으로 각각의 연결리스트당 원소가 적게 들어갈 수 있도록 설계를 해놓으면
검색이 빠르고 용이합니다. 배열의 특정 요소에 빠르게 접근할 수 있는 장점을 
dictionary[row][col][hei]를 통하여 얻을 수 있었습니다.
2. 추가 : 추가 또한 그저 배열로만 사전을 하면 뒤로 미루는 작업이 필요하지만
결국 이러한 구현은 연결리스트로 이루어 져있기에 그저 앞뒤의 포인터방향만 바꿔
주면 추가가 되므로 연결리스트의 장점을 이용 할 수 있었습니다.
고로 이 방법은 배열의 장점과 연결리스트의 장점을 mix한 방법이 됐습니다.!
'''
while(1):
    word=input('단어를 입력해주세요')
    row=alphabet.index(word[0].lower())
    plus=[]
    try:
        col=alphabet.index(word[1].lower())+1
    except:
        col=0
    try:
        hei=alphabet.index(word[2].lower())+1
    except:
        hei=0
    node=dictionary[row][col][hei].finding(word)
    if node==0:
        mean=input('찾을수 없는 단어입니다. 뜻을 추가하세요(추가하지 않으려면 공백')
        if mean=='':
            continue
        else:
            plus.append(word)
            plus.append(mean)
            print(word,mean,',',row,col,hei,'에 추가')
            node=Node(plus)
            dictionary[row][col][hei].insert_sort(node)
            
    else:
        print(node)

