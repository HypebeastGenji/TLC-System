
from cmath import nan
import pandas as pd

# filename = './data/testing.csv'

mode_add = True

def save_hours(data_file, person, hour_dict):

    tlc_data = pd.read_csv(data_file, index_col=0)
    for key in hour_dict:
        card_num = int(key)
        print('[JOB CARD NUMBER]:', card_num)

        
        column_title = person + " Hours"
        column_idx = tlc_data.columns.get_loc(column_title)
        try:
            card_idx = list(tlc_data.index).index(card_num)
        except ValueError:
            print("[JCN NOT FOUND]: Creating row")
            tlc_data.loc[card_num] = ['', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            card_idx = list(tlc_data.index).index(card_num)
        job_hours = tlc_data.values[card_idx][column_idx]
        print("current hours for " + person + ' = ' + str(job_hours))
        if job_hours == 0:
            print('yes')
            print(hour_dict[key])
            print(str(hour_dict[key]))
            print(str(hour_dict[key])[1:-1])
            print(card_num)
            tlc_data.at[card_num, column_title] = str(hour_dict[key])[1:-1]
            print('yes')
        else:
            print("New hours:", str(hour_dict[key])[1:-1])
            print('[JOINING HOURS]')
            new_hrs = job_hours + ', ' + str(hour_dict[key])[1:-1]
            print("[NEW HOURS]:", new_hrs)
            tlc_data.at[card_num, column_title] = new_hrs
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(tlc_data)
    print("----------------------------------------------------------------------------------------------------------------------------")

    tlc_data.to_csv('./data/output.csv')
        

def main(mode, save=False):

    person = input("Enter Person: ")
    hours_dict = {}

    mode_add = mode
    while mode_add == True:

        job_card = input("Enter JCN: ")
    
        def add_hours(jcn):
            
            hours = []
            hour = int(input("Enter hours: "))
            while True:
                hours.append(hour)
                hour = input("Enter hours: ")
                try:
                    hour = int(hour)
                except ValueError:
                    if hour == ':q':
                        print("[QUITTING]")
                        break
                    else:
                        print("[ERROR]: Please enter valid number of hours")
            if jcn not in hours_dict:
                hours_dict[jcn] = hours
            else:
                old_hours = hours_dict[jcn]
                print("Old hours:", old_hours)
                print("New hours:", hours)
                concat = input("Join hours? (y/n): ")
                while True:
                    if concat == 'y':
                        new_hours = old_hours + hours
                        hours_dict[jcn] = new_hours
                    elif concat == 'n':
                        decision = input("Which set of hours would you like to use? (new/old): ")
                        while True:
                            if decision == 'new':
                                print("[USING NEW HOURS]:", hours)
                                hours_dict[jcn] = hours
                            elif decision == 'old':
                                print('[USING OLD HOURS]:', old_hours)
                            else:
                                print('[ERROR]')
                                decision = input("Which set of hours would you like to use? (new/old): ")
                    else:
                        print('[ERROR]')
                        concat = input("Join hours? (y/n): ")
        add_hours(job_card)


        add_again = input("Add another?: ")
        if add_again in ["y", ' ', '', 'yes']:
            mode_add = True
            print(hours_dict)
            continue
        elif add_again == "no" or "n":
            mode_add == False
            print(hours_dict)
            save_hours('./data/testing.csv', person, hours_dict)
            break
        else:
            print(hours_dict)
            if save == True:
                save_hours('./data/testing.csv', person, hours_dict)
            break

def start():
    main(mode_add)

start()
