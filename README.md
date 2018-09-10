# Location-Entropy
Location entropy is a way to find out how famous partcular place is in terms of its visits by different people. While deciding the famous factor it not only considers the total number of visits by different people but also takes people' visit to other locations as well into account. Please refer to http://www-scf.usc.edu/~hto/resources/dple.pdf to get the clarity with example.

This repository contains the program (location_entropy.py) to find out the location entropy of given venues.

# Requirement
1. Python 2/3
2. Pandas

# Algorithm-
1. Take the input csv file containing userId and venueId columns.
2. Go through each row and update two dictionaries uid_to_loc and loc_to_uid. 
At any any instance uid_to_loc dictionary will have lost of all visited rows' uids. This value for venueIds for each key uid in itself will point to a dictionary which will contain all venue visited by this user and number of times visited. There will an entry 'total' also which will show how many places the user has visited any place. It has been used to get the P for the location in O(1) time. In short it will be <userId, <(venueId, frequency)|(total, frequency)>>.
The same way we are using loc_to_uid which is a dictionary of all visited rows' venueIds. The value uid for each key venueId will have all the userIds who have visited the place. The corresponding value to such userIds will be 1 (we are taking care of the frequency in uid_to_loc). In short, it will be <venueId, <userId:1>>
3. At the end you will have uid_to_loc and loc_to_uid dictionaries which will contain info about all users and venues.  So what we are doing is traversing all values in dictionary loc_to_uid and finding out all uid visiting to a loc. Info about how many time the user has visited the venue and whats the total frequency of the venue is given in uid_to_loc dictionary. We can directly apply the location entropy formula and can write the entropy to the  output file.

# How to run?
Customer can download or clone this repository. He need to have a user location visit file (csv file containing two coloumns 'userId' and 'venueId', there can more than these coloumns but those will not be used in program). For testing purpose two input files has been given here which can be used to test the program. 'sample_input' is a very small file to test and 'dataset_TSMC2014_NYC.csv' is dataset taken from kaggle dataset on NYC and Tokyo checkin(https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset).
The program output has been tested on both samples and giving good result with time complexity O(n) and space complexity O(n).

To run the program you need to be in this directory and run the following command-
python location_entropy.py <input_filename> <output_filename>
For example in case of sample_input.csv command will be like:
python location_entropy.py sample_input.csv sample_output.csv

The output <location_id, entropy> will be in <output_filename>. here by default we are not sorting the values w.r.t entropy but you can do it by uncommenting line number 74 '# entropy_list.sort(key=lambda x: x[1], reverse=True)' in location_entropy.py.
In case of any clearance, contact me on sunny.kmar.r@gmail.com
