import csv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

GlobalFileName:str
GlobalFileName=''
def ConvertToPaypal(fname:str):
   try: 
    fr=open(fname,'r+',encoding='UTF+8')
    fw=open('OUTPUT_PAYPAL.csv','w',encoding='UTF+8')
    icntr=1

    while True:
        line = fr.readline()
        if not line:
            break
        print ('Processing line# '+ str(icntr))
        if icntr==5001:
            print('Maximum limit is achived of recipients per payment file.\r\n')
            break
        if len(line)>0 and icntr>1: 
            paymentline=line.split(',')
            #mbrown@myco.com,"100,50",EUR,ID001,Here is your payment, PAYPAL.
            amount =paymentline[1].replace('.',',')
            outline=paymentline[0].replace('"','') + ',\"'+amount+"\",EUR,ID"+ str(icntr)+ ',Owed '+ paymentline[2] + ',PAYPAL.\r'
            fw.write(outline)
            fw.flush()
        icntr+=1 
    
    print('Closing Files.')
    fw.close()
    fr.close()
   except Exception as ex:
      print('Exception' + str(ex))

def FileLoader():
   global GlobalFileName
   Tk().withdraw() # we dont want full view
   filename= askopenfilename(filetypes=[('Csv Files','.csv' )] ,title="Select Csv file into Paypal format")
   GlobalFileName=filename

def main():
   global GlobalFileName
   
   FileLoader()
   ConvertToPaypal(GlobalFileName)

if __name__=='__main__':
   main()

