def FCFS(referenceString,head):
    currentHead=head
    totalSeekTime=0
    headString=str(currentHead)+"-> "
    for currentRef in referenceString:
        headString+=str(currentRef)+'-> '
        totalSeekTime+=abs(currentHead-currentRef)
        currentHead=currentRef
    print(headString)
    print("Avg. Seek Time : ",totalSeekTime/len(referenceString))
def SSTF(referenceString,head):
    currentHead=head
    referencePointer=0
    totalSeekTime=0
    lengthOfReferenceString=len(referenceString)
    headString=str(currentHead)+"-> "
    while referenceString!=[]:
        minDistance=max(referenceString)
        for i in range(len(referenceString)):
            currentRef=referenceString[i]
            if currentHead!=currentRef:
                if(abs(currentHead-currentRef)<minDistance):
                    minDistance=abs(currentHead-currentRef)    
                    referencePointer=i
        headString+=str(referenceString[referencePointer])+'-> '
        currentHead=referenceString[referencePointer]
        totalSeekTime+=minDistance
        referenceString=referenceString[:referencePointer]+referenceString[referencePointer+1:]
    print(headString)
    print("Avg. Seek Time : ",totalSeekTime/lengthOfReferenceString)
SSTF([176, 79, 34, 60, 92, 11, 41, 114],50)
