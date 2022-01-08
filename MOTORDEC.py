
import CDATAPROCESSING
import csv,time



dete=CDATAPROCESSING.tempdi
b={}
row=0

def put(a):
    with open("MOTOR.csv",mode='w',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([a]) 
        csvfile.close()
        print("done")

motorstate=0


while(1):

    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        row=len(data)-1
        a=data[row][0]
        csvfile.close()
        print("done")


        temp=int(data[row][0])
        hum=int(data[row][1])
        moist=int(data[row][2])
        crx=int(data[row][3])
        cry=int(data[row][4])
        qindex=int(data[row][5])

        print(temp)
        print(hum)
        print(dete)
        b=dete[temp]
        m=b[hum]
    

        if(moist<m):
            print("on")
            motorstate=1
            put(1)
            time.sleep(1)
        else:
            print("off")
            motorstate=0
            put(0)
            time.sleep(1)
