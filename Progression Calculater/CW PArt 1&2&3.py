#I declare that my work contaims no examples of misconduct,such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID:20221158
#Student name:Rathusaigini Thavarajah
#Date:25/11/2022

progress=0                                                     #opening a 0 variable to modify within  the loop and calculate the total progress out comes
trailer=0                                                         #opening a 0 variable to modify within  the loop and calculate the total moudule-trailer out comes
exclude=0                                                       #opening a 0 variable to modify within  the loop and calculate the total excluded out comes
retriever=0                                                     #opening a 0 variable to modify within  the loop and calculate the total moudule-trailer out comes
total=0                                                            #opening a 0 variable to modify within the loop and calculate the total count
count="y"
pass_cre=[]                                                  #opening empty list and appending it within the loop and getting the all pass credit inputs
defer_cre=[]                                                  #opening empty list and appending it within the loop and getting the all defer credit inputs
fail_cre=[]                                                      #opening empty list and appending it within the loop and getting the all failcredit inputs
progress_outcome=[]                                   #opening empty list and appending it within the loop and getting the all progress outcome inputs
UoW_num=[]                                                #opening empty list and appending it within the loop and getting the all UoW numbers inputs
def Range(x):
    if (x not in (0,20,40,60,80,100,120)):
             print("Out of range")


while True:
    count="y"
    print("choice 1- student can predict the progression")
    print("choice 2- staff can predict the progression")
    print("choice 3-end the program please enter ")
    choice=input("Enter your choice num:")
    if choice!="1" and choice!="2 "and choice!="3":
        print("Invalid selection")
    elif choice=="1":
        while True:
            try:
                 UoW_number=input("Enter the student's UoW number: ")  #prompt input from user
                 UoW_num.append(UoW_number)   #appending the UoW_num
                
                 pass_credit=int(input("Enter your total  PASS credits: "))     #prompt input form user 
                 pass_cre.append(pass_credit)  #appending the pass_credit

                 defer_credit=int(input("Enter your total DEFER credits: "))   #prompt input from user
                 defer_cre.append(defer_credit)    #appending the defer_cre

                 fail_credit=int(input("Enter your total FAIL credits: "))  #prompt input from user
                 fail_cre.append(fail_credit)                                                   #appending the fail_cre
                 if pass_credit+defer_credit+fail_credit==120:
                     if pass_credit==120:
                          print("Progress")
                          progress+=1    #modifying the progress outcome count inside progress coundition
                          progress_outcome.append('progress')#appending the progress_outcome

                     elif pass_credit==100 and (defer_credit in (20,0)) and (fail_credit  in(0,20)):
                          print("Progrss(module trailer)") 
                          trailer+=1#modifying the  do not progress (module trailer ) count inside the condition
                          progress_outcome.append('progress (module trailer)') #appending the progress_outcome
                
                     elif (pass_credit in (40,20,0)) and (defer_credit in (0,20,40)) and (fail_credit in(80,100,120)):
                           print("Exclude")
                           exclude+=1   #modifying the  Exclude count inside the condition
                           progress_outcome.append('Exclude') #appending the progress_outcome
   
                     elif(pass_credit in (0,20,40,60,80))and (defer_credit in (120,80,60,40,0,20)) and (fail_credit in (0,20,40,60,20)):#condition to get progress as a  outcome 
                            print("Do not progress – module retriever ")
                            retriever+=1 #modifying the do not progress-module retriever count inside the condition
                            progress_outcome.append("Do not progress – module retriever ") #appending the progress_outcome
                 
                     else:
                         print("Total incorrect")  #checking whether total is! =120 or not #if total is less than or greater than 120 print "Total Incorrecect"
                         total+=1 #modifying the total count inside the condition
            except ValueError:
                 print("Integer required")
            data=str(input("\n would you like to enter another set of data ?\n Enter 'y' for yes or 'q' to quit ans view results:"))
            def  histogram(outcome,count):
                    print(f"{outcome} {count} :",count*"*")  #by useing for loop we can count the stars and print it 
        
        
            if data=='q':
                 print("-----"*10)
                 print("Histogram\n")
                 histogram("progress", progress)
                 histogram("trailer", trailer)
                 histogram("retriever",retriever)
                 histogram("exclude", exclude)
        
                 print(progress+trailer+retriever+exclude,"outcomes in total")
                 print("-----"*10)
                 break
            elif data=='y':
                 continue
            else:
                 break

    print("Part 2:")

    for i in range(len(progress_outcome)):#using for loop and repeating for the number of count we get progress outcome
          print(progress_outcome[i],'-',pass_cre[i],',',defer_cre[i],',',fail_cre[i])#accessing the elements of the lists orderly

    print(" Part 3: ")

    f=open('progression_outcome.txt','w')   #stands foe write mode   #Reference Lectures notes in BB
    f=open('progression_outcome.txt','a')    #stands for append mode  #reference Lectures notes in BB
    for i in range(len(progress_outcome)):
          t="{} - {} , {} , {} ".format(progress_outcome[i],pass_cre[i], defer_cre[i], fail_cre[i])
          f.write(t)
    f.close() # closing the function(must)
    f=open('progression_outcome.txt','r')  #stands for read mode   #reference Letctures notes in BB
    for i in range(len(progress_outcome)):
          t="{} - {} , {} , {} ".format(progress_outcome[i],pass_cre[i], defer_cre[i], fail_cre[i])
          print(t)
          f.close()
