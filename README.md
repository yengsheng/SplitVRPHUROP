# SplitVRPHUROP
Useful .py files:

convert_to_tsplib.py: This file moves into each child file in the SDVRP instances, searches for the .cri file, and converts them into the TSPLIB format.

split_and_sol.py: Takes all the .txt files which have been converted from convert_to_tsplib.py, and creates two split versions as .vrp files: 
The first with the rounded-down demands, and the second with the x10 demands.
It also has the function that takes all the .txt/.vrp and creates the .sol file using vrp_rtr.exe, running Powershell using Python (This lagged my file explorer, probably because
of how inefficiently I wrote the code, please be patient if you run this with lots of files!)

apriorisplit.py: The split function is found here, when a .txt file is passed into the conversionista function, it spits out the two different .vrp files with the proper names

matplotlib_instead_lol.py: Takes in all the .txt/.vrp and .sol files and creates a .png with the plot. (WIP: still trying to figure out how to show where a split occurs on the
plot itself)

pathing.py: Uses turtle instead to draw the plots, which I've stopped using because of how slow it is

info_creation.py: I plan on writing a .csv file with all the objective distances, split locations, and original demand for the split locations using this .py file.

I've also included all the .eps files since they are much clearer plots
