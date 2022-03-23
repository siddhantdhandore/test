def SCAN(referenceString,start,head,end):
    minFromRef=min(referenceString)
    maxFromRef=max(referenceString)
    referenceString=sorted(referenceString)
    
    #validation of user input
    if(start>minFromRef):
        return "start should be less than minFromRef",minFromRef
    elif(end<maxFromRef):
        return "end should be larger than minFromRef",maxFromRef
    elif(head<start or head>maxFromRef):
        return "Invalid Head"

    currentHead=head
    leftStart=start
    totalSeekTime=0
    leftString=""
    rightString=""
    for i in range(len(referenceString)):
        currentRef=referenceString[i]
        if currentRef<head:
            dist=currentRef-leftStart
            leftString= "\nfrom %s to %s = %d"%(currentRef,leftStart,dist)+leftString
            currentHead=currentRef
            leftStart=currentHead
            
        elif currentRef>head:
            if currentHead < head:
                leftString= "\nfrom %s to %s = %d"%(head,currentHead,head-currentHead)+leftString
                totalSeekTime+=head-currentHead
                currentHead=start
            dist=currentRef-currentHead
            rightString+="from %s to %s = %d\n"%(currentHead,currentRef,dist)
            currentHead=referenceString[i]
        totalSeekTime+=dist
    print(leftString)
    print(rightString)
    print("totalSeekTime : ",totalSeekTime)
    print("Avg. Seek Time : ", totalSeekTime/(len(referenceString)+1))
referenceString=[176, 79, 34, 60, 92, 11, 41, 114]
start=0
head=50
end=199
SCAN(referenceString,start,head,end)
