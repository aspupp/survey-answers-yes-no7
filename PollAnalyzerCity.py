import pandas as pd
class PollAnalyzerCity:
    def __init__(self, filename, question_columns):
        self.filename = filename
        self.question_columns = question_columns
        self.replace_dict = {"yes": 1, "no": 0}
        self.df = None
        self.by_city = None
    def load_and_convert(self):
        self.df = pd.read_csv(self.filename)
        for col in self.question_columns:
            self.df[col] = self.df[col].map(self.replace_dict)
    def group_by_city(self, chosen_question):
        if "city" not in self.df.columns:
            print("Колонки 'city' нет в файле")
            return
        self.by_city = (
            self.df.groupby("city")[chosen_question]
            .mean()
            .reset_index()
        )
        self.by_city.columns = ["city", f"share_yes_{chosen_question}"]
        print(f"Среднее 'yes' по городам вопрос: '{chosen_question}':")
        print(self.by_city)
    def save_by_city(self):
        if self.by_city is not None:
            self.by_city.to_csv("by_city.csv", index=False)
            print("\nФайл by_city.csv сохранён.")
