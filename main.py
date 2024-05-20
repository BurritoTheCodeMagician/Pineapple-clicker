#####################
# pineapple clicker #
# beta v0.0.3			  #
# by burrito		    #	
#####################

# imports #
import os
from colorama import Fore
import time
import json
import random

version = "				    v0.0.2"
def changelog():
	clear()
	print("0.0.0 (prerelease) - made the game")
	print("0.0.0 (prerelease) - pineapple per second works, games technically functional")
	print("0.0.1 (prerelease) - fixed most loopholes. game is playable")
	print("0.0.2 (beta) - added store")
	print("0.0.3 (beta) - added save string")
	print(f"\npress {Fore.BLUE}[ENTER]{Fore.RESET} to go back")
	print("0.0.4 (beta) - added saving and loading (save code doesnt work yet)")
	print("0.0.5 (beta) - added golden pineapples")
	input("> ")
	
# variable setup #
class variable_class:
	def __init__(self):
		# values
		self.optionFirst = "New Game"
		self.goldenpineapple = True
		self.golden_pineapple_message = ""
		self.total_goldenpineapples = 0
		self.pineapples = 0.0
		self.most_pineapples = 0.0
		self.lastharvest = 0.0
		self.pps_multiplier = 1
		self.pps = 0.0
		self.click_message = "+1"
		self.harvest_message = ""
		self.store_message = ""
		self.name = "jimmy neutron"
		
		self.buildings = ["cursors","grandpas","farms","mines","factories","shipments","alchemy labs","portals","time machines"]

		# buildings
		self.cursors = 0
		self.grandpas = 0
		self.farms = 0
		self.mines = 0
		self.factories = 0
		self.shipments = 0
		self.alchemists = 0
		self.portals = 0
		self.time_machines = 0

	# multipliers
		self.mult_click = 1
		self.mult_cursors = 1
		self.mult_grandpas = 1
		self.mult_farms = 1
		self.mult_mines = 1
		self.mult_factories = 1
		self.mult_shipments = 1
		self.mult_alchemists = 1
		self.mult_portals = 1
		self.mult_time_machines = 1

	# base costs
		self.cost_cursors = 10
		self.cost_grandpas = 80
		self.cost_farms = 800
		self.cost_mines = 80_000
		self.cost_factories = 800_000
		self.cost_shipments = 8_000_000
		self.cost_alchemists = 80_000_000
		self.cost_portals = 800_000_000
		self.cost_time_machines = 8_000_000_000

	# pps
		self.pps_cursors = 0.5
		self.pps_grandpas = 1.5
		self.pps_farms = 10
		self.pps_mines = 50
		self.pps_factories = 200
		self.pps_shipments = 500
		self.pps_alchemists = 2000
		self.pps_portals = 8000
		self.pps_time_machines = 25000

v = variable_class()

