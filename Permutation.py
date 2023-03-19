def permutation(lst):
    if len(lst) == 0:   #檢查是否為空
        return []       #傳回空列表，不做任何事
    
    if len(lst) == 1:   #檢查是否只有一個元素
        return [lst]    #回傳自己的列表(單一元素)
    
    l = []              #如果lst不為空且包含多個元素，用空的list來儲存
    
    for i in range(len(lst)):
        m = lst[i]      # m 來代表所在目前的數值
        remLst = lst[:i] + lst[i+1:]  #在遍歷lst中的每個元素時，都會創建一個新列表remLst
                                      #此列表利用切片方式，記錄了所在位置之前 及 所在位置之後的所有元素
        
        for p in permutation(remLst):  #利用遞迴呼叫permutation()來計算remList這個切片中的所有元素
            l.append([m] + p)          #將目前所在的數值m添加到每個排列的前面，p列表接在後面，一同放進l中
    return l                           #當for迴圈遍歷完所有元素後，函數將返回包含所有列表的l
data = list('123')
for p in permutation(data):
    print(p)

