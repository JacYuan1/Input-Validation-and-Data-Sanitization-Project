import csv
import re

file = open("") # Enter the path to the file here.
extract_data = csv.reader(file)

final_list = []

for i in extract_data:
    final_list.append(i)

previous_Val = ""

for outter_list in final_list:

    if outter_list[0] == "student":

       user_input = outter_list[1].strip()

       previous_Val = user_input

       if re.search("[\d]{3} [\d]{3} [\d]{3}", user_input) or re.search("\d{9}", user_input):
           
           print("Yes.")
           
       else:
           
           print("No.")

    elif outter_list[0] == "password":
        
        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[A-Za-z0-9\x20-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]{12,}$", user_input):
            
            print("Yes.")

        else:
            
            print("No.")

    elif outter_list[0] == "username":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[A-Za-z0-9]{3,20}$", user_input):

            print("Yes.")
        
        else:
            
            print("No.")

    elif outter_list[0] == "email":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[A-Za-z0-9]{3,20}@[A-Za-z0-9]{3,20}\.[A-Za-z0-9]{3,20}$", user_input):

            print("Yes.")
        
        else:
            
            print("No.")

    elif outter_list[0] == "previous":

        user_input = outter_list[1].strip()

        if user_input == previous_Val:

            print("Yes.")

        else:

            print("No.")

    elif outter_list[0] == "phone":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[\d]{10}$", user_input) or re.search("^[\d]{3}\.[\d]{3}\.[\d]{4}$", user_input) or re.search("^[\d]{3}\-[\d]{3}\-[\d]{4}$", user_input) or re.search("^\([\d]{3}\) [\d]{3}\-[\d]{4}$", user_input):
            
            print("Yes.")

        else:

            print("No.")

    elif outter_list[0] == "postal":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[A-Z][\d][A-Z][\d][A-Z][\d]$", user_input) or re.search("^[A-Z][\d][A-Z] [\d][A-Z][\d]$", user_input):

            print("Yes.")
        
        else:

            print("No.")

    elif outter_list[0] == "address":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[A-Za-z\d\.\-\ ]*$", user_input):

            print("Yes.")

        else:

            print("No.")

    elif outter_list[0] == "binary":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("^[10]*$", user_input):

            print("Yes.")

        else:

            print("No.")

    elif outter_list[0] == "bio":

        user_input = outter_list[1].strip()

        previous_Val = user_input

        if re.search("<(.*)>.*?|<(.*) />", user_input):

            print("No.")

        else:

            print("Yes.")

file.close