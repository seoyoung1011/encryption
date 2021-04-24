def 중복문자열제거(str):
    result = "".join(dict.fromkeys(str))
    return result


def encryption(string, PWkey):
    board = ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""]
    key = 중복문자열제거(PWkey).upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    al = ""
    string = string.replace(" ", "")
    string = string.upper()
    string = string.replace("Z", "Q")

    for a in alphabet:
        if a not in key:
            al += a
    alphabet = al

    count = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == "":
                board[i][j] += key[count]
            if count < len(key):
                count += 1
            if count == len(key):
                break
        if count == len(key):
            break

    count = 0
    for i in range(5):
        for j in range(5):
            if not board[i][j]:
                board[i][j] += alphabet[count]
                if count < len(alphabet):
                    count += 1
                if count == len(alphabet):
                    break
        if count == len(alphabet):
            break

    play_fair = []
    enc_play_fair = []
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    result = ""

    i = 0
    while i < len(string):
        tmp_arr = [[], []]
        tmp_arr[0] = string[i]
        try:
            if string[i] == string[i + 1]:
                tmp_arr[1] = 'X'
                i -= 1
            else:
                tmp_arr[1] = string[i + 1]
        except:
            tmp_arr[1] = 'X'
        play_fair.append(tmp_arr)
        i += 2

    for i in range(len(play_fair)):
        tmp_arr = [[], []]
        for j in range(len(board)):
            for k in range(len(board[j])):
                if play_fair[i][0] == board[j][k]:
                    x1 = j
                    y1 = k
                if play_fair[i][1] == board[j][k]:
                    x2 = j
                    y2 = k
        if x1 == x2:
            tmp_arr[0] = board[x1][(y1+1) % 5]
            tmp_arr[1] = board[x2][(y2+1) % 5]
        elif y1 == y2:
            tmp_arr[0] = board[(x1+1) % 5][y1]
            tmp_arr[1] = board[(x2+1) % 5][y2]
        else:
            tmp_arr[0] = board[x2][y1]
            tmp_arr[1] = board[x1][y2]

        enc_play_fair.append(tmp_arr)

    for i in range(len(enc_play_fair)):
        result += enc_play_fair[i][0] + "" + enc_play_fair[i][1] + ""

    return result


def Decryption(PW, PWkey):
    board = ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""], \
            ["", "", "", "", ""]
    key = 중복문자열제거(PWkey).upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    al = ""
    PW = PW.replace(" ", "")
    PW = PW.upper()

    for a in alphabet:
        if a not in key:
            al += a
    alphabet = al

    count = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == "":
                board[i][j] += key[count]
            if count < len(key):
                count += 1
            if count == len(key):
                break
        if count == len(key):
            break

    count = 0
    for i in range(5):
        for j in range(5):
            if not board[i][j]:
                board[i][j] += alphabet[count]
                if count < len(alphabet):
                    count += 1
                if count == len(alphabet):
                    break
        if count == len(alphabet):
            break

    play_fair = []
    dec_play_fair = []
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    result = ""

    i = 0
    while i < len(PW):
        tmp_arr = [[], []]
        tmp_arr[0] = PW[i]
        tmp_arr[1] = PW[i+1]
        play_fair.append(tmp_arr)
        i += 2

    for i in range(len(play_fair)):
        tmp_arr = [[], []]
        for j in range(len(board)):
            for k in range(len(board[j])):
                if play_fair[i][0] == board[j][k]:
                    x1 = j
                    y1 = k
                if play_fair[i][1] == board[j][k]:
                    x2 = j
                    y2 = k
        if x1 == x2:
            tmp_arr[0] = board[x1][(y1+4) % 5]
            tmp_arr[1] = board[x2][(y2+4) % 5]
        elif y1 == y2:
            tmp_arr[0] = board[(x1+4) % 5][y1]
            tmp_arr[1] = board[(x2+4) % 5][y2]
        else:
            tmp_arr[0] = board[x2][y1]
            tmp_arr[1] = board[x1][y2]

        dec_play_fair.append(tmp_arr)

    for i in range(len(dec_play_fair)):
        if (i != (len(dec_play_fair)-1)) and (dec_play_fair[i][1] == 'X') and (dec_play_fair[i][0] == dec_play_fair[i+1][0]):
            result += dec_play_fair[i][0]
        else:
            result += dec_play_fair[i][0] + "" + dec_play_fair[i][1]

    return result

