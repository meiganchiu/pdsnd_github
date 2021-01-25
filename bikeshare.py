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
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to see data for chicago, new york city or washington?").lower()
    while (city not in ['chicago','new york city','washington']):
        city = input("Please enter valid city name. Would you like to see data for chicago, new york city or washington?").lower()
    

    # get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to filter data by? Ex: all, january, february, march, april, may, june").lower()
    while (month not in ['all','january','february','march','april','may','june']):
        month = input("Please enter valid month. Which month would you like to filter data by? Ex: all, january, february, march, april, may, june").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = int(input("Which day? Please type your response in integer (ex. Monday = 0"))
    while (day not in [0,1,2,3,4,5,6]):
        day = int(input("Please enter valid day. Which day? Please type your response in integer (ex. Monday = 0)"))


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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
    #    days = [0,1,2,3,4,5,6]
    #    day = day.index(day)

        df = df[df['day_of_week'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['month'].mode()[0]
    print('The most common month is '+popular_month)

    # TO DO: display the most common day of week
    popular_day= df['day_of_week'].mode()[0]
    print('The most common day of week is '+popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most commonly start hour is '+popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is '+popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is '+popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    frequent_start_end_station = df['combination'].mode()[0]
    print('The most combination of start station and end station trip is '+frequent_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is '+total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is '+mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subscriber_count = len(df[df['User Type'] == 'Subscriber'])
    dependent_count = len(df[df['User Type'] == 'Dependent'])
    customer_count = len(df[df['User Type'] == 'Customer'])
    print('The counts of Subscriber is '+str(subscriber_count)+'; '
        'The counts of Dependent is '+str(dependent_count)+'; '
        'The counts of customer is '+str(customer_count))

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        female_count = len(df[df['Gender'] == 'Female'])
        male_count = len(df[df['Gender'] == 'Male'])
        print('The counts of female is '+str(female_count)+'; '
            'The counts of male is '+str(male_count))
    else:
        print('Gender column not found')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if "Birth Year" in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year is '+str(int(earliest_birth_year))+'; '
            'The most recent birth year is '+str(int(most_recent_birth_year))+'; '
            'The most common birth year is '+str(int(most_common_birth_year)))
    else:
        print('Birth year column not found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    raw = input("Would you like to see 5 lines of raw data? yes or no").lower()
    while True:
        if raw == "no":
            break
        else:
            print(df[i:i+5])
            raw = input("Would you like to see 5 more lines of raw data? yes or no").lower()
            i += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
