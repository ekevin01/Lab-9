#the authors names are Isa Grace and Ellen Kevin
def replace_substring(x,y,z):
    output=[]
    index=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=len(y)
            output.append(z)
        else:
            output.append(x[index])
            index+=1
    print("".join(output))

string="PLeaseTwinkle Twinkle little PLeasestar"
replace_substring(string,"PLease","yay")

string="woahhhhhhhno thats awesomeno"
replace_substring(string,"no","YES!")
