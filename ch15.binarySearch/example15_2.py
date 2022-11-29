n = int(input())

data = list(map(int,input().split()))


def bi(data,start,end):
    
    if start > end:
        return -1
    
    tar = (start+end)//2
    
    if data[tar] == tar:
        return tar
     
    if data[tar] > tar:
        if data[start] <= start:
            return bi(data,start,end-1)
        elif data[end] >= end:
            return bi(data,tar+1,end)
    else:
        if data[start] >= start:
            return bi(data,start,end-1)
        elif data[end] >= end:
            return bi(data,tar+1,end)
        
        
print(bi(data,0,n-1))
    
        