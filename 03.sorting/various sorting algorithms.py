import random
import time
import copy



#selection sort
def selection_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j][1]>arr[j-1][1]:
                break
            else:
                arr[j],arr[j-1]=arr[j-1],arr[j]
#quick sort
def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr, pivot+1, high)

def partition(arr,pivot,high):
    value=arr[pivot][1]
    i=pivot+1
    for j in range(pivot+1,high+1):
        if arr[j][1]<value:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i-1],arr[pivot]=arr[pivot],arr[i-1]
    return i-1

#heap_sort
def adjust(a, i, size):
    while 2 * i + 1<= size:
        k = 2 * i + 1
        if k < size and a[k][1] < a[k+1][1]:   # a[2i]와 a[2i+1]중 a[2i+1]이 더 크다면 a[2i+1]이 위로 가야.
            k += 1

        if a[i][1] >= a[k][1]: #a[i]와 a[2i]중 a[i]가 크면 빠져나가
            break
        a[i], a[k] = a[k], a[i]  
        i = k


def heap_sort(a):
    h_size = len(a) - 1
    if h_size%2==1:
        for i in reversed(range(0, int(h_size/2+1))):
            adjust(a, i, h_size)
    else:
        for i in reversed(range(0, int(h_size/2))):
            adjust(a, i, h_size)
    for i in range(h_size) :
        a[0], a[h_size] = a[h_size], a[0]
        adjust(a,0, h_size-1)
        h_size -= 1
            
alphabet='abcdefghijklmnopqrstuvwxyz'
a=[]
student_id=[]
start=time.time()
for i in range(9):
    a.append([])
    for j in range(1000):
        a[i].append([0,0,0,0,0,0,0,0,0,0])
    
for i in range(50000):
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
    student_id.append([number,name,phone_num])
print(time.time()-start,'랜덤 생성 소요시간!')
#첫번째 검사 방법
flag=1
data=[]
start=time.time()
for i in range(9):
    for j in range(1000):
        for k in range(10):
            if a[i][j][k]>1:
                flag=0
                break
    flag=1
end=time.time()-start
print('검사 시간',end)
if flag:
    print('중복된 학번 존재 x')
else:
    print('중복된 학번 존재 합니다.')        
#두번째 검사 방법           
start=time.time()
for i in range(len(student_id)):
    data.append(student_id[i][0])
data_set=set(data)
if len(data_set)==len(data):
    end=time.time()-start
    print('검사 시간',end)
    print('겹치는 학번은 없네요')

student_id_copy2=copy.deepcopy(student_id)    
student_id_copy=copy.deepcopy(student_id)
start_time=time.time()
array=sorted(student_id,key= lambda x: x[1])
end_time=time.time()-start_time

for num in range(50):
    idx=1+num*1000
    print('%d번 : [ %s , %s , %s ], '%(idx, array[idx][0],array[idx][1],array[idx][2]),end='')
print('')
print('python 내장 sort알고리즘을 쓰면 ',end_time,'초가 걸려요!')

start_time=time.time()
selection_sort(student_id)
end_time=time.time()-start_time
print('')
print('selection sort를 쓰면',end_time,'초가 걸려요!')
for num in range(50):
    idx=1+num*1000
    print('%d번 : [ %s , %s , %s ], '%(idx, student_id[idx][0],student_id[idx][1],student_id[idx][2]),end='')
print('')
start_time=time.time()
quick_sort(student_id_copy,0,len(student_id_copy)-1)
end_time=time.time()-start_time
print('')
print('quick sort를 쓰면',end_time,'초가 걸려요!')
for num in range(50):
    idx=1+num*1000
    print('%d번 : [ %s , %s , %s ], '%(idx, student_id_copy[idx][0],student_id_copy[idx][1],student_id_copy[idx][2]),end='')

print('')
start_time=time.time()
heap_sort(student_id_copy2)
end_time=time.time()-start_time
print('')
print('heap sort를 쓰면',end_time,'초가 걸려요!')
for num in range(50):
    idx=1+num*1000
    print('%d번 : [ %s , %s , %s ], '%(idx, student_id_copy2[idx][0],student_id_copy2[idx][1],student_id_copy[idx][2]),end='')
print('')
flag=0
for i in range(len(student_id)-1):
    if student_id[i][1]>student_id[i+1][1]:
        flag=1
        break
if flag==1:
    print('selection sort 정렬 상태 불량')
else:
    print('selection sort 정렬 완료')

flag=0
for i in range(len(student_id)-1):
    if student_id_copy[i][1]>student_id_copy[i+1][1]:
        flag=1
        break
if flag==1:
    print('quick sort 정렬 상태 불량')
else:
    print('quick sort 정렬 완료')

flag=0
for i in range(len(student_id)-1):
    if student_id_copy2[i][1]>student_id_copy2[i+1][1]:
        flag=1
        break
if flag==1:
    print('heap sort 정렬 상태 불량')
else:
    print('heap sort 정렬 완료')
