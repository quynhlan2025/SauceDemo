from time import strptime


def convert_month_word_to_number(monthWord):
    newWord = monthWord[0].upper() + monthWord[1:3].lower()
    month_number = strptime(newWord, '%b').tm_mon
    if len(str(month_number)) == 1:
        return "0" + str(month_number)
    return str(month_number)
