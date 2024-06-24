import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('three_amigos_quiz')

upcoming_quizzes = SHEET.worksheet('upcoming_quizzes')
past_quizzes_normal = SHEET.worksheet('past_quizzes_normal')
past_quizzes_cl = SHEET.worksheet('past_quizzes_cl')

data_upcoming_quizzes = upcoming_quizzes.get_all_values()
data_past_quizzes_normal = past_quizzes_normal.get_all_values()
data_past_quizzes_cl = past_quizzes_cl.get_all_values()

print(data_upcoming_quizzes)