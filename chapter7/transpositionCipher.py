class TranspostionCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def transform(self):
        ciphertext = [''] * self.key

        for column in range(self.key):
            currentIndex = column

            while currentIndex < len(self.message):
                ciphertext[column] += self.message[currentIndex]
                currentIndex += self.key

        return ''.join(ciphertext)

    def decrypt(self):
        return "Chapter 8 work"
