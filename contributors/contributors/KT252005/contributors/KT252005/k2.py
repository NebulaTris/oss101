while True:
  try:
     user_input = input("Write your message: ")
    # Process the user input here

     words=text.split()
     sentences=[]
     # import pandas as pd 
     # r=pd.Series(words)
     # print(r)
     for codes in words: 
         p=list(codes)
         coding=True
         if (coding):
           if len(p)>=1:
             import random 
             import string
             random_string = ''.join(random.choices(string.ascii_letters, k=3))
             random_string2 = ''.join(random.choices(string.ascii_letters,k=3))
             r1=list(random_string )
             r2=list(random_string2)
             in_string=''.join(p) # '' uses as a separator 
             # print(in_string)
             a=r1+p[1:]+[p[0]]+r2
             code=''.join(a)
             #print(code)
             sentences.append(code)
             store_var=r1
             store_var2=r2
             pass 
     
    
     print('\n')
     decoded_words=[]
     for sentence in sentences:
    
       coded_message=list(sentence)
       decoded_list =[coded_message[-4]]+coded_message[3:-4]
       decoded_string=''.join(decoded_list)
       decoded_words.append(decoded_string)
       # print(decoded_string)
   
     m=' '.join(decoded_words) + '  '
     print(f"your message is :- \n {m}")
  except EOFError:
       print("No input was provided.")