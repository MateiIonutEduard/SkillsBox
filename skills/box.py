import requests as req
from bs4 import BeautifulSoup


class Answer(object):
    def __init__(self, title, answer):
        self.title = title
        self.answer = answer

    def __str__(self):
        res = '{}\n{}'.format(self.title, self.answer)
        return res


def GetAnswers(url):
    res = req.get('https://ebazhanov.github.io/{}'.format(url))
    soup = BeautifulSoup(res.content, "html.parser")

    quiz = []
    j = 0

    questions = soup.find_all('h4')
    answers = soup.find_all('ul', class_='task-list')

    for i in range(len(questions)):
        title = questions[i].text
        answer = None

        if i >= len(answers):
            break

        group = answers[i].contents

        for k in range(len(group)):
            item = group[k]

            if item == '\n':
                continue

            state = item.next
            j += 1

            if 'checked' in state.attrs:
                if state.attrs['checked'] == 'checked':
                    answer = item.text
                    break

        item = Answer(title, answer)
        quiz.append(item)

    return quiz


def FindAnswer(question, answers):
    for answer in answers:
        if question in answer.title:
            return answer.answer

    return None
