"""See https://docs.gspread.org/en/v6.1.2/oauth2.html."""

from datetime import datetime
from typing import Final, Sequence

import gspread
from gspread.utils import ValueInputOption

CLIENT: Final = gspread.service_account(
    filename=gspread.auth.DEFAULT_SERVICE_ACCOUNT_FILENAME,
)

SPREADSHEET: Final = CLIENT.open("Readings")

print(SPREADSHEET.sheet1.get("A1"))


def append_row(values: Sequence[str | int | float]):
    SPREADSHEET.sheet1.append_row(
        values,
        value_input_option=ValueInputOption.user_entered,  # So that dates aren't escaped.
    )


if __name__ == "__main__":
    print("Doing.")
    print(SPREADSHEET.sheet1.get("A1"))
    append_row((datetime.now().utcnow().isoformat(), 123))
    print("Done.")
