import csv
from task9 import PollAnalyzer
class PollAnalyzerMulti(PollAnalyzer):
    def __init__(self, filename, question_columns):
        super().__init__(filename, question_columns[0])
        self.question_columns = question_columns
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
        print("Класс: PollAnalyzerMulti (наследник PollAnalyzer)")
        print("Доля 'yes' по каждому вопросу:")
        for col, share in zip(self.question_columns, self.shares):
            print(f"  {col}: {share:.2f}  ({share * 100:.1f}%)")
        print()
        print("Список всех долей:", self.shares)
columns = ["q1_like_python", "q2_do_sport", "q3_have_pet", "q4_drink_coffee"]
poll = PollAnalyzerMulti("poll.csv", columns)
poll.load_all()
poll.calculate_shares()
poll.show_result()