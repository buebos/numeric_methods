class Map:
    everything = []
    length = len(everything)

    def set(self, key, value):
        self.everything.append([key, value])
        self.length = len(self.everything)

    def get(self, key):
        if len(self.everything) == 0:
            return None

        for i in range(len(self.everything)):
            if self.everything[i][0] == key:
                return self.everything[i][1]

        return None