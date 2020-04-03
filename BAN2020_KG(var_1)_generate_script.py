import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('2/1/20 00:00:00', '%m/%d/%y %H:%M:%S')
d2 = datetime.strptime('2/3/20 23:59:59', '%m/%d/%y %H:%M:%S')

#print(random_date(d1, d2))

Max_Hubs = 3
Max_Devices = 10
Max_Users = 100000
Max_Assets = 10
#Max_Actions_1 = 10
#Max_Actions_2 = 10
Max_Step_1 = 100000
Max_Step_2 = 50000
Max_App_categories = 10
Max_Apps = 100
SPARQL_path = "C:/Blazegraph/1"


def createXML(filename):
    """
    Создаем XML файл.
    """
#Open SPARQL file
    spql = open("sparql_script.spql", "wt")

# Add header
    header = str("<?xml version='1.0' encoding='UTF-8'?>\n<rdf:RDF\nxmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\nxmlns:vCard='http://www.w3.org/2001/vcard-rdf/3.0#'\nxmlns:my='http://127.0.0.1/bg/ont/test1#'\n>")


# Add Hubs definitions
    f = open(filename + "_static.nq", "wt")
    f.write(header)
    f.write("\n<!--Hubs definitions-->\n")
    f.close()
    f = open(filename + "_static.nq", "at")

    i=1
    while i <= Max_Hubs:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Hub_") + str(i) + str("/'>\n<my:has_id>H") + str (i) + str("</my:has_id>\n</rdf:Description>\n")
        f.write(body)
        i=i+1


# Add Device models definitions

    f.write("\n<!--Device models definitions-->\n")


    i=1
    for j in ('Moto2k','Cisco3260','ArrisWB11','ArrisWB20'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Device_model_") + str(i) + str("/'>\n<my:has_id>") + str (j) + str("</my:has_id>\n</rdf:Description>\n")
        f.write(body)
        i=i+1

# Add tariffs definitions

    f.write("\n<!--Tariffs definitions-->\n")

    i = 1
    for j in ('Promo', 'Basic', 'Advance', 'Advance+', 'Profi'):
          body = str("<rdf:Description rdf:about='http://127.0.0.1/Tariff_") + str(i) + str("/'>\n<my:has_id>") + str(
           j) + str("</my:has_id>\n</rdf:Description>\n")
          f.write(body)
          i = i + 1

# Add Services definitions
    f.write("\n<!--Services definitions-->\n")

    i = 1
    for j in ('WatchTV', 'VOD', 'nPVR', 'PPV'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Service_") + str(i) + str("/'>\n<my:has_id>") + str(j) + str("</my:has_id>\n</rdf:Description>\n")
        f.write(body)
        i = i + 1

    f.write("\n</rdf:RDF>\n")
    f.close()
    spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_static.nq>;\n")

# Add App categories  definitions
    i = 1
    f = open(filename + "_app_categories_.nq", "at")
    f.write(header)
    f.write("\n<!--Application categories definitions-->\n")
    while i <= Max_App_categories:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/App_category_") + str(i) + str("/'>\n<my:has_id>App_category_") + str(
            i) + str("</my:has_id>\n<my:has_description>") + str("Application_category_") + str(i) + str(
            "</my:has_description>\n</rdf:Description>\n")
        f.write(body)
        i = i + 1
    f.write("\n</rdf:RDF>\n")
    f.close()
    spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_app_categories_.nq>;\n")

# Add Apps definitions
    i = 1
    f = open(filename + "_apps_.nq", "at")
    f.write(header)
    f.write("\n<!--Applications definitions-->\n")
    while i <= Max_Apps:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Application_") + str(i) + str(
            "/'>\n<my:has_id>Application_") + str(
            i) + str("</my:has_id>\n<my:has_app_category>App_category_") + str(random.randint(1, Max_App_categories)) + str(
            "</my:has_app_category>\n</rdf:Description>\n")
        f.write(body)
        i = i + 1
    f.write("\n</rdf:RDF>\n")
    f.close()
    spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_apps_.nq>;\n")

    # Add Device  definitions
    FileNum = 0
    i=1
    k=1
    j = ['Moto2k','Cisco3260','ArrisWB11','ArrisWB20']
    while i <= Max_Devices:
        FileNum = FileNum + 1
        f = open(filename + "_device_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Device definitions-->\n")
        while k <= Max_Step_1:
            body = str("<rdf:Description rdf:about='http://127.0.0.1/Device_") + str(i) + str("/'>\n<my:has_id>D") + str (i) + str("</my:has_id>\n<my:is_connected_to_hub>H") + str(random.randint(1, Max_Hubs)) + str("</my:is_connected_to_hub>\n<my:has_the_device_model>") + str(random.choice(j)) + str("</my:has_the_device_model>\n</rdf:Description>\n")
            f.write(body)
            i=i+1
            k=k+1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_device_" + str(FileNum) + "_.nq>;\n")
        k=1

