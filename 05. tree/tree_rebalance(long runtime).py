import random

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None
class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = None
    def search(self, item,depth):
        if self.head.val is None:
            return None
        else:
            return self.__search_node(self.head, item,depth)
    def __search_node(self, cur, item, depth):
        if cur is None :
            return None,None
        if cur.val[0] == item:
            return cur,depth
        else:
            if cur.val[0].lower() >= item.lower():
                depth=depth+1
                return self.__search_node(cur.left, item,depth)
            else:
                depth=depth+1
                return self.__search_node(cur.right, item,depth)
        return None
    def insert(self, item):
        if self.head is None:
            self.head = Node(item)
        
        else:
            self.__insert_node(self.head, item)
    def __insert_node(self, cur, item):
      
        if cur.val[0].lower() >= item[0].lower():
            if cur.left is not None:
                self.__insert_node(cur.left, item)
            else: cur.left = Node(item)
          
        else:
            if cur.right is not None:
                self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)
    def get_height(self,root):
        if root is None:
            return 0
        return 1+max(self.get_height(root.left), self.get_height(root.right))
    def count_node(self,root):
        if root is None:
            return 0
        else:
            return 1 + self.count_node(root.left) + self.count_node(root.right)
class Balanced_BinaryTree:
    def __init__(self):
        self.head= None
    def search(self, item,depth):
        if self.head.val is None:
            return None
        else:
            return self.__search_node(self.head, item,depth)
    def __search_node(self, cur, item, depth):
        if cur is None :
            return None,None
        if cur.val[0] == item:
            return cur,depth
        else:
            if cur.val[0].lower() >= item.lower():
                depth=depth+1
                return self.__search_node(cur.left, item,depth)
            else:
                depth=depth+1
                return self.__search_node(cur.right, item,depth)
        return None
    #head 기준으로 right쪽에 넣으면 넣은 레벨부터 head까지 balance 작업 left도 동일
    def insert(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            
            self.head = self.__insert_node(self.head, item)

    
    def __insert_node(self, cur, item):
        
        if cur.val[0] >= item[0]:
            if cur.left is not None:
                cur.left = self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        
        else:
            if cur.right is not None:
                cur.right = self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)

   
        return self.balance(cur)

 
    def balance(self, cur):
        
        left_height = self.get_height(cur.left)
        right_height = self.get_height(cur.right)
        #right balanced
        if left_height - right_height < -1:
            #right left balanced"
            if self.get_height(cur.right.right) - self.get_height(cur.right.left) < 0:
                return self.RLrotate(cur)
            else:
                return self.RRrotate(cur)
        #left balanced
        elif left_height - right_height > 1:
            #left right balanced
            if self.get_height(cur.left.left) - self.get_height(cur.left.right) < 0:
                return self.LRrotate(cur)
            else:
                return self.LLrotate(cur)
        return cur

    def LLrotate(self, cur):
        L = cur.left
        cur.left = L.right
        L.right = cur
        return L
    def LRrotate(self,cur):
        L = cur.left
        LR = L.right
        cur.left = LR.right
        LR.right = cur
        L.right= LR.left
        LR.left=L
        
        return LR
    def RRrotate(self, cur):
        R = cur.right
        cur.right = R.left
        R.left = cur
        return R

    def RLrotate(self, cur):
        R = cur.right
        RL = R.left
        cur.right = RL.left
        RL.left = cur
        R.left = RL.right
        RL.right = R
        
        return RL


    def get_height(self, root):
        if root is None: 
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

      
              
        
            
            
file_name='randdict_utf8.TXT'
data=open(file_name,'r',encoding='UTF8')
line=data.readline()
dictionary=BinaryTree()
balance_dictionary = Balanced_BinaryTree()
#랜덤한 10개의 영단어를 뽑아낼 english
english = []
num=1
while line:
    lines=(line[:-1])
    line=data.readline() 
    a=line.split(':')
    a[0]=a[0][:-1]
    if len(a) == 1:
        continue
    a[1]=a[1][:-1]
    dictionary.insert(a)
    english.append(a[0])
    balance_dictionary.insert(a)
    print(num)
    num+=1
data.close()

print('사전 파일을 모두 읽었습니다.',dictionary.count_node(dictionary.head),'개의 단어가 있습니다.')
print('A 트리의 전체 높이는',dictionary.get_height(dictionary.head),'입니다.')
#리스트속 겹치지 않게 10개뽑는 것!
item = random.sample(english,10)

print('랜덤하게 선택된 단어 10개 : ', end='')
for i in range(10):
    print(item[i],' ',end='')
print('')


for i in range(10):
    depth=1
    node, depth = dictionary.search(item[i],depth)
    print(node.val[0], node.val[1], '( 레벨',depth,')')

print('B 트리의 전체 높이는',balance_dictionary.get_height(balance_dictionary.head),'입니다.')

for i in range(10):
    depth=1
    node, depth = balance_dictionary.search(item[i],depth)
    print(node.val[0],node.val[1],'( 레벨',depth,')')
    
