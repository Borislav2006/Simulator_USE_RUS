import json
from bs4 import BeautifulSoup
from pathlib import Path
from re import fullmatch
from itertools import permutations

# import os
#
# os.rename(fr'C:\Python_Projects\USE_simulator_RUS\Tasks_materials\conditions_of_quizzes\task_4\quiz_6.png',
#           fr'C:\Python_Projects\USE_simulator_RUS\Tasks_materials\conditions_of_quizzes\task_4\quiz_{1}.png')
# for i in range(1, 59):
#     os.rename(fr'C:\Python_Projects\USE_simulator_RUS\Tasks_materials\conditions_of_quizzes\task_4\carbon ({i}).png',
#               fr'C:\Python_Projects\USE_simulator_RUS\Tasks_materials\conditions_of_quizzes\task_4\quiz_{i + 1}.png')


# def f():
#     path = Path('tasks.json')
#     WHOLE_THEORY = json.loads(path.read_text(encoding='utf-8'))
#     for i in range(1, 60):
#         WHOLE_THEORY[f"task_4"][f"quiz_{i}"]["quiz_condition"] = f"Tasks_materials\\conditions_of_quizzes\\task_4\\quiz_{i}.png"
#     path.write_text(json.dumps(WHOLE_THEORY, indent=4, ensure_ascii=False), encoding='utf-8')
#
#
# f()


class Soup:
    """ Класс для парсинга данных с сайта решу ЕГЭ """

    def __init__(self, soup, number_task):
        self.soup = soup
        self.number_task = number_task

    def questions(self, quiz_number=0, write_in_json=False, write_to_txt=False):
        questions = self.soup.find_all("div", class_="nobreak")
        counter = 1
        for i in questions:
            if i.find_parents("div", "expand"):
                pass
            else:
                question = i.find("p", class_="left_margin").text
                print(counter, question)
                if write_to_txt:
                    with open(rf"C:\Python_Projects\EGE_simulator_RUS\Tasks_materials\questions_for_quizzes\task_{self.number_task}\quiz_{counter}", "w", encoding="utf-8") as file:
                        file.write(question[:question.index(".") + 1])
                if write_in_json:
                    path = Path('tasks.json')
                    WHOLE_THEORY = json.loads(path.read_text(encoding='utf-8'))
                    WHOLE_THEORY[f"task_{self.number_task}"][f"quiz_{counter}"] = {
                        "task_number": self.number_task,
                        "quiz_number": quiz_number,
                        "quiz_condition": "",
                        "quiz_question": f"Tasks_materials\\questions_for_quizzes\\task_{self.number_task}\\quiz_{counter}",
                        "photo_of_answer_options": None,
                        "correct_answer": "",
                        "quiz_explanation": None,
                    }
                    path.write_text(json.dumps(WHOLE_THEORY, indent=4, ensure_ascii=False), encoding='utf-8')
                counter += 1
                quiz_number += 1

    def answer(self, write_in_json=False):
        answers = self.soup.find_all("div", class_="answer")
        counter = 1
        for answer in answers:
            if answer.find_parents("div", "expand"):
                pass
            else:
                val = answer.text[7:]
                if val.isdigit():
                    answer = "|".join(list(map(lambda x: "".join(x), permutations(val))))
                else:
                    answer = "|".join(list(map(str.capitalize, val.split("|"))))
                print(counter, answer)
                if write_in_json:
                    path = Path('tasks.json')
                    WHOLE_THEORY = json.loads(path.read_text(encoding='utf-8'))
                    WHOLE_THEORY[f"task_{self.number_task}"][f"quiz_{counter}"]["correct_answer"] = answer
                    path.write_text(json.dumps(WHOLE_THEORY, indent=4, ensure_ascii=False), encoding='utf-8')
                counter += 1

    def answer_options(self):
        questions = self.soup.find_all("div", class_="nobreak")
        counter2 = 1
        for i in questions:
            if i.find_parents("div", "expand"):
                pass
            else:
                options = i.find_all("p")[1:]
                counter = 1
                print(counter2)
                for option in options:
                    option = option.text.strip()
                    if fullmatch(r"\d\).+|\d\..+", option):
                        if option[1] == ".":
                            option = option.replace(".", ")", 1)
                            print(option)
                        else:
                            print(option)
                    elif option:
                        print(f"{counter})", option)
                        counter += 1
                counter2 += 1


def read_file(number_task: int) -> str:
    with open(rf"html/task_{number_task}.html", encoding="utf8") as file:
        return file.read()


task_number = 4
bouillon = BeautifulSoup(read_file(task_number), "lxml")
my_soup = Soup(bouillon, number_task=task_number)
my_soup.questions(
    quiz_number=0,
    write_in_json=False,
    write_to_txt=False
)
my_soup.answer(write_in_json=False)
# my_soup.answer_options()