# functions #
def buy(bypass=None):
	clear()
	print(f"you have:{v.pineapples:,}\n\nshop:\n  [1] buildings\n  [2] upgrades\n  [3] back\n")
	if bypass == None:
		option = input("> ")
	else:
		option = str(bypass)
	match option:
		case "1":
			clear()
			print(f"you have: {v.pineapples:,}\n\nbuildings\n  [1] cursors (${v.cost_cursors:,})\n  [2] grandpas (${v.cost_grandpas:,})\n  [3] farms (${v.cost_farms:,})\n  [4] mines (${v.cost_mines:,})\n  [5] factories (${v.cost_factories:,})\n  [6] shipments (${v.cost_shipments:,})\n  [7] alchemists (${v.cost_alchemists:,})\n  [8] portals (${v.cost_portals:,})\n  [9] time machines (${v.cost_time_machines:,})\n{Fore.BLUE}  [0] update pineapple count{Fore.RESET}\n\n{Fore.GREEN}{v.store_message if bypass != None else ''}{Fore.RESET}")
			option = input("> ")
			match option:
				case "1":
					if v.pineapples > round(v.cost_cursors):
						v.pineapples -= round(v.cost_cursors)
						v.cursors += 1
						v.cost_cursors = round(v.cost_cursors * 1.1)
						v.store_message = f"bought a cursor for ${v.cost_cursors:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "2":
					if v.pineapples > round(v.cost_grandpas):
						v.pineapples -= round(v.cost_grandpas)
						v.grandpas += 1
						v.cost_grandpas = round(v.cost_grandpas * 1.1)
						v.store_message = f"bought a grandpa for ${v.cost_grandpas:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "3":
					if v.pineapples > round(v.cost_farms):
						v.pineapples -= round(v.cost_farms)
						v.farms += 1
						v.cost_farms = round(v.cost_farms * 1.1)
						v.store_message = f"bought a farm for ${v.cost_farms:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "4":
					if v.pineapples > round(v.cost_mines):
						v.pineapples -= round(v.cost_mines)
						v.mines += 1
						v.cost_mines = round(v.cost_mines * 1.1)
						v.store_message = f"bought a mine for ${v.cost_mines:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "5":
					if v.pineapples > round(v.cost_factories):
						v.pineapples -= round(v.cost_factories)
						v.factories += 1
						v.cost_factories = round(v.cost_factories * 1.1)
						v.store_message = f"bought a factory for ${v.cost_factories:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "6":
					if v.pineapples > round(v.cost_shipments):
						v.pineapples -= round(v.cost_shipments)
						v.shipments += 1
						v.cost_shipments = round(v.cost_shipments * 1.1)
						v.store_message = f"bought a shipment for ${v.cost_shipments:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "7":
					if v.pineapples > round(v.cost_alchemists):
						v.pineapples -= round(v.cost_alchemists)
						v.alchemists += 1
						v.cost_alchemists = round(v.cost_alchemists * 1.1)
						buy(1)
					else:
						buy(1)

				case "8":
					if v.pineapples > round(v.cost_portals):
						v.pineapples -= round(v.cost_portals)
						v.portals += 1
						v.cost_portals = round(v.cost_portals * 1.1)
						v.store_message = f"bought a portal for ${v.cost_portals:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)

				case "9":
					if v.pineapples > round(v.cost_time_machines):
						v.pineapples -= round(v.cost_time_machines)
						v.time_machines += 1
						v.cost_time_machines = round(v.cost_time_machines * 1.1)
						v.store_message = f"bought a time machine for ${v.cost_time_machines:,}"
						buy(1)
					else:
						v.store_message = f"{Fore.RED}not enough pineapples!{Fore.RESET}"
						buy(1)


			
				case "0":
					harvest()
					v.store_message = ""
					buy(1)

				case _:
					buy()
		

def credits():
	clear()
	input(f"micheal\n\npress{Fore.BLUE} [ENTER] {Fore.RESET}to go back\n")
	
def stats():
	clear()
	print(f"{Fore.BLUE} |-|-| stats |-|-| {Fore.RESET}")
	print(f"pineapples: {v.pineapples}")
	print(f"most pineapples: {v.most_pineapples}")
	print(f"pps: {v.pps * v.pps_multiplier}")
	print(f"raw pps:{v.pps}")
	print(f"cursors: {v.cursors}")
	print(f"grandpas: {v.grandpas}")
	print(f"farms: {v.farms}")
	print(f"mines: {v.mines}")
	print(f"factories: {v.factories}")
	print(f"shipments: {v.shipments}")
	print(f"alchemists: {v.alchemists}")
	print(f"portals: {v.portals}")
	print(f"time machines: {v.time_machines}")
	print(f"\npress{Fore.BLUE} [ENTER] {Fore.RESET}to go back")
	input("> ")

def save():
	data = {}
	for variable in vars(v):
		data[variable] = vars(v)[variable]
	with open("save.json", "w") as f:
		json.dump(data, f)
						
def load():
		filepath = "save.json"
		with open(filepath, "r") as f:
			data = json.load(f)
			for variable in data:
				setattr(v, variable, data[variable])


def update_pps():
	pps = (v.cursors * v.pps_cursors * v.mult_cursors)
	pps += (v.grandpas * v.pps_grandpas * v.mult_grandpas)
	pps += (v.farms * v.pps_farms * v.mult_farms)
	pps += (v.mines * v.pps_mines * v.mult_mines)
	pps += (v.factories * v.pps_factories * v.mult_factories)
	pps += (v.shipments * v.pps_shipments * v.mult_shipments)
	pps += (v.alchemists * v.pps_alchemists * v.mult_alchemists)
	pps += (v.portals * v.pps_portals * v.mult_portals)
	pps += (v.time_machines * v.pps_time_machines * v.mult_time_machines)
	v.pps = pps

