
# запрос номера секции трубы и длины секции
section_numbers = []
section_lengths = []
while True:
    section_number = input('Введите номер секции трубы (или "стоп" для завершения ввода): ')
    if section_number.lower() == 'стоп':
        break
    section_length = float(input('Введите длину секции: '))
    section_numbers.append(section_number)
    section_lengths.append(section_length)

# подсчет суммы длин и количества секций
total_length = sum(section_lengths)
num_sections = len(section_numbers)

# запись результатов в файл
with open('pipe_sections.txt', 'w') as f:
    for i in range(num_sections):
        f.write(f'Номер секции {section_numbers[i]}: длина секции: {section_lengths[i]} мм\n')
        print(f'Номер секции (трубы) {section_numbers[i]}: , длина секции: {section_lengths[i]} мм\n')
    f.write(f'Суммарная длина: {total_length} м\n')
    f.write(f'Количество секций: {num_sections}')
    
    print(f'Общая длина трубопровода', total_length, 'мм')
    print(f'Трубопровод состоит из', num_sections, 'секций')
