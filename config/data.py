import os
from dotenv import load_dotenv

load_dotenv() # HAVE TO LOAD ENV VARIABLES FIRST

class Data:
    testbase = os.getenv("LOGIN")
    test_id = 22
    USERNAME = f"{testbase}{test_id}"
    EMAIL = f"{testbase}{test_id}@mail.ru"
    PASSWORD = f"{testbase}{test_id}"

    VACANT_USERNAME = f"{USERNAME}v"
    VACANT_EMAIL = f"{EMAIL}v"

    EMPTY_DATA = ""

    SPACE_BUTTON_DATA =" "
