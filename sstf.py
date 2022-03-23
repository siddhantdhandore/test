def SSTF(referenceArray,head):
    maxer=max(referenceArray)
    visited=0
    currentHead=head
    refPointer=0
    totalSeekTime=0
    while visited!=len(referenceArray):
        minDistance=maxer
        for i in range(visited,len(referenceArray)):
            currentReference=referenceArray[i]
            if abs(currentReference-currentHead) <= minDistance:
                minDistance=abs(currentReference-currentHead)
                refPointer=i
        totalSeekTime+=minDistance
        print(currentHead,"to",referenceArray[refPointer],"=",minDistance)
        currentHead=referenceArray[refPointer]
        referenceArray[refPointer],referenceArray[visited]=referenceArray[visited],referenceArray[refPointer]
        visited+=1
    print("Total Seek Time :",totalSeekTime)
    print("Average Seek Time : ", totalSeekTime/len(referenceArray))

referenceArray=list(map(int,input("Enter space seperetd Reference String : ").split()))
head=int(input("enter head : "))
print()
SSTF(referenceArray,head)
