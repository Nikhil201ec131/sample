 # using this libraries to store customer data
import pathlib as pl
import pickle as pk
import os

class customer:
  account_no=0;
  name=''
  deposit_amt=0;

  def newaccount(self):
    self.account_no=int(input("enter an account number :"))
    self.name=input("enter new account holder name") 
    self.deposit_amt=int(input("enter amout you want to deposit (for new customers min deposit = 500rs)"))

  def editdetails(self):
    print("check your account n.o :",self.account_no)
    self.name=input("enter changed name :")
    self.deposit_amt=int(input("enter changed balance :"))
  
  def printaccount(self):
    print("account number :", self.account_no)
    print("name :",self.name)
    print("balance :",self.deposit_amt)

  def add_amt(self,amount):
    self.deposit_amt+=amount

  def withdraw_amt(self,amount):
    self.deposit_amt-=amount
  def enter():
    print("press enter to use BANKING SYSTEM")
    input()
def listAccount():
    account = customer()
    account.newaccount()
    writeAccountsFile(account)

def view_cus_data():
    file = pl.Path("customer_data")
    if file.exists():
      data=open('customer_data','rb')
      cuslist=pk.load(data)
      for man in cuslist:
        print(man.account_no,"  ",man.name,"  ",man.deposit_amt)
        data.close()
    else:
      print("no records")

def balance(accno):
    file = pl.Path("customer_data")
    if file.exists():
      data=open('customer_data','rb')
      cuslist=pk.load(data)
      data.close()
      x=0
      for man in cuslist:
        if(man==accno):
          print("your account balance :",man.deposit_amt)
          x=1
    elif x==0 :
      print("no account number please check the number")
    else:
      print("not found")

def depositorwithdraw(accno,option):
    file = pl.Path("customer_data")
    if file.exists():
      data=open('customer_data','rb')
      cuslist=pk.load(data)
      data.close()
      os.remove('customer_data')
      for man in cuslist:
        if man.account_no==accno:
          if option==1:
            amount=int(input("enter the amount you want to deposit : "))
            man.deposit_amt+=amount
            print("current balance",man.deposit_amt)
            print("transation completed")
          if option==2:
            amount=int(input("enter the amount you want to withdraw : "))
            if amount <=man.deposit_amt:
              man.deposit_amt-=amount
              print("current balance",man.deposit_amt)
              print("transation completed")
            else :
              print("insuffient balance")
    else:
      print("not found")

    newdata=open('new_cus','wb')
    pk.dump(cuslist,newdata)
    newdata.close()
    os.rename('new_cus','customer.data')

def writeAccountsFile(account) : 
    
    file = pl.Path("customer_data")
    if file.exists ():
        newdata = open('customer_data','rb')
        old = pk.load(newdata)
        old.append(account)
        newdata.close()
        os.remove('customer_data')
    else :
        old= [account]
    tfile = open('newaccounts_data','wb')
    pk.dump(old,tfile)
    tfile.close()
    os.rename('newaccounts_data', 'customer_data')

option=''
select=0
print("welcome to SBBI banking system")

while option!=6:
  print("select option number below")
  print("1.create account")
  print("2.depsit")
  print("3.withdraw")
  print("4.balance")
  print("5.customers data")
  print("6.exit")
  option=input("enter choice")

  if option=='1':
    listAccount()
  elif option=='2':
    acc=int(input("enter account number"))
    depositorwithdraw(acc,1)
  elif option=='3':
    acc=int(input("enter account number"))
    depositorwithdraw(acc,2)
  elif option=='4':
     acc=int(input("enter account number"))
     balance(acc)
  elif option=='5':
    view_cus_data()
  elif option=='6':
    print("\ncompleted")
    break
  else:
    print("please enter the input from above options")
    option=input("enter your choice")
    








          







  
