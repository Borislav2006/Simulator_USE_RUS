import json
import jmespath
from pprint import pprint
from random import choice, shuffle
from trash import rubbish

Data = {
    "task_1": {
        "quiz_1": {
            "task_number": 1,
            "quiz_number": 1,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_1.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_1",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Что", "Потому что", "Так как", "Но"],
            "correct_answer_to_the_quiz": "Что",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_2": {
            "task_number": 1,
            "quiz_number": 2,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_2.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_2",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Разве", "Именно", "Только", "Неужели"],
            "correct_answer_to_the_quiz": "Именно",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_3": {
            "task_number": 1,
            "quiz_number": 3,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_3.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_3",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Но", "Потому что", "Когда", "Только"],
            "correct_answer_to_the_quiz": "Когда",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_4": {
            "task_number": 1,
            "quiz_number": 4,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_4.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_4",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Ней", "Книге", "Него", "Которой"],
            "correct_answer_to_the_quiz": "Которой",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_5": {
            "task_number": 1,
            "quiz_number": 5,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_5.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_5",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Такой", "Нашей", "Моей", "Их"],
            "correct_answer_to_the_quiz": "Такой",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_6": {
            "task_number": 1,
            "quiz_number": 6,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_6.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_6",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Поэтому", "Конечно", "Думаю", "Полагаю"],
            "correct_answer_to_the_quiz": "Конечно",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_7": {
            "task_number": 1,
            "quiz_number": 7,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_7.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_7",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Как", "Не", "Это", "Просто"],
            "correct_answer_to_the_quiz": "Это",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_8": {
            "task_number": 1,
            "quiz_number": 8,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_8.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_8",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Как раз", "Именно", "Точно", "Лишь"],
            "correct_answer_to_the_quiz": "Лишь",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_9": {
            "task_number": 1,
            "quiz_number": 9,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_9.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_9",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Его", "Эту", "Какую-то", "Всю"],
            "correct_answer_to_the_quiz": "Его",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_10": {
            "task_number": 1,
            "quiz_number": 10,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_10.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_10",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Некоторой", "Другой", "Какой-то", "Себя"],
            "correct_answer_to_the_quiz": "Другой",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_11": {
            "task_number": 1,
            "quiz_number": 11,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_11.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_11",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Сгоряча", "Назло", "Вовсе", "Кое-где"],
            "correct_answer_to_the_quiz": "Вовсе",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_12": {
            "task_number": 1,
            "quiz_number": 12,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_12.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_12",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Как раз", "Вовсе не", "Именно", "Лишь"],
            "correct_answer_to_the_quiz": "Лишь",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_13": {
            "task_number": 1,
            "quiz_number": 13,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_13.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_13",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Иных", "Некоторых", "Его", "Каких-то"],
            "correct_answer_to_the_quiz": "Иных",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_14": {
            "task_number": 1,
            "quiz_number": 14,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_14.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_14",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Считается", "Во-вторых", "Полагаю", "Думаю"],
            "correct_answer_to_the_quiz": "Во-вторых",
            "quiz_explanation": None,
            "quiz_note": None
        }
    },
    "task_10": {
        "quiz_1": {
            "task_number": 10,
            "quiz_number": 1,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_10\\quiz_1.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_10\\quiz_1",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["125", "124", "135", "245"],
            "correct_answer_to_the_quiz": "124",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_2": {
            "task_number": 10,
            "quiz_number": 2,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_10\\quiz_2.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_10\\quiz_2",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["25", "15", "235", "134"],
            "correct_answer_to_the_quiz": "25",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_3": {
            "task_number": 10,
            "quiz_number": 3,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_10\\quiz_3.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_10\\quiz_3",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["23", "34", "25", "124"],
            "correct_answer_to_the_quiz": "23",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_4": {
            "task_number": 10,
            "quiz_number": 4,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_10\\quiz_4.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_10\\quiz_4",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["34", "134", "235", "13"],
            "correct_answer_to_the_quiz": "34",
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_5": {
            "task_number": 10,
            "quiz_number": 5,
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_10\\quiz_5.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_10\\quiz_5",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["23", "12", "245", "34"],
            "correct_answer_to_the_quiz": "23",
            "quiz_explanation": None,
            "quiz_note": None
        }
    }
}


pprint(choice(jmespath.search("task_10.*", Data)))
