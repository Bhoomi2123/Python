list = ["delhi", "mumbai", "chennai", "pune", "goa", "Jaipur"]

def element(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    element(list, idx+1)
    
element(list)