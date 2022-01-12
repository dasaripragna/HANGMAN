import random

print("welcome to uber")
print("halnayaknhalli ng sarjapura")
# import random

rider =[1,2,3,4]
destination=["sarjapu","banglore","nandihills","huskur"]
rider=["aksu","sohel","faisal","sabeer"]
def cab():
    rides=int(input(" enter how many killometers you want to ride ="))
    i=1
    total=0
    dict={}
    while i<=rides:
        dist = int (input("enter the kilometers= "))
        place=input("enter any place =")
        driver=random.choice(rider )
        print(driver, "is available")
        if driver in rider:
            print("im in your destination ")
            money=dist*5
            total+=money
            print ("ride money=",total)
        else:
            print("driver is not available")
        dict[driver]=total
        i=i+1
    print(dict)
    j=0
    for key in dict :
        if dict[key]>j:
            j=dict[key]
    print("ride is end up")

def can():
    print("your ride is canceled")
def main():
    options = int(input("press 1 to confirm ride  and press 2  for cancel ride   = "))
    if options == 1:
        cab()
        print("thanks to visit my cab service ","\U0001F200")
    else:
        can() 
main()





        
