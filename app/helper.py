import datetime
import dateparser

from typing import List

class Helper():
    
    @staticmethod
    def _message(msg: str, e: Exception = None) -> str:
        """
        Helper function to print messages.

        Args:
            msg (str): Message.
            e (Exception, optional): Exception if raised. Defaults to None.

        Returns:
            str: message formatted.
        """
        if e: return f'{msg}. {type(e).__name__}: "{e}".'
        else: return f'{msg}'
    
    @staticmethod
    def parse_date(dates: str) -> List[datetime.datetime]:        
        """
        Parse date(s) from the calendar.

        Args:
            dates (str): Dates in format "dd-mm-yyyy". There can be single date, or two date with delimiter ' - '.

        Returns:
            List[datetime.datetime]: Tuple of start date and end date (if available).
        """
        format = '%d-%m-%Y'
        try:
            ds = dates.split(' - ')
            start_date = ds[0]
            end_date = ds[1] if len(ds) > 1 else None
            start_date = datetime.datetime.strptime(start_date, format)
            end_date = datetime.datetime.strptime(end_date, format) if end_date is not None else start_date + datetime.timedelta(days = 1)
            if start_date == end_date: end_date = end_date + datetime.timedelta(days = 1)
        except ValueError as e:
            print(e)
            return None
        
        return (start_date, end_date)

