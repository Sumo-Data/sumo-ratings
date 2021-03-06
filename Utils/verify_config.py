import os

# This file is responsible for ensuring all the variables in the config file are valid. 
# An error will be printed to the command line if the file is not valid, and the program will be aborted. 

def verify(config):
    errorList = [] 
    try:
        # K_VALUE must be an integer 
        if(type(config['K_VALUE']) != int): 
            errorList.append("K_VALUE must be an integer.")
        
        # BASE_RATING must be an integer
        if(type(config['BASE_RATING']) != int):
            errorList.append("BASE_RATING must be an integer.")
        
        # checks for the file provided in BOUTS_PATH
        # if the file does exist, confirms that it is a CSV. 
        if(os.path.isfile(config['BOUTS_PATH']) == False):
            errorList.append("Can not locate the file provided in BOUTS_PATH.")
        elif(config['BOUTS_PATH'].endswith(".csv")== False):
            errorList.append("BOUTS_PATH must be in .csv file format.")

        # WRESTLERS_PATH checks are the same as above except for the WRESTLERS_PATH variable. 
        if(os.path.isfile(config['WRESTLERS_PATH']) == False):
            errorList.append("Can not locate the file provided in WRESTLERS_PATH.")
        elif(config['WRESTLERS_PATH'].endswith(".csv")== False):
            errorList.append("WRESTLERS_PATH must be in .csv file format.")

        # checks to see if PRINT_CURRENT is a boolean value. 
        if(type(config['PRINT_CURRENT']) != bool):
            errorList.append("PRINT_CURRENT must be a boolean value.")
        
        # validating print options. Will be skipped if print_current is false 
        if(config['PRINT_CURRENT'] == True):

            # checks to see if PRINT_STYLE is an acceptable format 
            if(config["PRINT_STYLE"] not in ["short", "long"]):
                errorList.append("PRINT_STYLE is not a valid option. it must be 'short' or 'long' ")


        #checks to see if the save format is either a .csv or json 
        if(config["SAVE_FORMAT"] not in ["csv", "json"]):
            errorList.append("SAVE_FORMAT is not a valid option. It must be 'csv' or 'json'. ")
        
        # checks to see if SAVE_CAREER_HIGH is boolean.
        if(type(config['SAVE_CAREER_HIGHS']) != bool):
            errorList.append("SAVE_CAREER_HIGH must be a boolean value.")

        # checks to see if SAVE_DAILY is boolean. 
        if(type(config["SAVE_DAILY"]) != bool):
            errorList.append("SAVE_DAILY must be a boolean value.")
    
        # Check if the error list has any errors. if > 0, throw assertion error. 
        if (len(errorList) > 0):
            raise AssertionError 
        
    except AssertionError as err:
        print("Your configuration file contains the following errors: ")
        for i, error in enumerate(errorList): 
            print(" ",i+1, error)
        print()
        print("The errors in the configuration file must be corrected before the program can run.")
        exit()
