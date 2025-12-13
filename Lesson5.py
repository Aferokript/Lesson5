import file_operations
from faker import Faker
import random

strength = random.randint(3, 19)
power = random.randint(3, 19)
agility = random.randint(3, 19)
endurance = random.randint(3, 19)
intelligence = random.randint(3, 19)
luck = random.randint(3, 19)

skill_list = ['Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар', 'Стремительный удар', 'Кислотный взгляд',
'Тайный побег','Ледяной выстрел','Огненный заряд']

for skills in skill_list:
    if skills == 'Стремительный прыжок':
        skills.replace('Стремительный прыжок', 'с͒т͒р̋͠е͠м͒͠ит͒е͠л̋͠ь̋н͒ы̋͠й͒͠ п̋͠р̋͠ы̋͠ж͒о̋ к̋̋')

k = 3
skills = random.sample(skill_list, k)
skill_dict = {
    'skill_1': skills[0],
    'skill_2': skills[1],
    'skill_3': skills[2]
}
fake = Faker('ru_RU')
fake_name = fake.first_name_male()
fake_surname = fake.last_name()
fake_city = fake.city()
fake_job = fake.job()
context = {
    'first_name':fake_name,
    'last_name':fake_surname,
    'job':fake_job,
    'town':fake_city,
    'strength':strength,
    'power':power,
    'agility':agility,
    'endurance':endurance,
    'intelligence':intelligence,
    'luck':luck,
    'skill_1':skills[0].replace('е', 'е͠'),
    'skill_2':skills[1].replace('е', 'е͠'),
    'skill_3':skills[2].replace('е', 'е͠')
}

file_operations.render_template('charsheet.svg', 'person_characteristics.svg', context)