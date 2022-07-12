import os.path


def caesar_encrypt(path_to_file, symbols_offset):
    alphabet_EN_lower, alphabet_EN_upper =  'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_RU_lower, alphabet_RU_upper = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    content = []
    encrypted_content = []
    

    def set_alphabet(letter):
        if letter in alphabet_EN_lower:
            return alphabet_EN_lower
        elif letter in alphabet_EN_upper:
            return alphabet_EN_upper
        elif letter in alphabet_RU_lower:
            return alphabet_RU_lower
        elif letter in alphabet_RU_upper:
            return alphabet_RU_upper
        else:
            raise ValueError('No alphabet!')


    #открываем файл на чтение
    with open(path_to_file, 'r') as f:
        for line in f:
            content.append(line)
    print('Successfully read!')

    for line in content: #перебираем строки в прочтенном файле
        encrypted_string = '' #пустая строка для добавления в результирующий список
        for alpha in line: #перебираем буквы в строке
            try:
                #устанавливаем нужный алфавит
                alphabet = set_alphabet(alpha)
                if alpha in alphabet:
                    position = alphabet.find(alpha) #ищем порядковый номер буквы в алфавите
                    new_position = position + symbols_offset
                    if new_position >= len(alphabet):
                        # если порядковый номер со смещением выходит за пределы диапазона алфавита, 
                        # то приводим к диапазону
                        new_position = (1 - position - symbols_offset) % (len(alphabet))
                    encrypted_string += alphabet[new_position]
            except ValueError: # обрабатываем исключение в случае если символ не входит в алфавит
                encrypted_string += alpha
        encrypted_content.append(encrypted_string)
    print('Successfully encrypted!')


    #открываем файл на запись и шифруем
    output_name, output_extension = os.path.splitext(path_to_file)
    with open(f'{output_name}_encrypted{output_extension}', 'w') as output_f:
        output_f.writelines(encrypted_content)
    print('Successfully wrote!')
