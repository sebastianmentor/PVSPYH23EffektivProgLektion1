from car import Car
from timeit import default_timer
import random
import string
import sys


ALPHABET = list(string.ascii_uppercase)
DIGITS = list(string.digits)



def create_all_car_with_all_license_plates() -> dict[str,list[Car]]:
    d = {}

    for first_pos in ALPHABET:
        d[first_pos] = []
        for second_pos in ALPHABET:
            for third_pos in ALPHABET:
                for i in DIGITS:
                    for j in DIGITS:
                        for k in DIGITS:
                            regnr = first_pos + second_pos + third_pos + i + j + k
                            d[first_pos].append(Car(regnr, '', ''))

    return d


def get_car_by_regno(regnr:str, dict_of_cars:dict[str,list[Car]]) -> Car|None:

    list_to_serach = dict_of_cars[regnr[0]]
    for car in list_to_serach:
        if car.regnr == regnr:
            return car

    return None    

def main():
    t_start = default_timer()
    cars_dict = create_all_car_with_all_license_plates()
    t_end = default_timer()
    print(f'Det tog {t_end - t_start} att skapa listan och tar upp {sys.getsizeof(cars_dict)//10**6}!')
    # print(cars_list[0].regnr, cars_list[1000].regnr, cars_list[7000000].regnr, cars_list[-1].regnr)


    while True:
        regnr = input('Ange regnummer:')
        if regnr == 'q': break
        
        t_start = default_timer()
        car = get_car_by_regno(regnr, cars_dict)
        t_end = default_timer()
        print(f'Sökningen tog {t_end-t_start}')

        if car:
            print('Hitta bil!')
        else:
            print('Bil finns inte :( ')
    
        





if __name__ == '__main__':
    main()