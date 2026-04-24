import csv
class PollAnalyzerMulti:
    def __init__(self, filename, question_columns):
        self.filename = filename
        self.question_columns = question_columns
        self.replace_dict = {"yes": 1, "no": 0}
        self.all_rows = []
        self.shares = []
    def load_all(self):
        with open(self.filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.all_rows.append(row)
    def calculate_shares(self):
        self.shares = []
        for col in self.question_columns:
            values = []
            for row in self.all_rows:
                number = self.replace_dict[row[col]]
                values.append(number)
            share = sum(values) / len(values)
            self.shares.append(share)
    def show_result(self):
        print("Доля 'yes' по каждому вопросу:")
        for col, share in zip(self.question_columns, self.shares):
            print(f"  {col}: {share:.2f}  ({share * 100:.1f}%)")
        print()
        print("Список всех долей:", self.shares)