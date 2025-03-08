class RaiFenceCipher:
    def __init__(self):
        pass
    def rail_fence_encrypt(self, plain_text, num_rails):
        rails =[[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == -1:
                direction = -1
    