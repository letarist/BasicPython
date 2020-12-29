import json

final_list = []
first_dict = {}
second_dict = {}
average_profit = 0
number_of_firms_without_losses = 0

with open('task7.txt', 'r', encoding='utf-8') as file_read:
    for i in file_read:
        profit = 0
        profit_minus = 0
        cmd = i.split()

        if int(cmd[2]) < int(cmd[3]):
            profit_minus = int(cmd[2]) - int(cmd[3])
            first_dict[cmd[0]] = profit_minus
        else:
            profit = int(cmd[2]) - int(cmd[3])
            number_of_firms_without_losses += 1
            average_profit += profit
            first_dict[cmd[0]] = profit

    average_profit /= number_of_firms_without_losses
    second_dict['average_profit'] = average_profit
    final_list.append(first_dict)
    final_list.append(second_dict)
    print(final_list)
with open('task7.json', 'w', encoding='utf-8') as file_write:
    json.dump(final_list, file_write, indent=4)