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
    cities = ['chicago','new york city','washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Would you like to see data for Chicago, New York City, or Washington? '))
    n = city.lower() in cities

    while n == False :
        city = str(input('Invalid City /n Try again '))
        n = city in cities
      
    # TO DO: get user input for month (all, january, february, ... , june)                
    month = str(input('Which month? January, February, March, April, May, June or type \"all\" to apply no month filter ? '))
    n = month.lower() in months
    while n == False:
        month = str(input('Invalid month /n Try again '))
        n = month in months
    
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    day = str(input('which day? Sunday, Monday, Tuesday, Wednsday, Thursday, Friday, Saterday or type \"all\" to apply no day filter. '))
    n = day.lower() in days
    while n == False:
        day = str(input('Invalid day /n Try again '))
        n = day in days                        
        
    city = city.lower()
    month = month.lower()
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    
    if month == 'all':
        popular_month = df['month'].mode()[0]
        count_month = df['month'].value_counts()
        print('most common month: {} , count: {} '.format(popular_month , count_month[popular_month]))
    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        count_day = df['day_of_week'].value_counts()
        print('most common day of the week: {} , count: {} '.format(popular_day , count_day[popular_day])) 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts() 
    print('most common hour of the day: {} , count: {}'.format(popular_hour , count_hour[popular_hour]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    start_stations_count = df['Start Station'].value_counts()   
    print('Most Common Start Station :{} , count: {} '.format(popular_start_station , start_stations_count[popular_start_station]))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    end_stations_count = df['End Station'].value_counts()   
    print('Most Common End Station :{} , count: {} '.format(popular_end_station , end_stations_count[popular_end_station]))


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] ='Start: '+ df['Start Station'] +' , ' +'End: '+ df['End Station']
    popular_trip = df['Trip'].mode()[0]
    trip_count = df['Trip'].value_counts()
    print('Most Common Trip :({}) , count:{} '.format(popular_trip , trip_count[popular_trip]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
   
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_time_duration = df['Trip Duration'].sum()
    avg_travil_time = df['Trip Duration'].mean()
    
          
    # TO DO: display mean travel time
    print('Total duration : {} '.format(total_time_duration))   
    print('Average duration : {}\n '.format(avg_travil_time))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Count of each user type : \n{}'.format(user_types_count)) 

    # TO DO: Display counts of gender
    if city in ['new york city','chicago']:
        user_gender_count = df['Gender'].value_counts()
        print('Gender count : \n{}'.format(user_gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city in ['new york city','chicago']:
        popular_birth = df['Birth Year'].mode()[0]
        popular_birth_count = df['Birth Year'].value_counts()
        earliest_date = df['Birth Year'].min()
        recent_date = df['Birth Year'].max()
        print('\nEarliest year of birth: {} , count : {} \nMost recent year of birth: {} , count: {} \nMost common year of birth: {} , count : {}'.format(earliest_date , popular_birth_count[earliest_date] , recent_date  , popular_birth_count[recent_date] , popular_birth , popular_birth_count[popular_birth]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        start = 0
        end = 5
        
        while True:
            permision = input('\nWould you like to view individual trip data ? Enter yes or no\n')            
            trip_data = df[start:end]
            print(trip_data)
            if permision.lower() != 'yes':
                break
            start += 5
            end += 5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
