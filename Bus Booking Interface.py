import datetime
class BusBooking:
    def __init__(self):
        self.waiting_list=[]
        self.window_seats=[]
        self.aisle_seats=[]
        for i in range(1,21):
            w="W"+str(i)
            a="A"+str(i)
            self.window_seats.append(w)
            self.aisle_seats.append(a)
        self.k=1
        self.passenger_list={}
        self.Waiting_list={}
        
    def book(self,name:str,preference='n'): #here(default) "n" shows no preference.
        booking_id=str(datetime.datetime.now())+name+preference[0]
        if preference in ["Window","window","W","w"]:
            if len(self.window_seats)>0:
                outcome=self.window_seats[0]
                self.window_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            elif len(self.aisle_seats)>0:
                outcome=self.aisle_seats[0]
                self.aisle_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            else:
                outcome="WL"+str(self.k)
                self.k+=1
                self.waiting_list.append(booking_id)
                self.Waiting_list[booking_id]=(name,outcome)
        elif preference in ["Aisle","aisle","A","a"]:
            if len(self.aisle_seats)>0:
                outcome=self.aisle_seats[0]
                self.aisle_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            elif len(self.window_seats)>0:
                outcome=self.window_seats[0]
                self.window_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            else:
                outcome="WL"+str(self.k)
                self.k+=1
                self.waiting_list.append(booking_id)
                self.Waiting_list[booking_id]=(name,outcome)
        else:
            if len(self.window_seats)>0:
                outcome=self.window_seats[0]
                self.window_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            elif len(self.aisle_seats)>0:
                outcome=self.aisle_seats[0]
                self.aisle_seats.remove(outcome)
                self.passenger_list[booking_id]=(name,outcome)
            else:
                outcome="WL"+str(self.k)
                self.k+=1
                self.waiting_list.append(booking_id)
                self.Waiting_list[booking_id]=(name,outcome)
        return(booking_id,outcome)
    
    def cancel(self,booking_id):
        if booking_id in self.passenger_list and len(self.waiting_list)>0:#####
            self.passenger_list[self.waiting_list[0]]=(self.Waiting_list[booking_id][0],self.passenger_list[booking_id])
            del self.passenger_list[booking_id]
            del self.Waiting_list[self.waiting_list[0]]
            self.waiting_list=self.waiting_list[1:]
            return True
        elif booking_id in self.passenger_list and len(self.waiting_list)==0:
            if self.passenger_list[booking_id][1][0]=='W':
                self.window_seats.append(self.passenger_list[booking_id][1])
                del self.passenger_list[booking_id]
            if self.passenger_list[booking_id][1][0]=='A':
                self.aisle_seats.append(self.passenger_list[booking_id][1])
                del self.passenger_list[booking_id]
                return True
        elif booking_id in self.waiting_list:
            self.waiting_list=self.waiting_list.remove(booking_id)
            del self.Waiting_list[booking_id]
            return True
        return False
    
    def status(self,booking_id):
        if booking_id in self.passenger_list:
            return self.passenger_list[booking_id]
        elif booking_id in self.Waiting_list:
            return (self.Waiting_list[booking_id][1],"WL"+str(self.waiting_list.index(booking_id)))
        else:
            return False
    def __str__(self):
        l=[]
        for x in self.passenger_list:
            l.append((x,self.status(x)[0],self.status(x)[1]))
        for y in self.Waiting_list:
            l.append((y,self.status(y)[0],self.status(y)[1]))
        for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j][0]>l[j+1][0]:
                    l[j],l[j+1]=l[j+1],l[j]
        return str(l)
        