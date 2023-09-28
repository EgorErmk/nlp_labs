# вставьте код здесь
digit_2_text = {1:'one',
                2:'two',
                3:'three',
                4:'four',
                5:'five',
                6:'six',
                7:'seven',
                8:'eight',
                9:'nine'}

teen_2_text = { 10:'ten',
                11:'eleven',
                12:'twelve',
                13:'thirteen',
                14:'fourteen',
                15:'fifteen',
                16:'sixteen',
                17:'seventeen',
                18:'eighteen',
                19:'nineteen'}

tens_2_text =  {20:'twenty',
                30:'thirty',
                40:'fourty',
                50:'fifty',
                60:'sixty',
                70:'seventy',
                80:'eighty',
                90:'ninety'}

power_2_text = {100:'hundred',
                1000:'thousand',
                10**6:'million',
                10**9:'billion',
                10**12:'trillion',
                10**15:'quadrillion',
                10**18:'quintillion'}



def num2text(number):
    text = ''
    order_of_magnitude = len(str(number))
    if order_of_magnitude > 3:
        if order_of_magnitude % 3:
            text += ' ' + num2text(number//10**(order_of_magnitude -(order_of_magnitude % 3))) + ' ' + power_2_text[10**(3*(order_of_magnitude//3))]
            text += num2text(number%10**(order_of_magnitude -(order_of_magnitude % 3)))
        else:
            text += ' ' + num2text(number//(10**(order_of_magnitude-3))) + ' ' + power_2_text[10**(order_of_magnitude)]
            text += num2text(number%(10**(order_of_magnitude-3)))
    else:
        if number//100:
            text += ' ' + digit_2_text[number//100] + ' ' + power_2_text[100]
        if number%100 < 20 and number%100 > 9:
            text += ' ' + teen_2_text[number%100]
            return text
        if number%100 >= 20:
            text += ' ' + tens_2_text[10*(number//10)]
        if number%10:
            text += ' ' + digit_2_text[number%10]
    return text

print(num2text(1111612))