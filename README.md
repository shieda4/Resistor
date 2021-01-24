# Resistor

## Story Time!

A client asked my to help him/her with her programming class final activity.   

She/he sent me her/his project proposal titled "Band Resistor color code Identification and Resistor Value Reader".

## Documentation

Inside main.py, along with the main function, there are 2 functions named  get\_resistor\_value and get\_color\_band.

### get_resistor_value

```python
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
```
