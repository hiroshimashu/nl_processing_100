""" 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ． """

def reverse_strings(str):
    new_str_list = list(reversed(str))
    new_str = "".join(new_str_list)
    return new_str

print(reverse_strings("stressed"))