'''
NOVEMBER 2022
ICS3U UNIT ASSIGNMENT - UNIT 2
CODED BY Calvin Lee

'''

###REMINDER THAT NO GLOBAL VARIABLES ARE INCLUDED HERE


#YOU ARE NOT RESPONSIBLE TO UNDERSTAND THIS FUNCTION
def generate_list_players(filename):
    names_list = []
    dob_list = []
    country_list = []
    nationalteam_list = []
    batting_list = []
    bowling_list = []
   
    file_in = open(filename, encoding="utf-8")
    file_in.readline()

    for line in file_in:
        line = line.strip().split(",")
       
        names_list.append(line[0])
        dob_list.append(line[1])
        country_list.append(line[2])
        nationalteam_list.append(line[3])
        batting_list.append(line[4])
        bowling_list.append(line[5])

   
    return names_list, \
            dob_list, \
            country_list, \
            nationalteam_list, \
            batting_list, \
            bowling_list


def print_menu(menu_list, program_title):

    print("\n"*5)
    print(program_title)
    print('*'*len(program_title))
    for i in range(0, len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')


def get_unique_countries(country_list):
    unique_countries = []
    for item in country_list:
        if item not in unique_countries and item != '':
            unique_countries.append(item)

    unique_countries.sort()
    return unique_countries


def print_unique_countries(unique_countries, datatype):
    print(f'\n\nAll {datatype} available are:')
    print("-"*20)
    for i in range(0, len(unique_countries)):
        print(f'{i+1:>3}. {unique_countries[i]}')
   
    print("\n")



def filter_all_listings(all_values_list, user_choice):
    matching_indexes_list = []

    for i in range(0, len(all_values_list)):
        if all_values_list[i] == user_choice:
            matching_indexes_list.append(i)

    return matching_indexes_list


def get_valid_option(options_list):
    possible_choice_values = []
    for i in range(0, len(options_list)):
        possible_choice_values.append(str(i+1))

    choice = input("Which number would you like to choose?: ")
    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1
    return options_list[choice]



def print_listings_index(list_indexes, all_name_list, all_nationalteam_list):

    for i in range(0, len(list_indexes)):
        current_index = list_indexes[i]
       
        name = all_name_list[current_index]
        team = all_nationalteam_list[current_index]
       
        s = f'{i+1:<3} {name} {team}'
        print(s)



def print_single_listing(current_index, name_list, dob_list, country_list, nationalteam_list, batting_list, bowling_list):

    name = name_list[current_index]
    dob = dob_list[current_index]
    country = country_list[current_index]
    team = nationalteam_list[current_index]
    batting_style = batting_list[current_index]
    bowling_style = bowling_list[current_index]

    print(name, dob, country, team, batting_style, bowling_style)


def print_all_listings(name_list, dob_list, country_list, nationalteam_list, batting_list, bowling_list):

    print("\n\nALL CRICKET PLAYERS")
    for i in range(0, 10):
        name = name_list[i]
        dob = dob_list[i]
        team = nationalteam_list[i]
        print(f'{name} {dob} {team}')



###YOU WILL ADD YOUR ADDITIONAL FUNCTIONS HERE

       
def get_unique_country_list(country_list):
    unique_origin_country_list = []
    for item in country_list:
        if item not in unique_origin_country_list and item != '':
            unique_origin_country_list.append(item)

    unique_origin_country_list.sort()
    return unique_origin_country_list

def print_country_origin_summary(team , team_list, unique_country_list, country_list):
    count = []
    for i in range(0, len(country_list)):
        count.append(0)

    for index in range(0,len(team_list)):
        if team_list[index] == team:
            country_description = country_list[index]
            country_number = unique_country_list.index(country_description)
            count[country_number] += 1
    return count

def print_coo_data(count,unique_country_list, team):
    Count = "Count:"
    COR = "Country of Origin: |"
           
    print("-" * 40)
    print(f'Your Team Choice : {team}')
    print("-" * 40)
    print(f'{COR:>27}{Count:>7}')
    print("-" * 40)
    for i in range(0, len(unique_country_list)):
        if count[i] != 0:
            print(f'{unique_country_list[i]:>24}  |{count[i]:>7}')


def find_year_data(dob_list):
    birth_year = []
    for i in range(0,len(dob_list)):
        var = int(dob_list[i][6:10])
        if var not in birth_year and var != '':
            birth_year.append(var)
    birth_year.sort() 
    return birth_year
        

def filter_birth_year(all_values_list, user_choice, complete_list, names_list):
    matching_indexes_list = []
    for i in range(0,len(complete_list)):
        if str(user_choice) == complete_list[i][6:10]:
            matching_indexes_list.append(names_list[i])
    return matching_indexes_list
        
def print_data(list_of_names, user_selection):
    number = 0
    print(f'\n\nShowing players born in : {user_selection}')
    print("*" * 30)
    for i in range(0, len(list_of_names)):
        number += 1
        print(f'{number:>3}.  | {list_of_names[i]}')
    
#MAIN
def main():
    program_title = "CRICKET PLAYERS"
    menu_items = ['See All Cricket Players', 'Filter by country', 'Count of Country Origin per team', 'Filter by Birth Year', 'Exit']

    all_name_list, \
        all_dob_list, \
        all_country_list, \
        all_nationalteam_list, \
        all_batting_list, \
        all_bowling_list = generate_list_players("cricket_players.csv")

    unique_countries = get_unique_countries(all_country_list)
   
    print_menu(menu_items, program_title)
    user_entry = get_valid_option(menu_items)
   
    while user_entry != 'Exit':

        ##PRINT ALL
        if user_entry == menu_items[0]:
            print_all_listings(all_name_list, \
                               all_dob_list, \
                               all_country_list, \
                               all_nationalteam_list, \
                               all_batting_list, \
                               all_bowling_list)
   

        #FILTER BY COUNTRY
        elif user_entry == menu_items[1]:

            print_unique_countries(unique_countries, "countries")
            current_country = get_valid_option(unique_countries)
           
            matching_indexes_list = filter_all_listings(all_country_list, current_country)
            print_listings_index(matching_indexes_list, all_name_list, all_nationalteam_list)

            current_listing_index = get_valid_option(matching_indexes_list)
                           
            print_single_listing(current_listing_index, \
                                 all_name_list, \
                                 all_dob_list, \
                                 all_country_list, \
                                 all_nationalteam_list, \
                                 all_batting_list, \
                                 all_bowling_list)



        #YOUR MENU OPTION HERE  
        elif user_entry == menu_items[2]:

            team_listings = get_unique_countries(all_nationalteam_list)
            print_unique_countries(team_listings, "teams")
            user_team_selection = get_valid_option(team_listings)

            country_listings = get_unique_country_list(all_country_list)
            country_data = print_country_origin_summary(user_team_selection, all_nationalteam_list, country_listings, all_country_list)
            print_coo_data(country_data, country_listings, user_team_selection)
           

        #YOUR MENU OPTION HERE
        elif user_entry == menu_items[3]:
            year_data = find_year_data(all_dob_list)
            print_unique_countries(year_data, "years")
            user_year_selection = get_valid_option(year_data)
            player_birth_data = filter_birth_year(year_data, user_year_selection, all_dob_list, all_name_list)
            print_data(player_birth_data, user_year_selection)
            
        print_menu(menu_items, program_title)
        user_entry = get_valid_option(menu_items)
       

    print("\n\nGoodbye!")
   

#NO CODE IS ADDED AFTER THIS POINT    
main()
