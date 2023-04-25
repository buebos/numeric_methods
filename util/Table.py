class Table:
    all: list[list] = []

    def get_column(self, index):
        column = []
        for i in range(len(self.all)):
            column.append(self.all[i][index])

        return column

    def ad_row(self, row: list):
        self.all.append(row)
