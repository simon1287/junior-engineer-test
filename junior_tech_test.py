import csv

# I noted the wording "please don't use the pandas library or similar".
# Therefore, all functions have been developed without using libraries,
# such as math, collections, statistics etc.
# However, I have no issues implementing these. :-)

def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    try:
        with open(file_path, 'r') as data:
            reader = csv.DictReader(data)
            output = list(reader)
        return output
    except IOError as e:
        print(e)


def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """
        # As sets are unique data elements, duplicates are filtered-out
    unique_team_names = set(dict['team_name'] for dict in data)

    return unique_team_names

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_type_list = [dict['event_type_name'] for dict in data]

    func_output = max(set(event_type_list), key=event_type_list.count)

    return func_output


def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    team_name_filter = [dict for dict in data if dict['team_name'] == team_name]

    return team_name_filter


def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    team_name_filtered_data = filter_by_team(data,team_name)
    count = 0

    for dict in team_name_filtered_data:
        if dict['event_type_name'] == event_type_name:
            count += 1
    
    return count


def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    team_name_filtered_data = filter_by_team(data, team_name)
    pass_length_total = float()
    count = int()

    for dict in team_name_filtered_data:
        if dict['pass_length'] != '':
            pass_length_total += float(dict['pass_length'])
            count += 1
    
    avg_pass_length = round(pass_length_total / count, 1)

    return avg_pass_length


def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    # Returning a set, rather than a list, as returning a
    # filtered list fails the tests.

    position_name_filter = [dict for dict in data if dict['player_position_name']
                            == position_name]
    
    filtered_player_names = set(dictionary['player_name']
                                for dictionary in position_name_filter)
    
    return filtered_player_names


def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    successful_pass_filter = [dict for dict in data if dict['event_type_name']
                              == 'Pass' if dict['outcome_name'] == '']
    
    unique_entry_count = len(set(dict['id'] for dict in successful_pass_filter))

    return unique_entry_count


def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    period_filter = [dict for dict in data if dict['period'] == period]
        
    return period_filter


def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    player_name_filter = [dict for dict in data if dict['player_name']
                          == player_name if dict['event_type_name'] == 'Shot']
    unique_entry_count = len(set(dict['id'] for dict in player_name_filter))

    return unique_entry_count
