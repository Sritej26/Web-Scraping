import os
import sys

states=[
	 "Aizwal",
	 "Allahabad",
	 "Andhra",
	 "Calcutta",
	  "Chattisgarh",
	  "Gauhati",
	  "Gujarat",
	  "Chandigarh",
	  "Itanagar",
	  "Jaipur",
	  "Jharkhand",
	 "Jodhpur",
	  "Karnataka",
	  "Kerala",
	  "Madras",
	  "Madurai",
	  "Delhi",
	  "Kohima",
	  "Manipur",
	  "Meghalaya",
	  "Shimla",
	  "Telangana",
	  "Tripura"
	]


def main():
	for state in states:
		print "\n"+state+":\n"
		os.system('python '+state+'/'+state+'.py')
	#os.system('python clists.py')

if __name__=='__main__':
	main()
