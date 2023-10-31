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
    return

def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    return

def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    return

def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    return

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    return

def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    return

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    return

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    return
