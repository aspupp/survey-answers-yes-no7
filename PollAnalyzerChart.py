import pandas as pd
import matplotlib.pyplot as plt
class PollAnalyzerChart:
    def __init__(self, filename, question_columns):
        self.filename = filename
        self.question_columns = question_columns
        self.replace_dict = {"yes": 1, "no": 0}
        self.df = None
    def load_and_convert(self):
        self.df = pd.read_csv(self.filename)
        for col in self.question_columns:
            self.df[col] = self.df[col].map(self.replace_dict)
    def draw_bar_chart(self, output_file="chart.png"):
        shares = [self.df[col].mean() for col in self.question_columns]
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(self.question_columns, shares, color="steelblue", width=0.5)

        for bar, share in zip(bars, shares):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.02,
                f"{share:.0%}",
                ha="center",
                va="bottom",
                fontsize=11
            )
        ax.set_title("Доля ответов 'yes' по каждому вопросу", fontsize=13)
        ax.set_xlabel("Вопросы")
        ax.set_ylabel("Доля 'yes'")
        ax.set_ylim(0, 1.15)
        ax.tick_params(axis="x", rotation=15)
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        print(f"График сохранён: {output_file}")