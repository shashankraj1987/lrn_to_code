def replace_pair(string: str) -> str:
    l = len(string)

    if l == 0 or l == 1:
        return string

    small_string = replace_pair(string[1:])

    if string[0] == small_string[0]:
        return string[0]+'*'+small_string[:l-2]
    else:
        return string[0]+small_string

print(replace_pair("hello"))