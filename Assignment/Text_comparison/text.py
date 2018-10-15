target_string="me thinks it is like a weasel"
length=len(target_string)

while True:
    index=0
    count=0
    input_string = input("please input the string: ")
    input_string = input_string.strip()
    for character in input_string:
        if index<=length-1:
            if character==target_string[index]:
                count+=1
                print(character)
            index+=1
    print("match character:"+str(count))
    print("Fitness is "+str(count)+"/"+str(length)+"= "+str(count/length*100)+"%"+"\n")


