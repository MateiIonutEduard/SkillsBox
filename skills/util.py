import requests as req
from bs4 import BeautifulSoup


class Skill(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self):
        return self.name

    def getValue(self):
        return self.value


def GetSkills(url):
    res = req.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    table = soup.find('table')
    skills = []

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        item = columns[0].a

        skill = Skill(item.text, item.attrs['href'])
        skills.append(skill)

    return skills


def FindSkill(name, skills):
    for skill in skills:
        if skill.name == name:
            return skill.value

    return None
