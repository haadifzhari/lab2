memory = [50, 30, 700, 200, 980]
programs = [20, 200, 500, 50]

block = []
for x in range(0, len(memory)): #append all block equal to -1, depends on the memory length
    block.append(-1)

print("Block Number \t Size")  
for z in range(0, len(memory)):
    print(z, "\t\t\t\t", memory[z])  #print block number  with its size
print()

for y in range(0, len(programs)): #assign the programs to block (programs < memory)
    for z in range(0, len(memory)): #check one by one
        if programs[y] <= memory[z]:
            block[y] = z
            for f in range(z+1, len(memory)):
                if memory[z] > memory[f] and programs[y] <= memory[f]:
                    block[y] = f
                    break
            break

print("Process size \tBlock number") #print result
for y in range(0, len(programs)):
    print((y+1), "\t", programs[y], end="\t\t\t")
    if block[y] != -1:   #if block != -1, block is occupied, check sequentially
        print(block[y])
    else:
        print("Blocks not allocated")
