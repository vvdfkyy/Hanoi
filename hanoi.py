def hanoi(n, source, target, auxiliary):
    # ^ Функция для перемещения дисков с одного столбика на другой
    
    
    if n == 1 :    # Если остался только один диск, просто перемещаем его
        
        print(f" Переміщуємо єдиний диск з {source} на  {target}")
        
    else :
        
        # Перемещаем верхние n-1 дисков с исходного столбика на вспомогательный
        hanoi(n - 1, source, auxiliary, target)
        
        # Перемещаем самый большой (нижний) диск с исходного столбика на целевой
        print(f"Переміщуємо диск {n} з {source} на {target}")
        
        # Перемещаем n-1 дисков со вспомогательного столбика на целевой
        hanoi(n - 1, auxiliary, target, source)


def main( ) :
    
    try :

        n = int(input("Введіть потрібну к-сть дисків : "))
                # ^ Запрашиваем у пользователя количество дисков
                
    except ValueError:
        print(" Помилка! Введіть ціле число! ")
        
        return

    print(" \n Рішення задачі Ханойські вежі: ")
    
    #  --                                                                --
    # |Вызываем функцию для перемещения дисков.                            |
    # |Здесь 'A' - исходный столбик, 'B' - целевой, 'C' - вспомогательный  |
    #  --                                                               --
    
    hanoi(n, " A ", " B ", " C ")





if __name__ == "__main__":
    main()