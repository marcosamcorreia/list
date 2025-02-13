import os
def AddList():
    list=[]
    numberList=1
    item=''
    nlist=[]

    print("Write the item do add it to the list: ")
    print("When complete, write done \n")

    while item !="done":
        text=input("Add your item: ")
        item=text.lower()
        if item!="done":
            list.append(text)
    print("Done \n")
    
    print("""=============== Here is your List ===============\n""")


    for i in list:
        print(f"           {numberList}    ---------------->    {i}")
        numberList+=1
    print("""\n================ End of the List ================\n""")
    os.system("pause")
if __name__ == "__main__":
    AddList()
