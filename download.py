from datetime import datetime

import pandas_market_calendars as mcal

import IEXTools


def main() -> None:
    d1 = IEXTools.DataDownloader()

    nyse = mcal.get_calendar('NYSE')

    days = nyse.valid_days(start_date='2023-01-01', end_date='2023-10-03')
    print(f'Downloading from {days[0]} to {days[-1]}')
    for day in days:
        d1.download(day, feed_type='tops')


if __name__ == '__main__':
    main()
