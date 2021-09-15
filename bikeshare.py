import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ["january","february","march","april","may","june","all"]

DAYS = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input("Which city do you want to get the info from? (chicago, new york city, washington)? ")
    city = city.lower()
    while city not in CITY_DATA:
            print("Please, select a valid city name: chicago, new york city, washington")
          
            city = input("Which city do you want to get the info from? (chicago, new york city, washington)? ")      
            city = city.lower()
            
    
    month = input("Which month do you want to get de info from (all, january, february, march, april, may, june)? ")
    month = month.lower()
    while month not in MONTHS:
            print("Please, select a valid month: all, january, february, march, april, may, june")
          
            month = input("Which month do you want to get de info from (all, january, february, march, april, may, june)? ")
            month = month.lower()

    
    day = input ("Which day do you want to get de info from (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)? ")
    day = day.lower()
    while day not in DAYS:
            print("Please, select a valid day: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday")
          
            day = input("Which day do you want to get de info from (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)? ")
            day = day.lower()

                 
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
    file = CITY_DATA[city]
    
    df = pd.read_csv(file)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        
        month_index = MONTHS.index(month)
        
        df = df[df['month'] == month_index]
        
    if day != "all":
        
        df = df[df['weekday'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    mc_month = df['month'].mode()[0]
    print("The most common month from the given fitered data is: " + Months[mc_month].title())

    
    mc_day = df['weekday'].mode()[0]
    print("The most common day from the given fitered data is: " + mc_day)


    
    mc_hour = df['hour'].mode()[0]
    print("The most common start time hour from the given fitered data is: " + str(mc_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    mc_ss = df['Start Station'].mode()[0]
    print("The most commonly used start station from the given fitered data is: " + mc_ss.title())
    

    
    mc_es = df['End Station'].mode()[0]
    print("The most commonly used end station from the given fitered data is: " + mc_es.title())


    
    mc_ce = (df['Start Station'] + " / " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip from the given fitered data is: " + mc_ce.title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    ttt = df['Trip Duration'].sum()
    print("The total travel time (in seconds) from the given fitered data is: " + str(ttt))

    
    mtt = df['Trip Duration'].mean()
    print("The mean travel time (in seconds) from the given fitered data is: " + str(mtt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    utc = df['User Type'].value_counts()
    print("The counts of user types from the given fitered data are: ")
    print(utc)


    if 'Gender' in df.columns: 
        gc = df['Gender'].value_counts()
        print("The counts of genders from the given fitered data are: ")
        print(gc)


    if 'Birth Year' in df.columns:
        eyb = df['Birth Year'].min()
        print("The earliest year of birth  from the given fitered data is: "+ str(int(eyb)))
    
        mryb = df['Birth Year'].max()
        print("The most recent year of birth  from the given fitered data is: "+ str(int(mryb)))
    
    
        mcyb = df['Birth Year'].mode()[0]
        print("The most common year of birth  from the given fitered data is: "+ str(int(mcyb)))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def show_rows(df):        
    """Displays some rows of data upon request."""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    start_loc = 0
   
    while True:
        if view_data.lower() == 'no':
            break 
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display.lower() == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
