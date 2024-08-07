'''
The classes: DividendRecord, UnusualEntryChecker, DuplicateDivAmtChecker, and AlertManager were created by GPT4o and
may need to be modified significantly.
'''

class DividendRecord:
    def __init__(self, symbol, xDivDate, divAmt):
        self.Symbol = symbol
        self.xDivDate = xDivDate
        self.DivAmt = divAmt


class UnusualEntryChecker:
    def __init__(self):
        pass

    def check(self, records):
        raise NotImplementedError("Subclasses should implement this method")


class DuplicateDivAmtChecker(UnusualEntryChecker):
    def __init__(self):
        super().__init__()

    def check(self, records):
        unusual_entries = []
        record_dict = {}

        for record in records:
            key = (record.symbol, record.xDivDate)
            if key in record_dict:
                if record.divAmt != record_dict[key]:
                    unusual_entries.append(record)
            else:
                record_dict[key] = record.divAmt

        return unusual_entries


class AlertManager:
    def __init__(self):
        pass

    def send_alert(self, unusual_entries):
        for entry in unusual_entries:
            print(f"Unusual Entry Found: Symbol={entry.symbol}, xDivDate={entry.xDivDate}, DivAmt={entry.divAmt}")