def get_roman_letter(n):
    letters = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    if 1 <= n <= 10:
        return letters[n-1]


def sub_roman(x, y):
    is_in_bounds = lambda a: 1 <= a <= 10
    # Das ist ein Shortcut, um eine Funktion namens is_in_bounds zu definieren,
    # die als Argument a erhält und 1 <= a <= 10 zurückgibt

    result = x + y
    if not (is_in_bounds(x) and is_in_bounds(y)) or not is_in_bounds(result):
        return "Fehler"
    return get_roman_letter(result)


def trib(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2

    return trib(n-1) + trib(n-2) + trib(n-3)


def search_max_slow(a):
    if len(a) == 1:
        return a[0]

    max_rec = search_max_slow(a[1:])

    if max_rec > a[0]:
        return max_rec
    return a[0]


def search_max_fast(a):

    def search_max_help(a, l):
        if l == len(a):
            return float("-inf")

        max_rec = search_max_help(a, l+1)

        if max_rec > a[l]:
            return max_rec
        return a[l]

    if len(a) > 0:
        return search_max_help(a, 0)


# Wenn die Liste leer ist, wirft man normal einen Fehler, aber das kam wahrscheinlich noch nicht in der Vorlesung
