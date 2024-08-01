import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york', 'washington']
months = ['all', 'january','february','march','april','may','june']
days =['all', 'sunday','monday','tuesday','wednesday','thrusday','friday','saturday']
#city = ''
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in cities:
            break
        else:
            print('Please enter a valid city name.')
     
    # TO DO: get user input for month,day or none
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        choice = input('Would you like to filter the data by month,day or none?\n').lower()
        if choice == 'month':
            month = input('Which month? January, February, March, April, May, June or All?\n' ).lower()
            day ='all'
            if month in months:
                break
            else:
                print('Please enter a valid month.')
        elif choice == 'day':
            day = input('Which day? Sunday, Monday....Saturday? Select All for no filter').lower()
            month = 'all'
            if day in days:
                break
            else:
                print('Please enter a valid day.')
        elif choice == 'none':
            month = 'all'
            day = 'all'
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
    #Load data file into dataframe
    df =pd.read_csv(CITY_DATA[city])
    #convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract month and day from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #Month filter if applicable
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month']== month]
     #day of week filter if aplicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = "January"
    elif popular_month == 2:
        popular_month = "February"
    elif popular_month == 3:
        popular_month = "March"
    elif popular_month == 4:
        popular_month = "April"
    elif popular_month == 5:
        popular_month = "May"
    elif popular_month == 6:
        popular_month = "June"
    print('Most Common Month: \n', popular_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week: \n', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    if popular_hour < 12:
        print('Most Common Start Hour: \n', popular_hour, ' AM')
    elif popular_hour >= 12:
        if popular_hour > 12:
            popular_hour -= 12
        print('Most Common Start Hour: \n', popular_hour, ' PM')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: \n", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: \n", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + " to " +  df['End Station']
    common_combo_station = combo_station.mode()[0]
    print("Most Common Trip from Start to End:\n {}".format(common_combo_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The Total Travel Time is {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    if minute> 60:
        hour, minute = divmod(minute, 60)
        print('The Average Travel Time is {} Hours, {} Minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The Average Trip Duration is {} Minutes and {} Seconds.'.format(minute, second))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type:\n", user_types)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of Each User Gender:')
        print(gender)
    except:
        print('Counts of Each User Gender:\nSorry, no gender data available for {} City'.format(city.title()))


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min() #earliest birth year
        recent = df['Birth Year'].max() #recent birth Year
        common = df['Birth Year'].mode() # Common Birth Year
        print('Counts of User Birth Year:')
        print('Oldest User(s) Birth Year: ', int(earliest))
        print('Youngest User(s) Birth Year: ', int(recent))
        print('Most Common Birth Year: ', int(common))
    except:
        print('Counts of User Birth Year:\nSorry, no birth year data available for {} City'.format(city.title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def  display_data(df):
    
    start_loc = 0
    end_loc = 5
    df_length = len(df.index)
    #Ask user if they want to see the first 5 rows of data?
    display_first_five = input('Do you want to see the first 5 rows of data? Enter Y or N.\n').lower()
    if display_first_five != 'y':
        return
        
    while start_loc < df_length:
        print(df.iloc[start_loc:start_loc+end_loc])
        start_loc += end_loc
        if start_loc < df_length:
            display_next_five = input('Do you want to see the next 5 rows of data? Enter Y or N.\n').lower()
            if display_next_five != 'y':
                break
     
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
