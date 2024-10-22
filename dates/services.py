import requests

def get_sheet_upcoming_dates(api_id, tab_name=None):
    url = f'https://sheetdb.io/api/v1/fvi6b7rkv2z2b'
    if tab_name:
        url += f'?sheet={upcoming_quizzes}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None