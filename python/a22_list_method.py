class Mylist:
    def __init__(self):
        self.myVariable = "Kwon"
        self.myVariable2 = "su"
        self.myList=list()

    def append(self, ele):
        self.myList.append(ele)




def main():
    list_a = [1,2,3]
    list_b = [4,5,6]
    
    print(list_a+list_b)
    print(list_a)
    list_a.extend(list_b)
    print(list_a)

    list_b.append(7)
    list_b.append(8)
    print(list_b)
    list_b.insert(1, 4.5)
    print(list_b)
    myList_a=MyList()
    myList_a.append(1)
    print(myList_a,myVariable, myVariable2)

if __name__ == "__main__":
    main()
    