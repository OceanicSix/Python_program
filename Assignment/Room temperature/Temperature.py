house_temp = 20


def cal_temperature(inner_temperature, external_temperature):
    if inner_temperature < external_temperature:
        return (inner_temperature + external_temperature) / 2
    else:
        return (3 * inner_temperature + external_temperature) / 4


# temperature_file=open("JAN0107.txt","r")
# for line in temperature_file:
#     ex_temp=float(line.strip())
#     house_temp=cal_temperature(house_temp,ex_temp)
#     house_temp=round(house_temp,1)
# print(house_temp)

file_list = ["APR0814.txt", "AUG0107.txt", "JAN0107.txt", "OCT0107.txt"]
for file in file_list:
    temperature_file = open(file, "r")
    for line in temperature_file:
        ex_temp = float(line.strip())
        house_temp = cal_temperature(house_temp, ex_temp)
        house_temp = round(house_temp, 1)
    print("The final temperature for file " + file + " is: " + str(house_temp))
