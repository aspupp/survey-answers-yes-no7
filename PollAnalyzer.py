import csv
class PollAnalyzer:
    def __init__(self, filename, column_name):
        self.filename = filename
        self.column_name = column_name
        self.replace_dict = {"yes": 1, "no": 0}
        self.values = []
    def load_column(self):
        with open(self.filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                text = row[self.column_name]
                number = self.replace_dict[text]
                self.values.append(number)
    def get_share(self):
        if len(self.values) == 0:
            return 0
        return sum(self.values) / len(self.values)
    def show_result(self):
        share = self.get_share()
        print(f"Колонка: {self.column_name}")
        print(f"Значения после замены: {self.values}")
        print(f"Всего ответов: {len(self.values)}")
        print(f"Количество 'yes': {sum(self.values)}")
        print(f"Доля 'yes': {share:.2f}  то есть {share * 100:.1f}%")