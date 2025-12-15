import file_operations
from faker import Faker
import random

fake = Faker('ru_RU')

runes = {
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
    'Я': 'Я̋'
}
def main():
    for i in range(10):
        fake_name = fake.first_name_male()
        fake_surname = fake.last_name()
        fake_city= fake.city()
        fake_job = fake.job()
        strength = random.randint(3, 19)
        power = random.randint(3, 19)
        agility = random.randint(3, 19)
        endurance = random.randint(3, 19)
        intelligence = random.randint(3, 19)
        luck = random.randint(3, 19)

        skill_list = ['Стремительный прыжок',
                      'Электрический выстрел',
                      'Ледяной удар',
                      'Стремительный удар',
                      'Кислотный взгляд',
                      'Тайный побег',
                      'Ледяной выстрел',
                      'Огненный заряд']

        k = 3
        skills = random.sample(skill_list, k)

        styled_skills = []
        for skill in skills:
            styled_skill = ''
            for char in skill:
                if char in runes:
                    styled_skill += runes[char]
                else:
                    styled_skill += char
            styled_skills.append(styled_skill)

        context = {
            'first_name': FAKE_NAME,
            'last_name': FAKE_SURNAME,
            'job': FAKE_JOB,
            'town': FAKE_CITY,
            'strength': strength,
            'power': power,
            'agility': agility,
            'endurance': endurance,
            'intelligence': intelligence,
            'luck': luck,
            'skill_1': styled_skills[0],
            'skill_2': styled_skills[1],
            'skill_3': styled_skills[2]
        }

        svg_content = file_operations.render_template('svg_files/charsheet.svg', f'svg_files/charsheet-{i}.svg',
                                                      context)
if __name__ == '__main__':
    main()
