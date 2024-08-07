team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
print('В команде "%s" - %s участников' % (team1_name, team1_num))
print('В команде "%s" - %s участников' % (team2_name, team2_num))
print('Итого сегодня в командах участников %s - %s' % (team1_num, team2_num))

#Использование format():
print('Команда "{}" решила задач: {}'.format(team1_name, score1))
print('Команда "{}" решила задач: {}'.format(team2_name, score2))
print('"{}" решили задачи за {}'.format(team2_name, team2_time))

#Использование f-строк:
print(f'Команды решили {score1} и {score2} задачи.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!.')