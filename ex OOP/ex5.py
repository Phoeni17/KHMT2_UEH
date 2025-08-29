class Wordplay():
    def __init__(self):
        self.list_of_words = ['Apple', 'Ginger', 'Bigger', 'Price', 'Level', 'Madam', 'Racecar']

    def words_with_length(self, length):
        list = []
        self.length = int(length)
        for words in self.list_of_words:
            if len(words) == length:
                list.append(words)
            else:
                pass
        print(f"Tu co do dai bang {self.length}: {list}")

    def starts_with(self, s):
        self.s = s
        list = []
        for words in self.list_of_words:
            if words.startswith(s):
                list.append(words)
            else:
                pass
        print(f"Tu bat dau bang {s} la: {list}")

    def ends_with(self, s):
        t = s.lower()
        list = []
        for words in self.list_of_words:
            if words.endswith(t):
                list.append(words)
            else:
                pass
        print(f"Tu ket thuc bang {s} la: {list}")

    def palindrome(self):
        list = []
        for palin in self.list_of_words:
            palin = palin.lower()
            if palin == palin[::-1]:
                list.append(palin)
            else:
                pass
        print(f"Tu palindrome: {list}")

    def only(self, L):
        t = L.lower()
        list = []
        for letter in self.list_of_words:
            if t in letter.lower():
                list.append(letter)
            else:
                pass
        print(f"Nhung tu co chu {L} la: {list}")

    def avoids(self, L):
        t = L.lower()
        list = []
        for letter in self.list_of_words:
            if t not in letter.lower():
                list.append(letter)
            else:
                pass
        print(f"Nhung tu khong co chu {L} la: {list}")

wp1 = Wordplay()

wp1.words_with_length(5)
wp1.starts_with("G")
wp1.ends_with("R")
wp1.palindrome()
wp1.only("i")
wp1.avoids("a")
