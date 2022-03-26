#BLL
import pickle
class Customer:
    cust_list=[]     #call customer.custlist(class_name.Gvar_name)
    def __init__(self):        #constactor
        self.id=0     
        self.Name=0
        self.Age=0
        self.Mob=0
        self.Address=0
        self.Email=0
        self.Gender=0

    def add_customer(self):      #addcustomer
        Customer.cust_list.append(self)

    def search_customer(self):       #searchcustomer
        for i in Customer.cust_list:
            if (i.id==self.id):
                    self.Name=i.Name
                    self.Age=i.Age
                    self.Mob=i.Mob
                    self.Address=i.Address
                    self.Email=i.Email
                    self.Gender=i.Gender    

            elif self.Name==cust.Name:
                return i
            
            else:
                print("Invalid search")

    @staticmethod
    def delete_customer(id):        #deletcustomer
        for i in Customer.cust_list:
            if i.id==id:
                Customer.cust_list.remove(i)
                return

    def modify_customer(self):       #modifycustomer
        for i in Customer.cust_list:
            if self.id==cust.id:
                self.id=cust.id     
                self.Name=cust.Name
                self.Age=cust.Age
                self.Mob=cust.Mob
                self.Address=cust.Address
                self.Email=cust.Email
                self.Gender=cust.Gender
                return

    def show_customer(self,cust):         #showdata
        print("customer id:",cust.id,"\t""customer Name:",cust.Name,"\t""customer Age:",cust.Age)
        print("customer Mob:",cust.Mob,"\t""customer Address:",cust.Address)
        print("customer Email:",cust.Email,"\t""customer Gender:",cust.Gender)
#PLL

while(1):
    print()
    print("\n\n")
    print("\t\t\t\t***** Welcome to Customer management system *****\n")
    print("\t\t\t\tPress 1 add customer, Press 2 search customer:")
    print("\t\t\t\tPress 3 Delet customer, Press 4 Modify customer:")
    print("\t\t\t\tPress 5 show customer , Press 6 exit:")
    print("\t\t\t\tpress 7 dump in pickle exit , press 8 Load for pickle:")

    choice=input("Enter the choice digit:=")
    if choice=="1":
        cust=Customer()
        cust.id=input("Enter the customer id:=")
        cust.Name=input("Enter the customer Name:=")
        cust.Age=input("Enter the customer Age:=")
        cust.Mob=input("Enter the customer Mob:=")
        cust.Email=input("Enter the customer Email:=")
        cust.Address=input("Enter the customer Address:=")
        cust.Gender=input("Enter the customer Gender:=")
        cust.add_customer()
        print("customer add successfuly:")
        print()

    elif choice=="2":
        cust=Customer()
        cust.id=input("Enter The Customer Id:")
        cust.search_customer()
        cust.show_customer()

    elif choice=="3":
        id=input("Enter the customer id which you want to delete:")
        Customer.delete_customer(id)
        print("Customer Delete successfully!")
        print()

    elif choice=="4":
        cust=Customer()
        cust.id=input("Enter the customer id:=")
        cust.Name=input("Enter the customer Name:=")
        cust.Age=input("Enter the customer Age:=")
        cust.Mob=input("Enter the customer Mob:=")
        cust.Email=input("Enter the customer Email:=")
        cust.Address=input("Enter the customer Address:=")
        cust.Gender=input("Enter the customer Gender:=")
        cust.modify_customer()
        print("customer modify successfuly:")
        print()
    
    elif choice=="5":
        for i in Customer.cust_list:
            cust.show_customer(i)
        print()
        
    elif choice=="6":
        print("\t\t\t\tThanks for using software")
        break         
    
    elif choice=="7":
        pass

    elif choice=="8":
        pass






# ob=customer()
# # print(ob)
# ob.showdata()
# print(ob.id,ob.Name,ob.Age,ob.Mob,ob.Adress,ob.Email,ob.Gender)
# ob.id=10
# ob.Name="Divakar"
# ob.Age=23
# ob.Mob=9027716398
# ob.Email="divakarjadkdjfd25665@"
# ob.Gender="Mail"
# ob.Adress="khurja bulandshar pin-203141"
# ob1=customer()
# # ob1.showdata()
# ob1.id=20
# ob1.Name="Nishu"
# ob1.Age=22
# ob1.Mob=9027716398
# ob1.Email="neeshujadkdjfd25665@"
# ob1.Gender="Mail"
# ob1.Adress="Noida pin-203141"
# print(ob.id,ob.Name,ob.Age,ob.Mob,ob.Adress,ob.Email,ob.Gender)
# print(ob1.id,ob1.Name,ob1.Age,ob1.Mob,ob.Adress,ob.Email,ob.Gender)