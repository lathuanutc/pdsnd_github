import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to choose for analyzing? \n ie. chicago, new york city, washington: ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Your inputted city is invalid, please try again.")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True:
        month = input("Which month would you like to analyze? \n(ie. all, january, february,...,november, december): ").lower()
        if month in months:
            break
        else:
            print("Your inputted month is invalid. Please try again.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day of the week would you like to choose for analyzing?\n(all, monday, tuesday, ..., sunday): ").lower()
        if day in day_of_week:
            break
        else:
            print("Invalid day. Please try again.")

    print('-'*40)   
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if 'month' in df.columns and len(df['month']) > 0:
        most_common_month = df['month'].mode()[0]
        print("Most common month: {}".format(most_common_month))
    else:
        print("Month data is not available.")

    # TO DO: display the most common day of week
    if 'day_of_week' in df.columns and len(df['day_of_week']) > 0:
        most_common_day_of_week = df['day_of_week'].mode()[0]
        print("Most common day of week: {}".format(most_common_day_of_week))
    else:
        print("Day of week data is not available.")

    # TO DO: display the most common start hour
    if 'Start Time' in df.columns:
        df['hour'] = df['Start Time'].dt.hour
        if len(df['hour']) > 0:
            most_common_start_hour = df['hour'].mode()[0]
            print("Most common start hour: {}".format(most_common_start_hour))
        else:
            print("Start hour data is not available.")
    else:
        print("Start Time data is not available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    print("test")
    print(df['Start Station'].mode())
    # TO DO: display most commonly used start station
    start_station_mode_result = df['Start Station'].mode()
    end_station_mode_result = df['End Station'].mode()

    if not start_station_mode_result.empty:
        most_frequent_start_station = start_station_mode_result[0]
        print("Most common start station is: {}".format(most_frequent_start_station))
    else:
        print("No common start station found, the column might be empty.")

    if not end_station_mode_result.empty:
        most_frequent_end_station = end_station_mode_result[0]
        print("Most common end station is: {}".format(most_frequent_end_station))
    else:
        print("No common end station found, the column might be empty.")

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    trip_mode_result = df['trip'].mode()
    
    if not trip_mode_result.empty:
        most_frequent_trip = df['trip'].mode()[0]
        print("Most common trip: {}". format(most_frequent_trip))
    else:
        print("No coomon trip found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types is:")
    print(user_types)

    # Check if the 'Gender' column exists
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Gender counts:")
        print(gender_counts)
    else:
        print("The 'Gender' column does not exist in the DataFrame.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest birth year: {}".format(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max()
        print("Most recent birth year: {}".format(most_recent_birth_year))

        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year: {}".format(most_common_birth_year))
    else:
        print("Birth year data is not available.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no:\n').lower()
        start_loc = 0

        while view_data == 'yes':
            if df.empty:
                print("The DataFrame is empty.")
                break
            
            end_loc = min(start_loc + 5, len(df))
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            
    
            if start_loc >= len(df):
                print("No more data to display.")
                break
            
            view_data = input("Do you wish to continue? Enter yes or no:\n").lower()

            if view_data != 'yes':
                break
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
