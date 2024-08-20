from car import Car
from timeit import default_timer
import string
import sys

#------------------------------------------------------------------------
# Implement binary search on the registration plates
#------------------------------------------------------------------------


ALPHABET = list(string.ascii_uppercase)
DIGITS = list(string.digits)



def create_all_car_with_all_license_plates() -> list[Car]:
    l = []

    for first_pos in ALPHABET:
        for second_pos in ALPHABET:
            for third_pos in ALPHABET:
                for i in DIGITS:
                    for j in DIGITS:
                        for k in DIGITS:
                            regnr = first_pos + second_pos + third_pos + i + j + k
                            l.append(Car(regnr, '', ''))

    return l

def calc_numeric_value_from_licens_plate(regnr:str) -> int:
    '''Converts a registration plate to a numeric value
    
       Exampel ABC123:
       A -> 65 ascii
       B -> 66 ascii 
       C -> 67 ascii
       123 -> number
       converts to -> 656667123 | '65'+'66'+'67'+'123' 
    '''
    first = str(ord(regnr[0]))
    second = str(ord(regnr[1]))
    third = str(ord(regnr[2]))
    num = regnr[3:]
    return int(first + second + third + num)

def get_car_by_regno(regnr:str, list_of_cars:list[Car]) -> Car|None:

    start = 0
    end = len(list_of_cars) - 1
    target_value = calc_numeric_value_from_licens_plate(regnr)
    count = 0
    
    while start <= end:
        mid = (end + start)//2
        count += 1

        if calc_numeric_value_from_licens_plate(list_of_cars[mid].regnr) == target_value:
            print(f'Found at index {mid} and took {count}')
            return True
        
        elif calc_numeric_value_from_licens_plate(list_of_cars[mid].regnr) < target_value:
            start = mid + 1

        else:
            end = mid - 1

    return False


def main():
    t_start = default_timer()
    cars_list = create_all_car_with_all_license_plates()
    t_end = default_timer()
    print(f'Det tog {t_end - t_start} att skapa listan och tar upp {sys.getsizeof(cars_list)//10**6}!')  

    while True:
        regnr = input('Ange regnummer:')
        if regnr == 'q': break
        
        t_start = default_timer()
        car = get_car_by_regno(regnr, cars_list)
        t_end = default_timer()
        print(f'Sökningen tog {t_end-t_start}')



        if car:
            print('Hitta bil!')
        else:
            print('Bil finns inte :( ')
    
        





if __name__ == '__main__':
    main()