from datetime import datetime

def getMonthName(strdate, format="'%d-%b-%Y'"):
    return datetime.strptime(strdate, format).strftime("%b")

def removeExtraDoubleQuotation(data):
    return eval(data)

def csv_to_list_dict(csvdata):
    counter = 0
    keys = []
    my_list = []
    for row in csvdata:
        if counter == 0:
            keys = row
            counter+=1
        else:
            my_list.append(dict(zip(keys, row)))
    return my_list