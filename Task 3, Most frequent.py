#Task 3, Most Frequent
# Liten hjelper for å gjøre en tekst om til ord (enkelt og nybegynnervennlig)
def simple_tokenize(text: str):
    # Gjør alt til små bokstaver
    text = text.lower()
    # Bytt ut vanlig tegnsetting med mellomrom
    for ch in ".!,?:;":
        text = text.replace(ch, " ")
    # Del opp på mellomrom
    words = text.split()
    return words

# a) Mest vanlige ord i a1 som ikke ligger i a2
def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:
    # Hvis lista er tom, returner tom streng
    if len(inputList1) == 0:
        return ""

    # Gjør en "forbudt"-liste (sett er raskt, men du kan også bruke liste)
    banned = set()
    for w in inputList2:
        banned.add(w)

    # Tell hvor ofte hvert ord dukker opp, men bare hvis det ikke er forbudt
    freq = {}       # ord -> antall
    last_pos = {}   # ord -> siste posisjon i inputList1

    for i in range(len(inputList1)):
        w = inputList1[i]
        if w not in banned:
            if w in freq:
                freq[w] = freq[w] + 1
            else:
                freq[w] = 1
            # lagre siste posisjon (blir oppdatert hver gang)
            last_pos[w] = i

    # Hvis alle ord var forbudt
    if len(freq) == 0:
        return ""

    # Finn ordet med høyest frekvens.
    # Ved lik frekvens: velg det som kommer SIST i lista (størst last_pos).
    best_word = ""
    best_count = -1
    best_last = -1

    for w in freq:
        count = freq[w]
        pos = last_pos[w]
        if count > best_count:
            best_word = w
            best_count = count
            best_last = pos
        elif count == best_count:
            if pos > best_last:
                best_word = w
                best_last = pos

    return best_word

# b) Mest vanlige ordet som kommer rett etter targetWord i inputList
def findMostFrequentFollower(inputList: list[str], targetWord: str) -> str:
    if len(inputList) == 0:
        return ""

    # Tell hva som følger etter targetWord
    freq = {}     # ord -> antall ganger det følger etter targetWord
    last_pos = {} # ord -> siste posisjon der det sto etter targetWord

    # Gå gjennom alle par (ord[i], ord[i+1])
    i = 0
    while i < len(inputList) - 1:
        if inputList[i] == targetWord:
            follower = inputList[i + 1]
            if follower in freq:
                freq[follower] = freq[follower] + 1
            else:
                freq[follower] = 1
            last_pos[follower] = i + 1  # lagre hvor det dukket opp sist
        i = i + 1

    # Hvis targetWord aldri ble funnet eller ikke hadde noe etter seg
    if len(freq) == 0:
        return ""

    # Finn ordet som følger oftest.
    # Ved likhet: velg det som står SIST i lista.
    best_word = ""
    best_count = -1
    best_last = -1

    for w in freq:
        count = freq[w]
        pos = last_pos[w]
        if count > best_count:
            best_word = w
            best_count = count
            best_last = pos
        elif count == best_count:
            if pos > best_last:
                best_word = w
                best_last = pos

    return best_word

# -----------------------------
# Eksempelbruk (du kan teste dette):
text = "This is the way. The way is shut. The door is the end."
words = simple_tokenize(text)

# a) Finn mest vanlig i words som ikke er i a2
a2 = simple_tokenize("is the")
print("a) ->", findMostFrequentWord(words, a2))

# b) Følger-ord
print("b) the ->", findMostFrequentFollower(words, "the"))   # forventet "way"
print("b) is  ->", findMostFrequentFollower(words, "is"))    # forventet "the"
print("b) way->", findMostFrequentFollower(words, "way"))  # forventet "is"
