

print("STAFF VERSION")
print("Student ID : W1761247")
print("")

progress_total=0
trailing_total=0
retriever_total=0
exclude_total=0
credit_total=0
students=0

def rangeError():
   print("RANGE ERROR")
    
def dataTypeError():
   print("INPUT INTEGERS")
   

while True:
    credit_total=0
    students += 1
    while True: 
        try:
            passed_credits = int(input("Enter passed credits: "))
            if passed_credits not in range(0,121,20):
                rangeError()
                continue
            else:
                credit_total=credit_total+passed_credits
                break
        except:
            dataTypeError()
            continue

    while True:
        try:
            deferred_credits = int(input("Enter deferred credits: "))
            if deferred_credits not in range(0,121,20):
                rangeError()
                continue
            else:
                credit_total=credit_total+deferred_credits
                break
        except:
            dataTypeError()
            continue
 
    while True:
        try:
            failed_credits = int(input("Enter failed credits: "))
            if failed_credits not in range(0,121,20):
                rangeError()
                continue
            else:
                credit_total=credit_total+failed_credits
                break
        except:
            dataTypeError()
            continue

  
    if credit_total!=120: #check the sum of three inputs not equal to 120
        print("TOTAL INCORRECT")
        students -= 1
        continue
    
    elif passed_credits == 120: #deciding progression level and keeping the record of each student
        progress_total = progress_total + 1  
    elif passed_credits == 100:          
        trailing_total = trailing_total + 1  
    elif passed_credits <= 80 and failed_credits <= 60:            
        retriever_total = retriever_total + 1 
    elif failed_credits >= 80:            
        exclude_total = exclude_total + 1
    else:
        break

    while True: #if user wants to add more or proceed the histogram loop
        print('')
        print("Enter 'q' for the histogram of current records","\nEnter 'c' to add more records")
        qc = input()
        print('')
        if qc=="q":
             break
        elif qc=="c":
            break
        else:
            print("INPUT 'q' or 'c' ")
            continue
    
    if qc=="c":
        continue
    else:
        break





print(students,'outcomes in total.') #verticle histogram
print('')

print("    progress ", "Trailing ", "Retriever ", "Exclude" )
print(" "*7,progress_total ," "*7,trailing_total ," "*7,retriever_total ," "*7,exclude_total)

while students > 0:
    print('')
    
    if progress_total > 0:
        print("\t*" ,end=" ")
        progress_total -= 1
        students -= 1
    else:
        print("\t " ,end=" ")
        
    if trailing_total > 0:
        print("\t  *" ,end=" ")
        trailing_total -= 1
        students -= 1
    else:
        print("\t " ,end=" ")

    if retriever_total > 0:
        print("\t    *" ,end=" ")
        retriever_total -= 1
        students -= 1
    else:
        print("\t " ,end=" ")

    if exclude_total > 0:
        print("\t      *" ,end=" ")
        exclude_total -= 1
        students -= 1
    else:
        print("\t " ,end=" ")
    
 
