import requests

result = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')
data = result.json()

question_data = data['results']
