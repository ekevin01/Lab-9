#the authors names are Isa Grace and Ellen Kevin

def remove_substring(x,y):
    output=[]
    index=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=len(y)
        else:
            output.append(x[index])
            index+=1
    print("".join(output))

string="PLeaseTwinkle Twinkle little PLeasestar"
remove_substring(string,"PLease")
