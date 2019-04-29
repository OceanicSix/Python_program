single_data={"latitude":0,
             "longitude":0,
             "datetime":0,
             "confidence":0,
             "date":0,
             "surface_temperature_celcius":0}

entire_data=[]

data=open("hotspot.csv","r")
next(data) # skip first line

for line in data:
    data_list = line.strip().split(",")
    single_data["latitude"]=int(data_list[0])
    single_data["date"]=data_list[1]
    single_data["air_temperature_celcius"]=int(data_list[2])
    single_data["relative_humidity"]=float(data_list[3])
    single_data["windspeed_knots"]=float(data_list[4])
    single_data["max_wind_speed"]=float(data_list[5])
    single_data["precipitation"]=data_list[6]
    entire_data.append(single_data.copy())

print(entire_data)