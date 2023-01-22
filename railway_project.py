import random
import pickle
import sys

logged_in=False
uid = 0
pwd = ""


class train:
    def __init__(self,name = '', num = 0, arr_time = '',dep_time = '',src = '' ,des = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0,fare_1ac = 0, fare_2ac = 0 ,fare_sl = 0):
        self.name=name
        self.num=num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.src = src
        self.des = des
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}
        self.fare = {'1AC' : fare_1ac,'2AC' : fare_2ac ,'SL' : fare_sl}
    def print_seat_availablity(self):
        print("No. of seats available in 1AC :- "+str(self.seats['1AC']))
        print("No. of seats available in 2AC :- "+str(self.seats['2AC']))
        print("No. of seats available in SL :- "+str(self.seats['SL']))  
    def check_availabilty(self,coach='',ticket_num = 0):
    	coach = coach.upper()
    	if coach not in ('SL','1AC','2AC'):
    		print_seat_availablity()
    		coach = input("Enter the coach(1AC/2AC/SL) :-")
    	else:
    		if self.seats[coach] == 0:
    			return False
    		elif self.seats[coach] >= ticket_num :
    			return True
    		else:
    			return False
    def book_ticket(self,coach = '',no_of_tickets = 0):
    	self.seats[coach] -= no_of_tickets
    	    return True


class ticket:
	def __init__(self,train,user,ticket_num,coach):
		self.pnr = str(train.num)+str(user.uid)+str(random.randint(100,999))
		self.train_num = train.num
		self.coach = coach
		self.uid = user.uid
		self.train_name = train.name
		self.user_name = user.name
		self.ticket_num = ticket_num
		user.history.update({self.pnr : self})
	    ticket_dict.update({self.pnr : self})


class user:
	def __init__(self,uid = 0,name = '',hometown = '',cell_num = '',pwd = ''):
		self.uid = uid
		self.name = name
		self.hometown = ''
		self.cell_num = ''
		self.pwd = pwd
		self.history = {}


class acceptors:
	''' Class containing functions for accepting and 
	validating values properly'''
	def accept_uid():
		uid = 0
		try:
			uid = int(input("Enter the User ID:- "))
		except ValueError:
			print("Please enter user ID properly.")
			return acceptors.accept_uid()
		else:
			return uid

	def accept_pwd():
		pwd = input("Enter your password:- ")
		return pwd

    
    def accept_train_number():
		train_num = 0
		try:
			train_num = int(input("Enter the train number :- "))
		except ValueError:
			print("Please enter train number properly.")
			return acceptors.accept_train_number()
		else:
			if train_num not in trains:
				print("Please enter a valid train number.")
				return acceptors.accept_train_number()
			else:
				return train_num
	
 
    def accept_menu_option():
		option = input("Enter your option :- ")
		if option not in ('1','2','3','4','5','6','7','8'):
			print("Please enter a valid option!")
			return acceptors.accept_menu_option()
		else:
			return int(option)

	def accept_coach():
		coach = input("Enter the coach :- ")
		coach = coach.upper()
		if coach not in ('SL','1AC','2AC'):
			print("Please enter coach properly.")
			return acceptors.accept_coach()
		else:
			return coach


    def accept_prompt():
		prompt = input("Confirm? (y/n) :-")
		if prompt not in ('y','n'):
			print("Please enter proper choice.")
			return acceptors.accept_prompt()
		return prompt		

        

























































































































































































































































