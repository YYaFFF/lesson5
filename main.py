import os
from faker.generator import random
import file_operations
from faker import Faker

FAKE = Faker("ru_Ru")
SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]
CONTEXT = {
    "first_name": "",
    "last_name": "",
    "job": "",
    "town": "",
    "strength": "",
    "agility": "",
    "endurance": "",
    "intelligence": "",
    "luck": "",
    "skill_1": "",
    "skill_2": "",
    "skill_3": ""
}
SPECIAL_LETTERS = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}
FILE_NAME = "result_cards/result_cards{}.svg"
SKILL_PATTERN = "skill_{}"
os.makedirs("result_cards", exist_ok=True)


def generate_random_character():
    CONTEXT["first_name"] = FAKE.first_name()
    CONTEXT["last_name"] = FAKE.last_name()
    CONTEXT["job"] = FAKE.job()
    CONTEXT["town"] = FAKE.city()
    CONTEXT["strength"] = random.randint(3, 18)
    CONTEXT["agility"] = random.randint(3, 8)
    CONTEXT["endurance"] = random.randint(3, 18)
    CONTEXT["intelligence"] = random.randint(3, 18)
    CONTEXT["luck"] = random.randint(3, 18)


def rename_skills():
    for x in range(10):
        skills_sample = random.sample(SKILLS, 3)
        runic_skills = []
        generate_random_character()
        for i in range(len(skills_sample)):
            skill = skills_sample[i]
            for letter, special_letter in SPECIAL_LETTERS.items():
                skill = skill.replace(letter, special_letter)
            runic_skills.append(skill)
            CONTEXT[SKILL_PATTERN.format(i + 1)] = runic_skills[i]
        file_operations.render_template("hero_card.svg", FILE_NAME.format(x + 1), CONTEXT)


def main():
    rename_skills()


if __name__ == "__main__":
    main()
