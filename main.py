import os
from faker.generator import random
import file_operations
from faker import Faker


fake = Faker("ru_Ru")

skills = ["Стремительный прыжок", "Электрический выстрел",
          "Ледяной удар", "Стремительный удар",
          "Кислотный взгляд", "Тайный побег",
          "Ледяной выстрел", "Огненный заряд"]

context = {
  "first_name": fake.first_name_male(),
  "last_name": fake.last_name_male(),
  "job": fake.job(),
  "town": fake.city(),
  "strength": random.randint(3, 18),
  "agility": random.randint(3, 18),
  "endurance": random.randint(3, 18),
  "intelligence": random.randint(3, 18),
  "luck": random.randint(3, 18),
  "skill_1": "",
  "skill_2": "",
  "skill_3": ""
}

special_letters = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

file_name = "result_cards/result_card{}.svg"
skill_pattern = "result_cards/result_card{}.svg"

os.makedirs(skill_pattern, exist_ok=True)


def rename_skills():
    for x in range(10):
        skills_sample = random.sample(skills, 3)
        runic_skills = []
        for i in range(len(skills_sample)):
            skill = skills_sample[i]
            for letter, special_letter in special_letters.items():
                skill = skill.replace(letter, special_letter)
            runic_skills.append(skill)
            context[skill_pattern.format(i + 1)] = runic_skills[i]
        file_operations.render_template("hero_card.svg", file_name.format(x + 1), context)


def main():
    rename_skills()


if __name__ == "__main__":
    main()