def harvest():

	# update pineapple count
	temp = v.pineapples
	v.pineapples += v.pps * (time.time() - v.lastharvest)
	v.lastharvest = time.time()
	v.pineapples = round(v.pineapples)
	v.harvest_message = f"{Fore.BLUE}+{v.pineapples - temp:,}{Fore.RESET}"
def clear():
	os.system("clear" if os.name == "posix" else "cls")

def printmainmenu():
	print(f"--------------------------\n{Fore.BLUE}|-|-| Pineapple Clicker |-|-|{Fore.RESET}\n--------------------------\n\noptions:\n	[1] {v.optionFirst}\n	[2] load game\n	[3] options\n	[4] credits\n	[5] Change Log\n	{Fore.RED}[6] exit{Fore.RESET}\n\n--------------------------\n{version}\n--------------------------")

def mainscreen():
	print(Fore.BLUE + "|-|-| Pineapple Clicker |-|-|" + Fore.RESET)
	print(f"--------------------------\n{v.name}\'s Pineapplery\n--------------------------\n" + f"{int(round(v.pineapples,0)):,}" + " pineapples")
	print(f"{v.pps:,}" + " pps")
	print(f"--------------------------\n[total] {v.harvest_message}")
	print(f"[click] {Fore.GREEN}{v.click_message}{Fore.RESET}\n{v.golden_pineapple_message}--------------------------")
	print(f"options:{Fore.BLUE}\n  [1] buy\n  [2] stats\n  [3] save\n  [4] change name\n  [5] change log{Fore.RED}\n  [6] exit{Fore.RESET}\n\n  {Fore.YELLOW}[7] {'COLLECT GOLDEN PINEAPPLE' if v.goldenpineapple == True else ''}{Fore.RESET}\n\n--------------------------\npress{Fore.BLUE} [ENTER] {Fore.RESET}to harvest or update your pineapple count")
	
def mainloop():
	v.goldenpineapple = True if random.randint(1,10) == 1 else False
	v.optionFirst = f"Continue"
	running = True
	while running:
		if v.pineapples > v.most_pineapples:
			v.most_pineapples = v.pineapples
		clear()
		update_pps()
		harvest()
		mainscreen()
		option = input("\n> ")
		v.golden_pineapple_message = ""
		
		if option == "":
			v.click_message = f"+{v.mult_click:,}!"
			v.pineapples += 1 * v.mult_click
		if option == "1":
			buy()
		if option == "2":
			stats()
		if option == "3":
			save()
		if option == "4":
			clear()
			option = input("new name:\n> ")
			v.name = option
		if option == "6":
			running = False
		if option == "5":
			changelog()
		if option == "7" and v.goldenpineapple == True:
			v.pineapples *= 2
			v.golden_pineapple_message = f"\n{Fore.YELLOW} [GOLDEN PINEAPPLE!] x2 pineapples. {Fore.RESET}"
	
# main game #
def main():
	clear()
	printmainmenu()

	# options 
	invalid_option = True
	while invalid_option:
		option = input("> ")
		try:
			if int(option) < 1 or int(option) > 6:
				clear()
				printmainmenu()
				time.sleep(0.2)
				clear()
				printmainmenu()
				print(f"{Fore.RED}invalid option{Fore.RESET}")
				continue
			else:
				invalid_option = False
			
		except:
			clear()
			printmainmenu()
			time.sleep(0.2)
			clear()
			printmainmenu()
			print(f"{Fore.RED}invalid option{Fore.RESET}")
			continue
	# end of option validation

	# option proccessing
	match option:
		case "1":
			v.lastharvest = time.time()
			mainloop()

		case "2":
			clear()
			load()

		case "3":
			clear()
			input(f"this feature doesnt work yet\npress{Fore.BLUE} [ENTER] {Fore.RESET}to go back\n")

		case "4":
			credits()

		case "5":
			changelog()
			
		case "6":
			clear()
			print(Fore.RED + "exitting...")
			exit(0)
	main()
main()

