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
def tree_data(dictionary,data,left,right):
    if left>right:
        return
    mid = (left+right)//2
    dictionary.insert(data[mid])
    tree_data(dictionary,data,left,mid-1)
    tree_data(dictionary,data,mid+1,right)
    
    
file_name='randdict_utf8.TXT'
data=open(file_name,'r',encoding='UTF8')
line=data.readline()
dictionary=BinaryTree()

english=[]
num=1
dict_english=[]
while line:
    lines=(line[:-1])
    line=data.readline() 
    a=line.split(':')
    a[0]=a[0][:-1]
    if len(a) == 1:
        continue
    a[1]=a[1][:-1]
    english.append(a)
    dict_english.append(a[0])
data.close()
english = sorted(english,key=lambda x :x[0].lower())
print(len(english))
tree_data(dictionary,english,0,len(english)-1)
print(dictionary.count_node(dictionary.head))

print('사전 파일을 모두 읽었습니다.',dictionary.count_node(dictionary.head),'개의 단어가 있습니다.')
print('A 트리의 전체 높이는',dictionary.get_height(dictionary.head),'입니다.')
#리스트속 겹치지 않게 10개뽑는 것!
item = random.sample(dict_english,10)

print('랜덤하게 선택된 단어 10개 : ', end='')
for i in range(10):
    print(item[i],' ',end='')
print('')


for i in range(10):
    depth=1
    node, depth = dictionary.search(item[i],depth)
    print(node.val[0], node.val[1], '( 레벨',depth,')')


    
