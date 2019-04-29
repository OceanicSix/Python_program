from pprint import pprint

def result_gen(data_list):
    result = {"latitude": 0, "longitude": 0, "confidence": 0, "surface_temperature_celcius": 0}
    result["latitude"] = data_list[0]
    result["longitude"] = data_list[1]
    result["confidence"] = data_list[3]
    result["surface_temperature_celcius"] = data_list[5]
    return result


date_file=open("hotspot_historic.csv","r")
next(date_file) # skip first line

tolist_flag=False


single_data={"datetime":0, "result":0}

whole_data=[]

previous_datetime=0
for line in date_file:
    data_list=line.strip().split(",")
    if data_list[2] !=previous_datetime:
        if previous_datetime!=0:
            whole_data.append(single_data.copy())
        single_data["datetime"]=data_list[2]
        single_data["result"]=result_gen(data_list)
        tolist_flag = False
    else:
        if tolist_flag == False:
            single_data["result"]=[single_data["result"]]
            single_data["result"].append(result_gen(data_list))
            tolist_flag=True
        else:
            single_data["result"].append(result_gen(data_list))
    previous_datetime=data_list[2]


pprint(whole_data)


