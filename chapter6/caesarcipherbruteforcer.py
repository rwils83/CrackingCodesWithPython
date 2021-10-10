from chapter5.ceaserCipher import CaesarCipher as cc


class BruteForcer:
    def __init__(self, message):
        self.message = message
        self.key = 0
        self.symbols = cc(None, 1, 'encrypt').symbols

    def brute_force(self):
        for key in range(len(self.symbols)+1):
            print(f'Results for Key {key}: {cc(self.message, key, "decrypt").transform_message()}')

