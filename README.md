# Location-Entropy
Location entropy is a way to find out how famous partcular place is in terms of its visits by different people. While deciding the famous factor it not only considers the total number of visits by different people but also takes people' visit to other locations as well into account. Please refer to http://www-scf.usc.edu/~hto/resources/dple.pdf to get the clarity with example.

This repository contains the program (location_entropy.py) to find out the location entropy of given venues.

# Requirement
1. Python 2/3
2. Pandas

# How to run?
Customer can download or clone this repository. He need to have a user location visit file (csv file containing two coloumns 'userId' and 'venueId', there can more than these coloumns but those will not be used in program). For testing purpose two input files has been given here which can be used to test the program. 'sample_input' is a very small file to test and 'dataset_TSMC2014_NYC.csv' is dataset taken from kaggle dataset on NYC and Tokyo checkin(https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset).
The program output has been tested on both samples and giving good result with time complexity O(n) and space complexity O(n).

To run the program you need to be in this directory and run the following command-
python location_entropy.py <input_filename> <output_filename>
For example in case of sample_input.csv command will be like:
python location_entropy.py sample_input.csv sample_output.csv

The output <location_id, entropy> will be in <output_filename>. here by default we are not sorting the values w.r.t entropy but you can do it by uncommenting line number 74 '# entropy_list.sort(key=lambda x: x[1], reverse=True)' in location_entropy.py.
In case of any clearance, contact me on sunny.kmar.r@gmail.com
