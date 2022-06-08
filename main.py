import skills.util as utils
import skills.box as box

if __name__ == '__main__':
    skills = utils.GetSkills('https://ebazhanov.github.io/linkedin-skill-assessments-quizzes/')
    name = input('Skill Name: ')

    running = True
    page = utils.FindSkill(name, skills)
    answers = box.GetAnswers(page)

    while running:
        question = input('Question: ')

        if not question:
            running = False

        if running:
            answer = box.FindAnswer(question, answers)

            if answer is not None:
                print('Answer: {}'.format(answer))

