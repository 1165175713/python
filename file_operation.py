with open(filename,'rb') as fr:
    with open(filename1,'wb') as fw:
        while True:
            con=fr.read(1) #size=1; con is a bytes array
            if con == b'': #when size>1 , this judge 
                break 
            fw.write( con )
            
#reference: http://c.biancheng.net/view/2545.html
#           https://zhuanlan.zhihu.com/p/78330811 
