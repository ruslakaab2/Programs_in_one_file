import time
num_str = {
    "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять",
    "6": "шесть", "7": "семь", "8": "восемь", "9": "девять", "10": "десять",
    "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать",
    "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать", "20": "двадцать",
    "30": "тридцать", "40": "сорок", "50": "пятьдесят", "60": "шестьдесят", "70": "семьдесят",
    "80": "восемьдесят", "90": "девяносто", "100": "сто", "200": "двести", "300": "триста",
    "400": "четыреста", "500": "пятьсот", "600": "шестьсот", "700": "семьсот",
    "800": "восемьсот", "900": "девятьсот", "1000": "тысяча"
}


def num_on_str(stroka):
    strochka = []
    stroka = stroka.split(" ")

    for num in stroka:
        if num.isdigit():
            num = int(num)
            if num < 1000:
                if num in num_str:
                    strochka.append(num_str[str(num)])
                else:

                    hundreds = num // 100 * 100
                    tens = (num % 100) // 10 * 10
                    units = num % 10

                    if hundreds > 0:
                        strochka.append(num_str[str(hundreds)])

                    if 10 <= num % 100 < 20:  # Обработка чисел от 11 до 19
                        strochka.append(num_str[str(num % 100)])
                    else:
                        if tens > 0:
                            strochka.append(num_str[str(tens)])
                        if units > 0:
                            strochka.append(num_str[str(units)])
            else:
                strochka.append("число больше 1000")  # Обработка чисел больше 1000
        else:
            strochka.append(num)

    return ' '.join(strochka)

