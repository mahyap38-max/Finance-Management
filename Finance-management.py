import sqlite3
connection=sqlite3.connect("management.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS
management(
id INTEGER PRIMARY KEY,
title TEXT,
amount TEXT,
type TEXT,
date TEXT,
description TEXT)""")

connection.commit()
if connection:
    connection.close()

class transaction:

    def __init__ (self,title,amount,type,date,description):
       
        self.title=title
        self.amount=amount
        self.type=type
        self.date=date
        self.description=description
    
    def totuple(self):
        return(
             self.title,
             self.amount,
             self.type,
             self.date,
             self.description
        )


class database:

    def add_trans():
        while True:
            title=(input("Enter the title: ").strip()).lower()
            if (len(title)==0):
                                    print("Please enter a title.")
                                    continue
            break

        while True:
            try:
                     amount=(input("Enter the amount:").strip())
                     if(len(amount)==0 or not amount.isdigit() or int (amount)<=0):
                           print("Invalid input \nPlease try again.")
                           continue
                     else:
                         break
            except Exception as e:
                 print("Error:",e)
                 continue
              
        print("Choose transaction type. \n1.Expense \n2.Income")
        
        while True:
            try:
                 choice=(int(input("Enter: ")))
            except ValueError :
                 print("Please choose a number among the list above.")
                 continue
            try:
                    if choice==1:
                        type="Expense"
                        break
                    elif choice==2:
                        type="Income"
                        break
                    else:
                        print("Invalid input \nPlease try again.")
                        continue
            except Exception as e:
                 print("Error",e)
                 continue

                
        print("Enter date.")
        while True:
                try:
                        day=(input("Day: ").strip()).lower()
                
                        if(not day.isdigit() or int(day)>31 or int(day)<=0):
                            print("invalid input \n Please try again")
                            continue
                        else:
                            break
                except Exception as e:
                     print("Error:",e)
                     continue

        while True:
                try:
                        month=(input("Month: ").strip()).lower()

                        if(not month.isdigit() or int(month)>12 or int(month)<=0):
                            print("Invalid input \nPlease try again")
                            continue
                        else:
                            break
                except Exception as e:
                     print("Error",e)
                     continue
        while True:
            try:
                    year=(input("Year: ").strip()).lower()

                    if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                        print("Invalid input \nPlease try again")
                        continue
                    else:
                        break
            except Exception as e:
                 print("Error",e)
                 continue

        try:
                newdate=year+'-'+month+'-'+day
        
                description=(input("*optional* \nEnter description: "))
        except Exception as e:
                    print("Error:",e)
                  
        try:
                newtrans=transaction(title,amount,type,newdate,description)

                connection=sqlite3.connect("management.db")
                cursor=connection.cursor()
                cursor.execute("""
                INSERT INTO management( title,amount,type,date,description)
                VALUES (?,?,?,?,?)""",(newtrans.totuple()))
        
                connection.commit()
                
        except Exception as e:
             print("Error",e)
            

        finally:
            if connection:
                                connection.close()
        return "Done"


    def delete_trans():

            
            while True:

                    title=(input("Enter title: ").strip()).lower()
                    if (len(title)==0):
                           print("Please enter a title.")
                           continue

                  
                    try:
                        connection=sqlite3.connect("management.db")
                        cursor=connection.cursor()
                        
                        cursor.execute("SELECT * FROM management WHERE title LIKE ? ",(f"%{title}%",))
                        rows=cursor.fetchall()

                        if not rows :
                              print("No data found for this title.\nPlease try again")
                              continue
                        
                    except Exception as e:
                        print("Error:",e)
                        continue

                
                    try:
                        validids=[]
                        for row in rows:
                                validids.append(row[0])
                                print(row)

                            
                    except Exception as e:
                        print("Error:",e)
                        continue

                    break
                
                    
                  

            print("Enter the ID to delete:")
            while True:
                    try:
                        id=int(input("ID: "))
                    except ValueError:
                        print("Please enter an integer number.")
                        continue

                    if id not in validids:
                          print("Please choose one of the displayed IDs.")
                          continue

                    try:
                        connection=sqlite3.connect("management.db")
                        cursor=connection.cursor()
                        cursor.execute("""
                        DELETE FROM management 
                        WHERE id=? """,(id,))
                        connection.commit()
                    except Exception as e:
                        print("Error:",e)
                        continue
                    if connection:
                        connection.close()
                    break
            return "Done"                       


    def update_trans():

            while True:
    
                        title=(input("Enter title: ").strip()).lower()
                        if(len(title)==0):
                                               print("Please enter a title.")
                                               continue
                    
                        try:
                            connection=sqlite3.connect("management.db")
                            cursor=connection.cursor()
                            cursor.execute("SELECT * FROM management WHERE title LIKE ? ",(f"%{title}%",))
                            rows=cursor.fetchall()

                            
                            if not rows :
                                print("No data found for this title.\nPlease try again")
                                continue
                            
                        except Exception as e:
                            print("Error:",e)
                            continue
    
                    
                        try:
                            validids=[]
                            for row in rows:
                                    validids.append(row[0])
                                    print(row)
    
                        except Exception as e:
                            print("Error:",e)
                            continue
                        break

            print("Enter the ID to update:")
            while True:
                                try:
                                   id=int(input("ID: "))
                                except ValueError:
                                   print("Please enter an integer number.")
                                   continue
           
                                if id not in validids:
                                     print("Please choose one of the displayed IDs.")
                                     continue
                                break

            while True:
                                try:
                                        amount=(input("Enter the amount:").strip())
                                        if(len(amount)==0 or not amount.isdigit() or int (amount)<=0):
                                            print("Invalid input \nPlease try again.")
                                            continue
                                        else:
                                            break
                                except Exception as e:
                                    print("Error:",e)
                                    continue
                                
                                
            print("Choose transaction type. \n1.Expense \n2.Income")
                
            while True:
                    try:
                        choice=(int(input("Enter: ")))
                    except ValueError :
                        print("Please choose a number among the list above.")
                        continue
                    try:
                            if choice==1:
                                type="Expense"
                                break
                            elif choice==2:
                                type="Income"
                                break
                            else:
                                print("Invalid input \nPlease try again.")
                                continue
                    except Exception as e:
                        print("Error",e)
                        continue

                        
            print("Enter date.")
            while True:
                        try:
                                day=(input("Day: ").strip()).lower()
                        
                                if(not day.isdigit() or int(day)>31 or int(day)<=0):
                                    print("invalid input \n Please try again")
                                    continue
                                else:
                                    break
                        except Exception as e:
                            print("Error:",e)
                            continue

            while True:
                        try:
                                month=(input("Month: ").strip()).lower()

                                if(not month.isdigit() or int(month)>12 or int(month)<=0):
                                    print("Invalid input \nPlease try again")
                                    continue
                                else:
                                    break
                        except Exception as e:
                            print("Error",e)
                            continue
            while True:
                    try:
                            year=(input("Year: ").strip()).lower()
                            if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                                print("Invalid input \nPlease try again")
                                continue
                            else:
                                break
                    except Exception as e:
                        print("Error",e)
                        continue
            while True:
                try:
                            date=year+'-'+month+'-'+day

                            description=(input("*optional* \nEnter description: "))
                except Exception as e:
                                print("Error:",e)
                                continue
                break


            try:
                  connection=sqlite3.connect("management.db")
                  cursor=connection.cursor()
                  cursor.execute("""
                  UPDATE management
                  SET amount=? , type=? , date=? , description=?
                  WHERE id=?  """,
                  (amount,type,date,description,id))
                  connection.commit()

                  if connection:
                        connection.close()
            except Exception as e:
                  print("Error:",e)

            return "Done"


    def search_by_title():

        while True:
            try:
                title=(input("Enter title:").strip()).lower()
                if(len(title)==0):
                       print("Please enter a title.")
                       continue
                connection=sqlite3.connect("management.db")
                cursor=connection.cursor()
                cursor.execute("SELECT * FROM management WHERE title LIKE ?",(f"%{title}%",))
                rows=cursor.fetchall()

                if not rows :
                                    print("No data found for this title.\nPlease try again")
                                    continue
                
                                        
            except Exception as e:
                                        print("Error:",e)
                                        continue
                
                                
           
                                       
            for row in rows:  
                                    print(row)
                
                                            
            
            if connection:
                   connection.close()
            break
        return "Done"


    def search_by_date():

        print("Enter date.")

        while True:
                           try:
                                   day=(input("Day: ").strip()).lower()
                           
                                   if(not day.isdigit() or int(day)>31 or int(day)<=0):
                                       print("invalid input \n Please try again")
                                       continue
                                   else:
                                       break
                           except Exception as e:
                                print("Error:",e)
                                continue
           
        while True:
                           try:
                                   month=(input("Month: ").strip()).lower()
           
                                   if(not month.isdigit() or int(month)>12 or int(month)<=0):
                                       print("Invalid input \nPlease try again")
                                       continue
                                   else:
                                       break
                           except Exception as e:
                                print("Error",e)
                                continue
        while True:
                        try:
                               year=(input("Year: ").strip()).lower()
           
                               if(not year.isdigit() or len(year)!=4 or int(year)<=0):
                                   print("Invalid input \nPlease try again")
                                   continue
                               else:
                                   break
                        except Exception as e:
                            print("Error",e)
                            continue
       
        date=year+'-'+month+'-'+day
                   
                                
        while True:
                try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE date=?",(date,))
                    rows=cursor.fetchall()
                    connection.commit()

                    if not rows:
                            print("No data found for this date.")
                            break
                except Exception as e:
                       print("Error:",e)

                for row in rows:
                       print(row)
                if connection:
                       connection.close()

                break
        return "Done"


class statistics:

    def total_income():

        try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Income",))
                    rows=cursor.fetchall()
                    connection.commit()
                    amount=0
                    for row in rows:
                            amount+=float(row[2])
                    print(f"Total income is :{amount}")
        except Exception as e:
               print("Error:",e)
        if connection:
               connection.close()
        return "Done"

    def total_expense():

            try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Expense",))
                    rows=cursor.fetchall()
                    amount=0
                    connection.commit()
                    for row in rows:
                            amount+=float(row[2])
                    print(f"Total income is :{amount}")
            except Exception as e:
                          print("Error:",e)
            if connection:
                   connection.close()

            return "Done"
                       
    def current_balance():
            try:
                    connection=sqlite3.connect("management.db")
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Income",))
                    rows=cursor.fetchall()
                    income=0
                    for row in rows:
                            income+=float(row[2])
                   
            except Exception as e:
                          print("Error:",e)
            try:
                    cursor.execute("SELECT * FROM management WHERE type=? ", ("Expense",))
                    rows=cursor.fetchall()
                    expense=0
                    connection.commit()
                    for row in rows:
                            expense+=float(row[2])
                   
            except Exception as e:
                                      print("Error:",e)

            if connection:
                   connection.close()

            balance=income-expense

            print(f"current balance is: {balance}")
            return "Done"


while True:
        print("---------Finance Manager---------")
        print("Choose 1 to access transaction.")
        print("Choose 2 to access statistics.")
        print("Choose 0 to exit.")

        while True:
            try:
                choice=int(input("Enter your choice: "))
                if (not 0<=choice<=2):  
                    print("Please choose from the list above.")
                    continue
                        
            
            except ValueError:
                print("Please choose a number from the list above.")    
                continue
            break     
             
            

        match choice :
               case 1:

                    while True:
                            print("---Transaction Management---")
                            print("[1] Add transaction")
                            print('[2] Delete transaction')
                            print('[3] Update transaction')
                            print('[4] Search by title')
                            print('[5] Search by date')
                            print('[0] Return to main menu')

                            while True:
                                    try:
                                        choice2=int(input("Enter your choice: "))
                                        if (not 0<=choice2<=5):
                                               
                                          print("Please choose a number from the list above.")
                                          continue
                                                
                                    except ValueError :
                                           print("Please choose from the list above.")
                                           continue
                                    break

                                           
                            match choice2:

                                   case 0:
                                          print("Returning to main menu")
                                          break
                               
                                   case 1:
                                            try:
                                                    print(database.add_trans())
                                            except Exception as e:
                                                   print(e)
                                
                                                
                                   case 2:
                                          print(database.delete_trans())
                                         
                                   case 3:
                                          print(database.update_trans())
                                         
                                   case 4:
                                          print(database.search_by_title())
                                          
                                   case 5:
                                          print(database.search_by_date())
                                          


               case 2:
                      while True:
                             print("---Statistics---")
                             print("[1] Total income")
                             print("[2] Total expense")
                             print("[3] Current balance")
                             print("[0] Return to main menu")
                             while True:
                                        try:
                                            choice3=int(input("Enter your choice: "))
                                            if (not 0<=choice3<=3):
                                                   
                                                print("Please choose a number from the list above.")
                                                continue
                                        except ValueError :
                                            print("Please choose from the list above.")
                                            continue
                                        break
                                       
                             match choice3:

                                    case 0:
                                           print("Returning to main menu")
                                           break
                                           
                                    case 1:
                                           print(statistics.total_income())
                                          
                                    case 2:
                                           print(statistics.total_expense())
                                         

                                    case 3:
                                           print(statistics.current_balance())
                                         

               case 0:
                      print("Exiting program...")
                      break
                                          
                                                    
                        



                                

                                
                                    
                






        
        