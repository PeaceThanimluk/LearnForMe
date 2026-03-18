#ต้องอยู่ในfolderเดียวกันถึงจะimportได้
from Account import Accounting #from ชื่อไฟล์ import ชื่อMethod
from programmer import Programmer
from sale import Sale 
#crate object
Account = Accounting("FreeFire" , 20000 , 30)
programmer = Programmer("King" , 60000 , 2 , "Coding")
Sale = Sale("Baka" , 20000 , "Bangkok")


#Show data
# Account.ShowData()

print(f"MOney: {Account._getIncome(100)}")