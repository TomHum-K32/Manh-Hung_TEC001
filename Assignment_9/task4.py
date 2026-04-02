def caesar_file(file_name, shift, direction):
    f = open(file_name, "r")
    text = f.read()
    f.close()

    result = ""

    for ch in text:
        if ch.isalpha():
            if direction == "right":
                n = shift
            else:
                n = -shift

            if ch.isupper():
                x = ord(ch) - ord('A')
                y = (x + n) % 26
                new_ch = chr(y + ord('A'))
            else:
                x = ord(ch) - ord('a')
                y = (x + n) % 26
                new_ch = chr(y + ord('a'))

            result = result + new_ch
        else:
            result = result + ch

    f2 = open("output.txt", "w")
    f2.write(result)
    f2.close()


caesar_file("input.txt", 3, "right")