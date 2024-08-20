from car import Car
from timeit import default_timer
import string
import sys


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



def get_car_by_regno(regnr:str, list_of_cars:list[Car]) -> Car|None:

    for car in list_of_cars:
        if car.regnr == regnr:
            return car
        elif car.regnr[0] > regnr[0]:
            break
        elif car.regnr[0] == regnr[0] and  car.regnr[1] > regnr[1]:
            break

    return None    


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