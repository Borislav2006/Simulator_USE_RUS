import logging
import json
import jmespath
import markups as nav
import ast
import random
import re
from contextlib import suppress
from aiogram import Dispatcher, Bot, types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound
from db import Database
from config import *
from other_functions import *

# Инициализируем бота
bot = Bot(token=BOT_TOKEN)  # Объект класса Bot
dp = Dispatcher(bot)  # Создали объект класса Dispatcher (нужен для хэндлеров)

# Включаем логирование, чтобы не пропустить важные сообщения красного цвета
logging.basicConfig(level=logging.INFO)

db = Database('database.db')

with open('tasks.json', encoding='utf-8') as json_file:
    WHOLE_THEORY = json.loads(json_file.read())  # Переменная, в которой хранится вся теория курса в формате JSON


class Message:
    """
     Класс работает с сообщениями:
     1) способен удалять сообщения
     2) способен печатать информацию, теорию, викторины и т.п.
    """

    def __init__(self):
        self.text_of_quiz_kind = read_text_file("Information\\text_of_quiz_kind")
        self.points_for_tasks = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 3, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1,
                                 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 24: 1, 25: 1, 26: 1}

    @staticmethod
    async def delete_messages(message: types.Message):
        """ Метод, способный удалять большие объекты: картинки, викторины и другое """
        with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
            await message.delete()

    @staticmethod
    async def del_last_message(human_id):
        """ Метод, удаляющий предыдущее сообщение """
        await bot.delete_message(human_id.from_user.id, human_id.message.message_id)

    async def del_output_text(self, text, human_id, menu=None):
        """ Метод, удаляющий предыдущее сообщение и печатающий текст с меню/без меню """
        await self.del_last_message(human_id)  # Удаляем предыдущее сообщение
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML")  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")

    @staticmethod
    async def output_text(text, human_id, menu=None):
        """ Метод, печатающий текст с меню/без меню """
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML")  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")

    async def output_of_quiz_kind(self, task_number, human_id, menu=None):
        """ Метод, печатающий виды викторины """
        incorrectly_solved_quizzes = db.get_incorrectly_solved_quizzes(human_id.from_user.id, task_number)
        if not incorrectly_solved_quizzes:
            count_incorrectly_solved_quizzes = 0
        else:
            count_incorrectly_solved_quizzes = len(json.loads(incorrectly_solved_quizzes))
        tasks_history = ast.literal_eval(db.get_tasks_history(human_id.from_user.id))
        number_of_quizzes_answered = tasks_history[f"task_{task_number}"]["number_of_quizzes_answered"]
        correctly_solved_quizzes = tasks_history[f"task_{task_number}"]["correctly_solved_quizzes"]
        correctly_solved_quizzes_in_percentages = 0
        incorrectly_solved_quizzes = tasks_history[f"task_{task_number}"]["incorrectly_solved_quizzes"]
        incorrectly_solved_quizzes_in_percentages = 0
        if number_of_quizzes_answered != 0:
            correctly_solved_quizzes_in_percentages = round(correctly_solved_quizzes / number_of_quizzes_answered * 100, 1)
            incorrectly_solved_quizzes_in_percentages = round(incorrectly_solved_quizzes / number_of_quizzes_answered * 100, 1)
            if correctly_solved_quizzes_in_percentages % 1 == 0:
                correctly_solved_quizzes_in_percentages = int(correctly_solved_quizzes_in_percentages)
            if incorrectly_solved_quizzes_in_percentages % 1 == 0:
                incorrectly_solved_quizzes_in_percentages = int(incorrectly_solved_quizzes_in_percentages)
        await self.del_output_text(self.text_of_quiz_kind.format(number_of_quizzes_answered,
                                                                 correctly_solved_quizzes,
                                                                 correctly_solved_quizzes_in_percentages,
                                                                 incorrectly_solved_quizzes,
                                                                 incorrectly_solved_quizzes_in_percentages,
                                                                 count_incorrectly_solved_quizzes,
                                                                 task_number), human_id, menu)

    async def output_any_random_quiz(self, task_number, human_id, is_option_2=False, random_quiz=None):
        """ Метод, удаляющий предыдущее сообщение, печатающий любую рандомную викторину """
        if not is_option_2:
            await self.del_last_message(human_id)
            random_quiz = random.choice(jmespath.search(f"task_{task_number}.*", WHOLE_THEORY))
        photo_conditions = types.MediaGroup()
        if random_quiz["quiz_condition"]:
            photo_conditions.attach_photo(types.InputFile(random_quiz["quiz_condition"]),
                                          caption=read_text_file(random_quiz["quiz_question"]),
                                          parse_mode="HTML")
            if random_quiz["photo_of_answer_options"]:
                photo_conditions.attach_photo(types.InputFile(random_quiz["photo_of_answer_options"]))
        elif random_quiz["photo_of_answer_options"]:
            photo_conditions.attach_photo(types.InputFile(random_quiz["photo_of_answer_options"]),
                                          caption=read_text_file(random_quiz["quiz_question"]),
                                          parse_mode="HTML")
        await bot.send_media_group(human_id.from_user.id, media=photo_conditions)

        db.set_random_quiz(human_id.from_user.id, json.dumps(random_quiz))
        db.set_correct_answer(human_id.from_user.id, random_quiz["correct_answer"])
        db.set_answered_the_quiz(human_id.from_user.id, False)

    async def output_random_incorrectly_solved_quiz(self, task_number, human_id):
        await self.del_last_message(human_id)
        incorrectly_solved_quizzes: str = db.get_incorrectly_solved_quizzes(human_id.from_user.id, task_number)
        if not incorrectly_solved_quizzes or incorrectly_solved_quizzes == "[]":
            await self.output_text("По этому заданию у Вас нет неверно решённых викторин!", human_id)
        else:
            incorrectly_solved_quizzes: list = json.loads(incorrectly_solved_quizzes)
            number_random_quiz = random.choice(incorrectly_solved_quizzes)
            for quiz in WHOLE_THEORY[f"task_{task_number}"]:
                quiz = WHOLE_THEORY[f"task_{task_number}"][quiz]
                if quiz["quiz_number"] == number_random_quiz:
                    await self.output_any_random_quiz(task_number, human_id, is_option_2=True, random_quiz=quiz)
                    break

    @staticmethod
    async def user_answer_processing(human_id, user_answer):
        """ Метод для обработки ответа на рандомную викторину """
        rndm_quiz = json.loads(db.get_random_quiz(human_id))
        tasks_history = ast.literal_eval(db.get_tasks_history(human_id))
        number_task = rndm_quiz["task_number"]
        correct_answer = str(db.get_correct_answer(human_id))
        incorrectly_solved_quizzes: str = db.get_incorrectly_solved_quizzes(human_id, number_task)
        if not incorrectly_solved_quizzes:
            incorrectly_solved_quizzes: list = []
        else:
            incorrectly_solved_quizzes: list = json.loads(incorrectly_solved_quizzes)
        if re.fullmatch(correct_answer, user_answer.capitalize()):
            tasks_history[f"task_{number_task}"]["correctly_solved_quizzes"] += 1
            tasks_history[f"task_{number_task}"]["number_of_quizzes_answered"] += 1
            db.set_tasks_history(human_id, json.dumps(tasks_history))
            if rndm_quiz["quiz_number"] in incorrectly_solved_quizzes:
                incorrectly_solved_quizzes.remove(rndm_quiz["quiz_number"])
                await bot.send_message(human_id,
                                       f"Поздравляю! Теперь эта викторина убрана из раздела неверно решённых "
                                       f"викторин для этого задания ЕГЭ")
                db.set_incorrectly_solved_quizzes(human_id, number_task,
                                                  json.dumps(incorrectly_solved_quizzes))
            else:
                await bot.send_message(human_id,
                                       f"Поздравляю! У Вас получилось решить это задание ЕГЭ!")
        else:
            tasks_history[f"task_{number_task}"]["incorrectly_solved_quizzes"] += 1
            tasks_history[f"task_{number_task}"]["number_of_quizzes_answered"] += 1
            db.set_tasks_history(human_id, json.dumps(tasks_history))
            if rndm_quiz["quiz_number"] not in incorrectly_solved_quizzes:
                incorrectly_solved_quizzes.append(rndm_quiz["quiz_number"])
                await bot.send_message(human_id,
                                       f"Ничего страшного! Теперь эта викторина занесена в раздел неверно решённых "
                                       f"викторин этого задания ЕГЭ")
                db.set_incorrectly_solved_quizzes(human_id, number_task,
                                                  json.dumps(incorrectly_solved_quizzes))
            else:
                await bot.send_message(human_id,
                                       f"Ничего страшного! В следующий раз у Вас получится решить это задание ЕГЭ!")


ms = Message()  # Экземпляр класса Message

"""

<b> ... </b> - Жирный текст

<i> ... </i> - Курсивный текст

<u> ... </u> - Подчеркнутый текст

<del> ... </del> - Зачеркнутый текст

<code> ... </code> - моно-шрифт

&lt;html&gt;Вопрос&lt;/html&gt; -> <html>Вопрос</html> ->

<a href='https://www.python.org/'>здесь</a>    -> ссылка

Чтобы вставить HTML код в сообщение блога, чтобы он не интерпретировался 
как команды HTML, нужно все символы < заменить на &lt;, а символы > на &gt;

"""
