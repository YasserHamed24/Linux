import os
from time import sleep

print("----  Make your choice  --- ")
print("clockwise     press : 1")
print("Anticlockwise press : 2")

x = input("Your choice is : ")
os.system('cls')
if x == "1":
  while True:
      print('''
                                      *
                                     ***
                                    *****
                                   *******
                                  *********
                                      *
                                      *
                                      *
                                      *
                                      *
                                      *
      ''')

      sleep(0.5)
      os.system('cls')
      print('''
                                      
                                  
                                  
                                  
                                  
                                      
                                                  *
                                                  * *
                                                  * * *  
                                                  * * * *
                                      * * * * * * * * * * * 
                                                  * * * *
                                                  * * *
                                                  * *
                                                  *
      ''')
      sleep(0.5)
      os.system('cls')
      print('''
                                      
                                  
                                  
                                  
                                  
                                      
                                              
                                              

                    
                                      *
                                      *
                                      * 
                                      *
                                      * 
                                  *********
                                   *******
                                    *****
                                     ***
                                      *    
                                              
      ''')
      sleep(0.5)
      os.system('cls')
      print('''
                                      
                                  
                                  
                                  
                                  
                                      
                          *                        
                        * *                                     
                      * * *                                              
                    * * * *                  
                  * * * * * * * * * * *
                    * * * *                                            
                      * * *                            
                        * *  
                          *                       
                                                  
      ''')
      sleep(0.5)
      os.system('cls')
elif x == "2":
  while True:
    print('''
                                          
                                      
                                      
                                      
                                      
                                          
                              *                        
                            * *                                     
                          * * *                                              
                        * * * *                  
                      * * * * * * * * * * *
                        * * * *                                            
                          * * *                            
                            * *  
                              *                       
                                                      
          ''')
    sleep(0.5)
    os.system('cls')
    
    print('''
                                    
                                
                                
                                
                                
                                    
                                            
                                            


                                          *
                                          *
                                          * 
                                          *
                                          * 
                                      *********
                                       *******
                                        *****
                                         ***
                                          *    
                                            
      ''')
    sleep(0.5)
    os.system('cls')

    print('''
                                          
                                      
                                      
                                      
                                      
                                          
                                                      *
                                                      * *
                                                      * * *  
                                                      * * * *
                                          * * * * * * * * * * * 
                                                      * * * *
                                                      * * *
                                                      * *
                                                      *
    ''')
    sleep(0.5)
    os.system('cls')
    print('''
                                          *
                                         ***
                                        *****
                                       *******
                                      *********
                                          *
                                          *
                                          *
                                          *
                                          *
                                          *
    ''')

    sleep(0.5)
    os.system('cls')
else:
   print("GET OUT!!")