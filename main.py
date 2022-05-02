import pandas

NATO_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_dict = {row.letter: row.code for (index, row) in NATO_data_frame.iterrows()}
print(NATO_dict)

program_on = True

while program_on:
    user_word = input("Enter a word: ").upper()

    if user_word == "EXIT":
        program_on = False
    else:
        word = [NATO_dict[letter] for letter in user_word if letter in NATO_dict]
        print(word)
