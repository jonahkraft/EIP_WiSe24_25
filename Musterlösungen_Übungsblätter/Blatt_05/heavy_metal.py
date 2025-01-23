def ex1(sentence: str):
    words = sentence.split()
    result = []

    for word in words:
        chars = list(word.lower())
        is_capitalized = word[0].isupper()

        index = - 1
        counter = 0

        for i, e in enumerate(chars):
            if e in ["a", "o", "u"]:
                counter += 1
                if counter == 2:
                    index = i
                    break

        if index != -1:
            char = chars[index]

            if char == "a":
                chars[index] = "ä"
            elif char == "o":
                chars[index] = "ö"
            elif char == "u":
                chars[index] = "ü"

        new_word = "".join(chars)
        if is_capitalized:
            new_word = new_word.capitalize()

        result.append(new_word)

    return " ".join(result)


def ex2(sentence: str):
    words = sentence.split()
    result = []

    for word in words:
        chars = list(word.lower())
        is_capitalized = word[0].isupper()

        a_counter = o_counter = u_counter = 0
        index = -1

        for i, e in enumerate(chars):
            if e == "a":
                a_counter += 1
                if a_counter == 2:
                    index = i
                    break

            elif e == "o":
                o_counter += 1
                if o_counter == 2:
                    index = i
                    break

            elif e == "u":
                u_counter += 1
                if u_counter == 2:
                    index = i
                    break

        if index != -1:
            char = chars[index]

            if char == "a":
                chars[index] = "ä"
            elif char == "o":
                chars[index] = "ö"
            elif char == "u":
                chars[index] = "ü"

        new_word = "".join(chars)
        if is_capitalized:
            new_word = new_word.capitalize()

        result.append(new_word)

    return " ".join(result)


args = ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]
for arg in args:
    print(ex1(arg))
print()
for arg in args:
    print(ex2(arg))