# Add Assets  definitions
    i = 1
    f = open(filename + "_assets_.nq", "at")
    f.write(header)
    f.write("\n<!--Asset definitions-->\n")
    while i <= Max_Assets:
            body = str("<rdf:Description rdf:about='http://127.0.0.1/Asset_") + str(i) + str("/'>\n<my:has_id>Asset") + str(i) + str("</my:has_id>\n<my:has_description>") + str("Asset_number_") +str(i)+ str("</my:has_description>\n</rdf:Description>\n")
            f.write(body)
            i = i + 1
    f.write("\n</rdf:RDF>\n")
    f.close()
    spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_assets_.nq>;\n")


# Add Users  definitions
#    FileNum = 0
#    i = 1
#    k = 1
#    while i <= Max_Users:
#        FileNum = FileNum + 1
#        f = open(filename + "_user_" + str(FileNum) + "_.nq", "at")
#        f.write(header)
#        f.write("\n<!--User definitions-->\n")
#        while k <= Max_Step_1:
#            body = str("<rdf:Description rdf:about='http://127.0.0.1/User_") + str(i) + str("/'>\n<my:has_id>U") + str(i) + str("</my:has_id>\n<my:uses_device>D") + str(i) + str("</my:uses_device>\n</rdf:Description>\n")
#            f.write(body)
#            i = i + 1
#            k = k + 1
#        f.write("\n</rdf:RDF>\n")
#        f.close()
#        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_user_" + str(FileNum) + "_.nq>;\n")
#        k = 1


 # Add Householdd  definitions
    FileNum = 0
    i = 1
    k = 1
    j = ['Promo', 'Basic', 'Advance', 'Advance+', 'Profi']
    while i <= Max_Users:
        FileNum = FileNum + 1
        f = open(filename + "_household_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Household definitions-->\n")
        while k <= Max_Step_1:
            body = str("<rdf:Description rdf:about='http://127.0.0.1/HouseHold_") + str(i) + str("/'>\n<my:has_id>HH") + str(i) + str("</my:has_id>\n<my:has_tariff_plan>") + str(random.choice(j)) + str("</my:has_tariff_plan>\n</rdf:Description>\n")
            f.write(body)
            i = i + 1
            k = k + 1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_household_" + str(FileNum) + "_.nq>;\n")
        k = 1

# Add Accounts  definitions
    FileNum = 0
    i = 1
    k = 1
    while i <= Max_Users:
        FileNum = FileNum + 1
        f = open(filename + "_account_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Account definitions-->\n")
        while k <= Max_Step_1:
            body = str("<rdf:Description rdf:about='http://127.0.0.1/Account_") + str(i) + str(
                "/'>\n<my:has_id>A") + str(i) + str("</my:has_id>\n<my:has_household>HH") + str(i) + str(
                "</my:has_household>\n</rdf:Description>\n")
            f.write(body)
            i = i + 1
            k = k + 1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_account_" + str(FileNum) + "_.nq>;\n")
        k = 1

 # Add Account - Application links Type-1  definitions
    FileNum = 0
    i = 1
    k = 1
    while i <= Max_Users:
        FileNum = FileNum + 1
        f = open(filename + "_links_1_" + str(FileNum) + "_.nq", "at")
        f.write(header)
        f.write("\n<!--Add Account - Application links Type-1-->\n")
        while k <= Max_Step_2:
            body = str("<rdf:Description rdf:about='http://127.0.0.1/Account_") + str(i) + str(
                "/'>")
            f.write(body)
            l=1
            while l <= Max_App_categories:
                body = str("\n<my:entitled_to>Application_") + str(random.randint(1,Max_Apps)) + str("</my:entitled_to>")
                f.write(body)
                l = l + 1
            body = str("\n</rdf:Description>\n")
            f.write(body)
            i = i + 1
            k = k + 1
        f.write("\n</rdf:RDF>\n")
        f.close()
        spql.write("\nLOAD <file:///" + str(SPARQL_path) + "/" + filename + "_links_1_" + str(FileNum) + "_.nq>;\n")
        k = 1


    spql.close()

if __name__ == "__main__":
    createXML("KG_telecom")
