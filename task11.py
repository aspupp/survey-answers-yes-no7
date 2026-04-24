import pandas as pd
from task9 import PollAnalyzer


class PollAnalyzerDataFrame(PollAnalyzer):
    """Наследник PollAnalyzer. Работает с pandas DataFrame."""

    def __init__(self, filename, question_columns):
        super().__init__(filename, question_columns[0])
        self.question_columns = question_columns
        self.df = None

    def load_and_convert(self):
        """Читаем CSV и заменяем yes/no на 0/1 во всех колонках"""
        self.df = pd.read_csv(self.filename)
        for col in self.question_columns:
            self.df[col] = self.df[col].map(self.replace_dict)

    def show_dataframe(self):
        """Показываем таблицу"""
        print("Класс: PollAnalyzerDataFrame (наследник PollAnalyzer)")
        print("\nТаблица после замены yes/no на 0/1:")
        print(self.df)

    def show_describe(self):
        print("\nСтатистика describe() по вопросам:")
        print(self.df[self.question_columns].describe())
        print("\nДоля 'yes' (строка mean):")
        print(self.df[self.question_columns].mean().round(2))
columns = ["q1_like_python", "q2_do_sport", "q3_have_pet", "q4_drink_coffee"]
poll = PollAnalyzerDataFrame("poll.csv", columns)
poll.load_and_convert()
poll.show_dataframe()
poll.show_describe()