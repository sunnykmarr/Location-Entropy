# Problem Statement: We are giving an input csv file containing two coloumns userId and venueId.
# Any userId, venueId combination means userId has visited venueId. There can multiple such instances.
# Our output will be location entropy for all venues (venueId)
# Formulae of 'Entropy for a Location' = −summation for all user ids(p(i) × log2(p(i)))
#
# This algorithm requires O(n) extra space (for two hash maps) and will require single scan of all entries in csv (means O(n) time complexity).
#
# Developer: Sunny Kumar
# sunny.kmar.r@gmail.com 
#
#

import pandas
import math
import sys

if(len(sys.argv)!=3):
	print("Please provide 2 argument: <input_filename>, <output_filename>")
	exit(-1)	
try:
	inpFile = pandas.read_csv(sys.argv[1], encoding='utf-8')
except:
	print("Please provide the correct input filename")
	exit(-1)

try:
	outFile= open(sys.argv[2], 'w')
except:
	print("You don't have permission to write/ create the location_output.csv")
	exit(-1)

if(('userId' not in inpFile.columns) or ('userId' not in inpFile.columns)):
	print("Input file doesn't have 'userId' or 'venueId' column")
	exit(-1)

# Method is comuting location entropy for all given venues.
def calculate_location_entropy():
	# uid_to_loc will contain a map from user to venue.
	uid_to_loc={}
	# loc_to_uid will contain a map from venue to user.
	loc_to_uid={}
	for i in range(0,len(inpFile)):
		if(inpFile.iloc[i]['userId'] in uid_to_loc.keys()):
			if(inpFile.iloc[i]['venueId'] in uid_to_loc[inpFile.iloc[i]['userId']].keys()):
				uid_to_loc[inpFile.iloc[i]['userId']][inpFile.iloc[i]['venueId']]=uid_to_loc[inpFile.iloc[i]['userId']][inpFile.iloc[i]['venueId']]+1
			else:
				uid_to_loc[inpFile.iloc[i]['userId']][inpFile.iloc[i]['venueId']]=1
			uid_to_loc[inpFile.iloc[i]['userId']]['total']=uid_to_loc[inpFile.iloc[i]['userId']]['total']+1
		else:
			uid_to_loc[inpFile.iloc[i]['userId']]={inpFile.iloc[i]['venueId']:1, 'total':1}

		if(inpFile.iloc[i]['venueId'] in loc_to_uid.keys()):
			if(inpFile.iloc[i]['userId'] in loc_to_uid[inpFile.iloc[i]['venueId']].keys()):
				continue
			else:
				loc_to_uid[inpFile.iloc[i]['venueId']][inpFile.iloc[i]['userId']]=1
		else:
			loc_to_uid[inpFile.iloc[i]['venueId']]={inpFile.iloc[i]['userId']:1}
			
	# Uncomment the next two lines  to get the values of both dictionaries
	# print(uid_to_loc)
	# print(loc_to_uid)
	
	# Entropy list will contain the list of venues and their entropies
	entropy_list=[]
	for i in loc_to_uid.keys():
		entropy=0
		for j in loc_to_uid[i].keys():
			# location entropy for location i w.r.t user j
			p=uid_to_loc[j][i]/uid_to_loc[j]['total']
			entropy=entropy-(p*math.log(p,2))
		entropy_list.append([i, entropy])
	# Uncomment the next line if you want to see the location entropy in decreasing order.
	# entropy_list.sort(key=lambda x: x[1], reverse=True)
	print(entropy_list)
	outFile.writelines("VenueId,Entropy\n")
	for i in range(0,len(entropy_list)):
		outFile.writelines(str(entropy_list[i][0])+","+str(entropy_list[i][1])+"\n")
	return entropy_list

calculate_location_entropy()
outFile.close()