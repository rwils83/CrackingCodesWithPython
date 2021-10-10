class ReverseCipher:
    def __init__(self, message):
        self.message = message

    def transform_message(self):
        i = len(self.message) - 1
        translated = ''
        while i >= 0:
            translated = translated + self.message[i]
            i = i -1

        return translated

    def transform_file(self, input_file,output_file):
        write_to_file = []
        with open(input_file, 'r')as f:
            for line in f.readlines():
                lines_for_file = []
                for word in line.split(" "):
                    self.message = word.strip()
                    lines_for_file.append(self.transform_message())
                write_to_file.append(lines_for_file)
        with open(output_file, 'w') as f:
            for line in write_to_file:
                f.writelines(' '.join(line) + "\n")



