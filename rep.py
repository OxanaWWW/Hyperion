def holidaycost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental


def hotel_cost(num_nights):
    return num_nights * 23


def plane_cost(city_flight):
    if city_flight == 'Mexico':
        price = 100
    elif city_flight == 'LA':
        price = 200
    else:
        price = 130
    return price


def car_rental(rent_days):
    return rent_days * 20


num_nights = int(input('enter:'))
city_flight = input('enter:')
rent_days = int(input('enter:'))

result_flight = plane_cost(city_flight)
result_hotel = hotel_cost(num_nights)
result_rent_days = car_rental(rent_days)
print(holidaycost(result_hotel, result_flight, result_rent_days))
