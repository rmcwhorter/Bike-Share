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
    city = input("Please enter a city (Chicago, New York City, Washington):\n").lower()
    while city != "Chicago".lower() and city != "New York City".lower() and city != "Washington".lower():
        city = input(
            "Your input didn't match.\n"
            "Please enter one of the following cities: Chicago, New York City, Washington\n").lower()

    # get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
                        "october", "november", "december"]
    month = input("Please enter a month or 'all' for all months:\n").lower()
    while month != "all" and month not in months:
        month = input("Your input didn't match\nPlease enter a month (ex. january) or all for all months:\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Please enter a day (ex. monday) or all for all days:\n").lower()
    while day != "all" and day not in days:
        day = input("Your input didn't match\nPlease enter a day (ex. monday) or all for all days:\n").lower()


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
    if city == "washington":
        df = pd.read_csv("./washington.csv")
    elif city == "chicago":
        df = pd.read_csv("./chicago.csv")
    else:
        df = pd.read_csv("./new_york_city.csv")

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    if month != "all":
        month_num = month_to_number(month)
        df = df[df["month"] == month_num]
    if day != "all":
        df = df[df["day"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    common_month = month_to_string(int(common_month))
    print("The most common month of the year was: {}\n".format(common_month))

    # display the most common day of week
    common_day = df["day"].mode()[0]
    print("The most common day of the week was: {}\n".format(common_day))

    # display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour of the day was: {}\n".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The most common start station was: {}\n".format(common_start_station))

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The most common end station was: {}\n".format(common_end_station))

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time was: {}\n".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time was: {}\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Type counts:\n{}\n".format(user_types))

    # Display counts of gender
    gender = df["Gender"].value_counts()
    print("The gender counts:\n{}\n".format(gender))

    # Display earliest, most recent, and most common year of birth
    earliest_year = df["Birth Year"].min()
    latest_year = df["Birth Year"].max()
    most_common_year = df["Birth Year"].mode()[0]

    print("The earliest year of birth was: {}\n"
          "The latest year of birth was: {}\n"
          "the most common year of birth was: {}\n".format(earliest_year,latest_year,most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def month_to_number(month_string):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
              "october", "november", "december"]
    return months.index(month_string) + 1

def month_to_string(month_int):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
              "october", "november", "december"]
    return months[month_int-1]

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
