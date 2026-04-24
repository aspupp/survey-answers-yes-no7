import pandas as pd
class PollAnalyzerDataFrame:
    def __init__(self, filename, question_columns):
        self.filename = filename
        self.question_columns = question_columns
        self.replace_dict = {"yes": 1, "no": 0}
        self.df = None
    def load_and_convert(self):
        self.df = pd.read_csv(self.filename)
        for col in self.question_columns:
            self.df[col] = self.df[col].map(self.replace_dict)
    def show_dataframe(self):
        print("Таблица после замены yes/no на 0/1:")
        print(self.df)
    def show_describe(self):
        print("\nСтатистика describe() по вопросам:")
        print(self.df[self.question_columns].describe())
        print("\nДоля 'yes' (строка mean):")
        print(self.df[self.question_columns].mean().round(2))