import string


class CaesarCipher:
    def __init__(self, message, key, mode):
        if message is None:
            self.message = message
        else:
            self.message = message.lower()
        self.key = key
        self.mode = mode
        self.symbols = string.ascii_lowercase

    def transform_message(self):
        translated = ''
        for symbol in self.message:
            if symbol in self.symbols:
                symbolIndex = self.symbols.find(symbol)

                if self.mode == "encrypt":
                    translatedIndex = symbolIndex + self.key
                elif self.mode == "decrypt":
                    translatedIndex = symbolIndex - self.key\

                if translatedIndex >= len(self.symbols):
                    translatedIndex = translatedIndex - len(self.symbols)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(self.symbols)

                translated = translated + self.symbols[translatedIndex]
            else:
                translated = translated + symbol

        return translated

    def transform_file(self, input_file, output_file):
        write_to_file = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                lines_for_file = []
                for word in line.split(" "):
                    self.message = word.strip().lower()
                    lines_for_file.append(self.transform_message())
                write_to_file.append(lines_for_file)
        with open(output_file, 'w') as f:
            for line in write_to_file:
                f.writelines(' '.join(line) + "\n")