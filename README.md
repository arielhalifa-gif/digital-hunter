# digital-hunter
Ariel Halifa
209643808
arava


### in this project....

the main file is listening to the intel topic produced by kafka
after validating we look for the target in the mysql database (this is the database I choose to work with)

# if the validation feild we sent that target to 'intel_signals_dlq' topic


# if the target is not in the database we save the target with distance = 0 km and priority = 99

if the target is in the bank of targets that means that the target is steel on priority so we use the haversine.py function to calculate the distance between lat and lon and save into the database