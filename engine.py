def 중복문자열제거(str):
    result = "".join(dict.fromkeys(str))
    return result


def 쌍자치환(string, PWkey):
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

    playFair = []
    encPlayFair = []
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    encStr = ""

    i = 0
    while i < len(string):
        tmpArr = [[], []]
        tmpArr[0] = string[i]
        try:
            if string[i] == string[i + 1]:
                tmpArr[1] = 'X'
                i -= 1
            else:
                tmpArr[1] = string[i + 1]
        except:
            tmpArr[1] = 'X'
        playFair.append(tmpArr)
        i += 2

    for i in range(len(playFair)):
        print(playFair[i][0] + "" + playFair[i][1] + "")
    for i in range(len(playFair)):
        tmpArr = [[], []]
        for j in range(len(board)):
            for k in range(len(board[j])):
                if playFair[i][0] == board[j][k]:
                    x1 = j
                    y1 = k
                if playFair[i][1] == board[j][k]:
                    x2 = j
                    y2 = k
        if x1 == x2:
            tmpArr[0] = board[x1][(y1+1) % 5]
            tmpArr[1] = board[x2][(y2+1) % 5]
        elif y1 == y2:
            tmpArr[0] = board[(x1+1) % 5][y1]
            tmpArr[1] = board[(x2+1) % 5][y2]
        else:
            tmpArr[0] = board[x2][y1]
            tmpArr[1] = board[x1][y2]

        encPlayFair.append(tmpArr)

    for i in range(len(encPlayFair)):
        encStr += str(encPlayFair[i][0]) + "" + str(encPlayFair[i][1]) + ""

    return encStr

