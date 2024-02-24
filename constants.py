import os, pathlib

# File Paths
HOME_DIRECTORY = pathlib.Path(__file__).parent.resolve()
LOGS_DIRECTORY = f'{HOME_DIRECTORY}/logs/'
REPORTS_DIRECTORY = f'{HOME_DIRECTORY}/reports'
LOG_FILENAME = 'codechef.log'

# HOME_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# LOGS_DIRECTORY = f'{HOME_DIRECTORY}/logs'
# REPORTS_DIRECTORY = F'{REPORTS_DIRECTORY}/reports'

# Constants
URL = "https://www.codechef.com/"
USERNAME = "berlin1999"
EMAIL = "berlin1999@proton.me"
USERNAME1 = "berlin1997"
EMAIL1 = "berlin1997@proton.me"
PASSWORD = "Password@123"
EMAIL2 = "berlin199@proton.me"
NEW_PASSWORD = "@Password@123"
WRONG_PASSWORD = "123@123"
COUNTRY = "United Kingdom"
TITLE = "Sign Up"
VERIFICATION_URL = "https://www.codechef.com/verify?destination=/getting-started"
DASHBOARD_URL = "https://www.codechef.com/dashboard"
ACCOUNT_URL = f"https://www.codechef.com/users/{USERNAME}"
COURSES_URL = "https://www.codechef.com/learn"
CONTEST_URL = "https://www.codechef.com/contests"
COURSE_NAME = "DSA in Python"
CONTACT_US_URL = "https://www.codechef.com/contactus"
EDIT_PROFILE_URL = "https://www.codechef.com/users/{username}/edit"
NEW_NAME = "ram"