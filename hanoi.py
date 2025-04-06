def hanoi( n, source, target, auxiliary ) :
    
    if n == 1 : 
        print( f" Переміщуємо єдиний диск з {source} на  {target}" )
        
    else :
        hanoi( n - 1, source, auxiliary, target )
        print( f"Переміщуємо диск {n} з {source} на {target}" )
        hanoi( n - 1, auxiliary, target, source )

def main( ) :
    
    try :
        n = int( input("Введіть потрібну к-сть дисків : ") )
                
    except ValueError :
        print( " Помилка! Введіть ціле число! " )
        return

    print( " \n Рішення задачі Ханойські вежі: " )
    
    #  --                                                               --
    # |Викликаємо функцію переміщення дисків.                            |
    # |Тут 'A' - вихідний стовпчик, 'B' - допоміжний, 'C' - цільовий     |
    #  --                                                               --
    hanoi( n, " A ", " B ", " C " )

if __name__ == "__main__" :
    main( )
