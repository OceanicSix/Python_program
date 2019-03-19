controller_price = {-5: ["S", 49], -2: ["C", 12], 0: ["N", 0], 1: ["H", 5], 6: ["O", 39]}


# def cal_temperature(inner_temperature, external_temperature):
#     if inner_temperature < external_temperature:
#         return (inner_temperature + external_temperature) / 2
#     else:
#         return (3 * inner_temperature + external_temperature) / 4

def cal_temperature(inner_temperature, external_temperature):
    if inner_temperature < external_temperature:
        return (3*inner_temperature + external_temperature) / 4
    else:
        return (7* inner_temperature + external_temperature) / 8


def temp_violation(temp, r):
    if temp > 20 + r:
        return temp - (20 + r)
    elif temp < 20 - r:
        return (20 - r) - temp
    else:
        return 0


# find out how to adjust the temperature, so that there will be minimal violation in the next three hours
# when no more adjustment is made.
def temp_prediction(current_temp, r, *temp):
    temp_change_list = [-5, -2, 0, 1, 6]
    future_temp_list = temp
    minimal_violate_temp = 10000
    minimal_price = 10000

    for change in temp_change_list:
        violate_temp = 0
        weight = 1
        inner_temp = current_temp + change
        violate_temp += temp_violation(inner_temp, r) * weight
        if len(future_temp_list) != 0:
            for future_temp in future_temp_list:
                weight -= 0.2
                inner_temp = cal_temperature(inner_temp, future_temp)
                violate_temp += temp_violation(inner_temp, r) * weight

        if violate_temp <= minimal_violate_temp:
            minimal_violate_temp = violate_temp
            if violate_temp == 0:
                if controller_price[change][1] < minimal_price:
                    minimal_price = controller_price[change][1]
                    temp_change = change
            else:
                temp_change = change
    return temp_change


# Generate the required data into a list

def temp_list_generation(file_name):
    temp_file = open(file_name, "r")
    temp_list = []
    for line in temp_file:
        temp_list.append(float(line.strip()))
    return temp_list


def temp_change_generation(house_temp, r, temp_list):
    temp_change_list = []
    for index in range(len(temp_list)):
        house_temp = cal_temperature(house_temp, temp_list[index])
        if index <= len(temp_list) - 4:
            temp_change = temp_prediction(house_temp, r, temp_list[index + 1], temp_list[index + 2],
                                          temp_list[index + 3])
        elif index == len(temp_list) - 3:
            temp_change = temp_prediction(house_temp, r, temp_list[-2], temp_list[-1])
        elif index == len(temp_list) - 2:
            temp_change = temp_prediction(house_temp, r, temp_list[-1])
        elif index == len(temp_list) - 1:
            temp_change = temp_prediction(house_temp, r)
        house_temp += temp_change
        temp_change_list.append(temp_change)
    return temp_change_list


def house_temp_generation(house_temp, temp_change_list, temp_list):
    house_temp_list = []
    for index in range(len(temp_list)):
        house_temp = cal_temperature(house_temp, temp_list[index])
        house_temp += temp_change_list[index]
        house_temp = round(house_temp, 1)
        house_temp_list.append(house_temp)
    return house_temp_list


def mode_change_generation(temp_change_list):
    temp_change = []
    for change in temp_change_list:
        temp_change.append(controller_price[change][0])
    return temp_change


def price_generation(temp_change_list):
    price_list = []
    total_price = 0
    for change in temp_change_list:
        total_price += controller_price[change][1]
        price_list.append(total_price)
    return price_list


def violation_generation(house_temp_list, r):
    occurrence_list = []
    occurrence = 0
    violation_list = []
    violation_accumulation_list = []
    violation_sum = 0
    for temp in house_temp_list:
        violation = temp_violation(temp, r)
        violation_list.append(round(violation, 1))
        violation_sum += violation
        violation_accumulation_list.append(round(violation_sum, 1))
        if violation != 0:
            occurrence += 1
        occurrence_list.append(occurrence)
    return violation_list, occurrence_list, violation_accumulation_list


house_temp = 20
temp_list = temp_list_generation("OCT0107.txt")  # The data file
temp_change_list = temp_change_generation(20, 2, temp_list)
house_temp_list = house_temp_generation(house_temp, temp_change_list, temp_list)
mode_change_list = mode_change_generation(temp_change_list)
price_list = price_generation(temp_change_list)
violation_tuple = violation_generation(house_temp_list, 2)

#form the output string
output = ""
for index in range(len(temp_list)):
    output += str(temp_list[index]) + "\t" + str(house_temp_list[index]) + "\t" + mode_change_list[index] \
              + "\t" + str(price_list[index]) + "\t" + str(violation_tuple[0][index]) + "\t" \
              + str(violation_tuple[1][index]) + "\t" + str(violation_tuple[2][index])
    output += "\n"
print(output)
