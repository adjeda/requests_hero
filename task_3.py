import requests
import datetime
from requests_html import HTML

def get_questions(tag: str, days: int):
    to_date = datetime.date.today()
    from_date = to_date - datetime.timedelta(days)
    url = "https://api.stackexchange.com/docs/questions"
    params = {'order': 'desc',
              'sort': 'activity',
              'filter': 'default',
              'tagged': 'python',
              'site': 'stackoverflow',
              'fromdate': f'{from_date}',
              'todate': f'{to_date}'}
    response = requests.get(url, params=params)
    html_str = response.text
    html = HTML(html=html_str)
    questions_summaries = html.find('.question-summary')
    print(questions_summaries)
    print(html_str)

get_questions('python', 2)