def combine(nums,path,start,r) :
    if(len(path)==r):
        print(sum(path))
        return
    for i in range(start,len(nums)):
        path.append(nums[i]);
        combine(nums,path,start+1,r)
        path.pop()

def permute(nums,path,used,r):
    if(len(path)==r):
        #print(path)
        result.append(path[:])
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i]=True
        path.append(nums[i])
        permute(nums,path,used,r)
        path.pop()
        used[i]=False
nums=[1,2,3,4]
# combine(nums,[],0,3)
result=[]
permute(nums,[],[False]*len(nums),2)



print(result)