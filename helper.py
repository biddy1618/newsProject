import re
import datetime

from typing import List

class Helper():
    
    @staticmethod
    def generateDates(startDate: str, endDate: str = None) -> List[str]:        
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
            startDate = datetime.datetime.strptime(startDate, format)
            endDate = datetime.datetime.strptime(endDate, format) if endDate is not None else startDate + datetime.timedelta(days=1)
        except Exception:
            raise ValueError("Please, input the date in following format: 'dd.mm.yyyy'.")
        
        if startDate >= endDate:
            raise AssertionError("Please, make sure that the end date is after the start date.")
        
        date_generated = [(startDate + datetime.timedelta(days=x)).strftime(format) for x in range(0, (endDate-startDate).days)]

        return date_generated

