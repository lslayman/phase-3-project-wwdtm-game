import requests, json

def fetch_trivia_questions(category=None, difficulty=None):
    url = 'https://opentdb.com/api.php?amount=10&type=multiple'
    params = {
        'category': category,
        'difficulty': difficulty
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    results = data['results']

    questions = []
    for result in results:
        question = result['question']
        incorrect_answers = result['incorrect_answers']
        correct_answer = result['correct_answer']
        questions.append({
            'question': question,
            'incorrect_answers': incorrect_answers,
            'correct_answer': correct_answer
        })

    return questions