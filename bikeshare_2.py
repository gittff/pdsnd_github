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

    while True:
        try:
            city = input("Enter the city (possible options: chicago, new york city, washington) ").lower()

            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print("\nThat\'s not a valid city!\n")
        except:
            print("No Input taken")
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Enter the month (possible options: all, january, february,..., june): ").lower()

            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print("\nThat\'s not a valid month!\n")
        except:
            print("No Input taken")
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter the day of week (possible options: all, monday, tuesday, ... sunday): ").lower()

            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print("\nThat\'s not a valid day of week!\n")
        except:
            print("No Input taken")
            break

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
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

# convert the Start Time column to datetime
#df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
#df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
#popular_hour = df['hour'].mode()[0]

#print('Most Popular Start Hour:', popular_hour)

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular travel month: ', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular travel day of week: ', popular_day_of_week)


    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]

    print('Most Popular travel hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_Station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_start_Station)

    # display most commonly used end station
    popular_end_Station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_end_Station)

    # display most frequent combination of start station and end station trip
    popular_route = (df['Start Station'] + " TO " + df['End Station']).mode()[0]
    print('Most Popular Route: ', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time: ", df['Trip Duration'].sum())

    # display mean travel time
    print("Mean Travel Time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nCounts of User Types: ", df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print("\nCounts of Gender: ", df['Gender'].value_counts())
    else:
        print("\nNo Gender Information to share.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        df['Birth Year']
        print("\nCustomers earliest year of birth: ", int(df['Birth Year'].min(skipna = True)))
        print("\nCustomers most recent year of birth: ", int(df['Birth Year'].max(skipna = True)))
        print("\nCustomers most common year of birth: ", int(df['Birth Year'].mode(dropna = True)[0]))
    else:
        print("\nNo Birth Year Information to share.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(iterable, size):
    #count = size
    """Yield successive chunks from iterable of length size."""
    yield iterable[0:size]



def raw_data_request(df):
    """Asks user whether he wants to see raw data"""
    raw_data_request = input('\nWould you like to see raw data? Enter yes or no.\n').lower()

    if raw_data_request != 'yes':
        return

    print(df.head(5))
    count = 5
    #more_raw_data_request = input('\nWould you like to see more raw data? Enter yes or no.\n').lower()
    while input('\nWould you like to see more raw data? Enter yes or no.\n').lower() == 'yes':
        '''###ToDo###: Use Generators###'''
        #for i, raw_data in my_enumerate(df, 1):
            #print("Raw Data {}: {}".format(i, raw_data))
        for raw_data in display_raw_data(df[count:], 5):
            print(raw_data)
        count += 5



    #break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_request(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
