def get_resistor_value(color_band):
    digits = {'Black': 0, 'Brown': 1,
              'Red': 2, 'Orange': 3,
              'Yellow': 4, 'Green': 5,
              'Blue': 6, 'Violet': 7,
              'Gray': 8, 'White': 9,
              'Gold': '', 'Silver': '',
              'No Color': ''}
    multiplier = {'Black': 1, 'Brown': 10,
                  'Red': 100, 'Orange': 1000,
                  'Yellow': 10000, 'Green': 100000,
                  'Blue': 1000000, 'Violet': 10000000,
                  'Gray': 100000000, 'White': 1000000000,
                  'Gold': 0.1, 'Silver': 0.01,
                  'No Color': ''}
    tolerance = {'Black': '', 'Brown': 1,
                 'Red': 2, 'Orange': 3,
                 'Yellow': 4, 'Green': '',
                 'Blue': '', 'Violet': '',
                 'Gray': '', 'White': '',
                 'Gold': 5, 'Silver': 10,
                 'No Color': 20}
    temp_coefficient = {'Black': 250, 'Brown': 100,
                        'Red': 50, 'Orange': 15,
                        'Yellow': 25, 'Green': 20,
                        'Blue': 10, 'Violet': 5,
                        'Gray': 1, 'White': '',
                        'Gold': '', 'Silver': '',
                        'No Color': ''}
    if len(color_band) == 4:
        first_digit = digits[color_band[0]]
        second_digit = digits[color_band[1]]
        multiplier_digit = multiplier[color_band[2]]
        tolerance_digit = tolerance[color_band[3]]

        first_digit = first_digit * 10
        second_digit = second_digit * 1
        total_digits = first_digit + second_digit

        print(str(total_digits * multiplier_digit) + ' ohms, a tolerance of (+/-)' + str(
            tolerance_digit) + '%')

    elif len(color_band) == 5:
        first_digit = digits[color_band[0]]
        second_digit = digits[color_band[1]]
        third_digit = digits[color_band[2]]
        multiplier_digit = multiplier[color_band[3]]
        tolerance_digit = tolerance[color_band[4]]

        first_digit = first_digit * 100
        second_digit = second_digit * 10
        third_digit = third_digit * 1
        total_digits = first_digit + second_digit + third_digit

        print(str(total_digits * multiplier_digit) + ' ohms, a tolerance of (+/-)' + str(
            tolerance_digit) + '%')

    elif len(color_band) == 6:
        first_digit = digits[color_band[0]]
        second_digit = digits[color_band[1]]
        third_digit = digits[color_band[2]]
        multiplier_digit = multiplier[color_band[3]]
        tolerance_digit = tolerance[color_band[4]]
        temperature_co_digit = temp_coefficient[color_band[5]]

        first_digit = first_digit * 100
        second_digit = second_digit * 10
        third_digit = third_digit * 1
        total_digits = first_digit + second_digit + third_digit

        print(str(total_digits * multiplier_digit) + ' ohms,a tolerance of (+/-)' + str(
            tolerance_digit) + '%' + ', and the temperature coefficient of ' + str(temperature_co_digit) + 'ppm/K')
    else:
        print('Invalid')


def get_color_band(resistor_value):
    digits = {0: 'Black', 1: 'Brown',
              2: 'Red', 3: 'Orange',
              4: 'Yellow', 5: 'Green',
              6: 'Blue', 7: 'Violet',
              8: 'Gray', 9: 'White'}
    multiplier = {1: 'Black', 10: 'Brown',
                  100: 'Red', 1000: 'Orange',
                  10000: 'Yellow', 100000: 'Green',
                  1000000: 'Blue', 10000000: 'Violet',
                  100000000: 'Gray', 1000000000: 'White',
                  0.1: 'Gold', 0.01: 'Silver'}
    tolerance = {1: 'Brown', 2: 'Red',
                 3: 'Orange', 4: 'Yellow',
                 5: 'Gold', 10: 'Silver', 20: 'No Color'}
    temp_coefficient = {250: 'Black', 100: 'Brown',
                        50: 'Red', 15: 'Orange',
                        25: 'Yellow', 20: 'Green',
                        10: 'Blue', 5: 'Violet',
                        1: 'Gray'}

    if len(resistor_value) == 2:
        resistor_digits = resistor_value[0]
        resistor_tolerance = resistor_value[1]
        print('4 Band Resistor')
        color_1 = digits[int(resistor_digits[0])]
        color_2 = digits[int(resistor_digits[1])]
        color_3 = multiplier[int(10 ** (len(resistor_digits) - 2))]
        color_4 = tolerance[int(resistor_tolerance)]
        print(color_1 + ' | ' + color_2 + ' | ' + color_3 + ' | ' + color_4)
        print('5 Band Resistor')
        color_1 = digits[int(resistor_digits[0])]
        color_2 = digits[int(resistor_digits[1])]
        color_3 = digits[int(resistor_digits[2])]
        color_4 = multiplier[int(10 ** (len(resistor_digits) - 3))]
        color_5 = tolerance[int(resistor_tolerance)]
        print(color_1 + ' | ' + color_2 + ' | ' + color_3 + ' | ' + color_4 + ' | ' + color_5)

    elif len(resistor_value) == 3:
        resistor_digits = resistor_value[0]
        resistor_tolerance = resistor_value[1]
        resistor_temperature_coefficient = resistor_value[2]

        print('6 Band Resistor')
        color_1 = digits[int(resistor_digits[0])]
        color_2 = digits[int(resistor_digits[1])]
        color_3 = digits[int(resistor_digits[2])]
        color_4 = multiplier[int(10 ** (len(resistor_digits) - 3))]
        color_5 = tolerance[int(resistor_tolerance)]
        color_6 = temp_coefficient[int(resistor_temperature_coefficient)]
        print(color_1 + ' | ' + color_2 + ' | ' + color_3 + ' | ' + color_4 + ' | ' + color_5 + ' | ' + color_6)
    else:
        print('Invalid')


if __name__ == "__main__":
    while True:
        print('[0] - Get Resistor Value')
        print('[1] - Get Color Band')

        selection = int(input())

        if selection == 0:
            colors = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Gray', 'White', 'Gold',
                      'Silver',
                      'No Color']
            print('Colors Available:')
            print(colors)
            print('Enter Colors - Comma Separated')
            colors_input = input()

            colors_input = colors_input.split(', ')
            get_resistor_value(colors_input)

        elif selection == 1:
            print('Enter ohms value, Tolerance, and or Temperature Coefficient - Comma Separated')
            values_input = input()
            values_input = values_input.split(', ')
            get_color_band(values_input)
        else:
            pass
