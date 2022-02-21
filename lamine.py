
import datetime
from multiprocessing import log_to_stderr
import time
import threading
from collections import deque




class Watchdog(threading.Thread):

	ro = -1
	cpt = -1

	def __init__(self, ro):

		self.ro = ro

		threading.Thread.__init__(self)


	def run(self):

		print(" : Starting watchdog")

		self.cpt = self.ro

		while (1):

			if(self.cpt >= 0):

				self.cpt -= 1
				time.sleep(1)

			else :
				print("!!! Watchdog stops tasks.")
				global watchdog
				watchdog = True
				self.cpt = self.ro


class first():


	name = None
	priority = -1
	ro = -1
	time_exec = -1
	last_deadline = -1
	last_time_exec = None
	preempted = False


	############################################################################
	def __init__(self, name, priority,preempted ,ro, time_exec ,last_execution):

		self.name = name
		self.priority = priority
		self.preempted = preempted
		self.ro = ro
		self.time_exec = time_exec
		self.last_time_exec = last_execution


	############################################################################
	def run(self):

		# Update last_time_exec
		self.last_time_exec = datetime.datetime.now()

	
		global tank
		
		execTime = self.time_exec
		print(self.name + " : Starting task (" + self.last_time_exec.strftime
            ("%H:%M:%S") + ") : execution time = " + str(execTime))
		
		while (tank <= 40  ):
			print( "producing 10 oil" )
			tank += 10

			execTime -= 1

			time.sleep(1)

			if (execTime <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
			
            
		

class seconde():


	name = None
	priority = -1
	ro = -1
	time_exec = -1
	last_deadline = -1
	last_time_exec = None
	preempted = False

	def __init__(self, name, priority,preempted ,ro, time_exec ,last_execution):

		self.name = name
		self.priority = priority
		self.preempted = preempted
		self.ro = ro
		self.time_exec = time_exec
		self.last_time_exec = last_execution


	def run(self):

		# Update last_time_exec
		self.last_time_exec = datetime.datetime.now()

		
		global tank
		
		
		execTime = self.time_exec

		print(self.name + " : Starting task (" + self.last_time_exec.strftime
            ("%H:%M:%S") + ") : execution time = " + str(execTime))

		while (tank <= 30 ):
			print( "producing 20 oil" )
			tank += 20

			execTime -= 1

			time.sleep(1)

			if (execTime <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
			

class machine1():


	name = None
	priority = -1
	ro = -1
	time_exec = -1
	last_deadline = -1
	last_time_exec = None
	preempted = False


	def __init__(self, name, priority,preempted ,ro, time_exec ,last_execution):

		self.name = name
		self.priority = priority
		self.preempted = preempted
		self.ro = ro
		self.time_exec = time_exec
		self.last_time_exec = last_execution


	def run(self):

		# Update last_time_exec
		self.last_time_exec = datetime.datetime.now()

		
		global tank 
		
		
		execTime = self.time_exec

		print(self.name + " : Starting task (" + self.last_time_exec.strftime
            ("%H:%M:%S") + ") : execution time = " + str(execTime))
		global stock1
		while (tank >= 25 and stock1 <= (stock2 /4)  ):
			
			print( "Consuming 25 oil" )
			tank-= 25
			print("producing 1 motor")
			stock1 += 1
			execTime -= 1
			time.sleep(1)
			if (execTime <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
			

		print(self.name + " : Pre-empting task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")

class machine2():


	name = None
	priority = -1
	ro = -1
	time_exec = -1
	last_deadline = -1
	last_time_exec = None
	preempted = False


	def __init__(self, name, priority,preempted ,ro, time_exec ,last_execution):

		self.name = name
		self.priority = priority
		self.preempted = preempted
		self.ro = ro
		self.time_exec = time_exec
		self.last_time_exec = last_execution



	def run(self):

		self.last_time_exec = datetime.datetime.now()

		
		global tank , stock2 
		
		execTime = self.time_exec

		print(self.name + " : Starting task (" + self.last_time_exec.strftime
            ("%H:%M:%S") + ") : execution time = " + str(execTime))
		global stock2
		while (tank >= 5 and stock1 > (stock2 /4)  ):
			
			print( "Consuming 5 oil" )
			tank-= 5
			print("producing 1 wheel")
			stock2 += 1
			execTime -= 1
			time.sleep(1)
			if (execTime <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
			


	
global tank, stock1, stock2
tank = 0
stock1 = 0
stock2 = 0

last_execution = datetime.datetime.now()

task_list = list()
task_list.append (first(name="first", priority = 1, ro = 5, preempted= False, time_exec = 2, last_execution = last_execution))
task_list.append (two(name="two", priority = 1, ro = 15,preempted= False ,time_exec = 3, last_execution = last_execution))
task_list.append (machine1(name="machine1", priority = 1, ro = 5,preempted= True ,time_exec = 5, last_execution = last_execution))
task_list.append (machine2(name="machine2", priority = 1, ro = 5,preempted= True ,time_exec = 5, last_execution = last_execution))



while(True):
	print("You now have " + str(stock1) + " motor " + str(stock2) + " wheels" )
	for task_to_run in task_list :
		task_to_run.run()









