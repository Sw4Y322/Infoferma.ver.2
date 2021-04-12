import random #оно не работает,залил уж так(((((((
y = 1
x1 = 0
x2 = 0
class player:
	def __init__(self , name = ""):
		self.name = name

	def hit():
		if random.random() < 0.8:
			return True
		else:
			return False
class game:
	def __init__(self,p1):
	
	def start_game(p1,p2):
		while (x1 < 11) or (x2 < 11):
			while p1.hit() == true:
				if p1.hit() == True:
					y = y + 1
				elif y % 2 == 1:
					x1 = x1 + 1
				else:
					x2 = x2 + 1
			y = 1



