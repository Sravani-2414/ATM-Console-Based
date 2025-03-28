accounts = {
         2614: ["sravani","14-01-2004","1416",30000],
         0001: ["gowthami","16-02-2004","1614",20000],
         6241: ["surthi","21-09-2025",None,10000]
     }
print("Welcome !")
while True:
     print("********************************")
     print("1. Withdraw")
     print("2. Deposit")
     print("3. Pin Generation")
     print("4. Mini Statement")
     print("5. Exit")
     x = int(input("Enter Your option: "))
     if x > 5:
         print("Choose the correct Option")
     else:
         if x == 1:
             accno = int(input("Enter Account Number: "))
             if accno not in accounts:
                 print("No user exists with Account number")
             else:
                 if accounts[accno][-2] is None:
                     print("Generate Pin before withdraw operation")
                 else:
                     pin = input("Enter Pin: ")
                     if accounts[accno][-2] != pin:
                         print("Invalid Pin, Try again")
                     else:
                         amt = int(input("Enter Amount to Withdraw: "))
                         if amt <= accounts[accno][-1]:
                             accounts[accno][-1] -= amt
                             print("Withdraw Success")
                         else:
                             print("Insufficient Fund/Balamace/Amount")
         elif x == 2:
             accno = int(input("Enter Account Number: "))
             if accno not in accounts:
                 print("No user exists with Account number")
             else:
                 amt = int(input("Enter Amount to be Deposited: "))
                 accounts[accno][-1] += amt
                 print("Deposit Success")
         elif x == 3:
             accno = int(input("Enter Account Number: "))
             if accno not in accounts:
                 print("No user exists with Account number")
             else:
                 if accounts[accno][-2] is not None:
                     print("Pin Already GEnerated")
                 else:
                     pin = input("Enter Pin: ")
                     cpin = input("Re enter Pin: ")
                     if pin != cpin:
                         print("Pin Does not Match")
                     else:
                         accounts[accno][-2] = pin
                         print("Pin Generated successfully !")
         elif x == 4:
             accno = int(input("Enter Account Number: "))
             if accno not in accounts:
                 print("No user exists with Account number")
             else:
                 if accounts[accno][-2] is None:
                     print("Generate Pin before Mini statment operation")
                 else:
                     pin = input("Enter Pin: ")
                     if accounts[accno][-2] != pin:
                         print("Invalid Pin, Try again")
                     else:
                         print(f"Account Number: {accno}")
                         print(f"Name: {accounts[accno][0]}")
                         print(f"Date of Birth: {accounts[accno][1]}")
                         print(f"Balance: {accounts[accno][-1]}")
         else:
             print("Thank You")
             break
     print("********************************")
