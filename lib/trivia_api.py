import requests, json

def fetch_trivia_questions(category=None, difficulty=None):
    url = 'https://opentdb.com/api.php?amount=10&type=multiple'
    params = {
        'category': category,
        'difficulty': difficulty
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data['results']