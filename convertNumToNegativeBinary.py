
num = int(input("enter a positive number "))
memory = int(input("enter the size of the number memory by BITS "))
binaryList = [int(0)] * (memory)
def convertToBinary(num):

    for i in range(memory):
        if 2 ** (memory-(i+1))<=num:
            num = num - 2**(memory-(i+1))
            binaryList[i] = 1

convertToBinary(num)

#print(binaryList)
for i in range(len(binaryList)):
    if binaryList[i] == 0:
        binaryList[i] = 1
    else:
        binaryList[i] = 0
#print(binaryList)
i=0
bool = False
while bool==False and i<memory:
    if binaryList[-(i+1)] == 0:
        binaryList[-(i+1)] = 1
        bool = True
    else:
        binaryList[-(i+1)] = 0
        i+=1

#print(binaryList)

binaryNum = int(0)
for j in range(memory):       
    binaryNum = binaryNum * 10 + binaryList[j]    

print(binaryNum)