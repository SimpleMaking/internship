from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta
from typing import Generator, List, Tuple

@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        list_of_dates = list()
        for value in self.dates:
            start = value[0]
            end = value[1]
            step = timedelta(hours=24)
            date = start
            while date <= end:
                list_of_dates.append(date)
                date += step
        
        return list_of_dates


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)


