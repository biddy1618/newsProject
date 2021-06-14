import re
import datetime

from typing import List

class Helper():
    
    @staticmethod
    def generate_dates(start_date: str, end_date: str = None) -> List[str]:        
        """
        Generates date(s) for fetching url links for specific dates.

        Args:
            startDate (str): start date in format "dd.mm.yyyy"
            endDate (str, optional): end date in format "dd.mm.yyyy", should be later than start date. 
            Defaults to None.

        Returns:
            List[str]: list of dates for the given date range (days).
        """
        format = "%d.%m.%Y"
        try:
            start_date = datetime.datetime.strptime(start_date, format)
            end_date = datetime.datetime.strptime(end_date, format) if end_date is not None else start_date + datetime.timedelta(days=1)
        except Exception:
            raise ValueError("Please, input the date in following format: 'dd.mm.yyyy'.")
        
        if start_date >= end_date:
            raise AssertionError("Please, make sure that the end date is after the start date.")
        
        date_generated = [(start_date + datetime.timedelta(days=x)).strftime(format) for x in range(0, (end_date-start_date).days)]

        return date_generated

