import pandas as pd
import json
from fastapi import FastAPI, UploadFile, File
import uvicorn
import io
class PollAnalyzerAPI:
    def __init__(self, question_columns):
        self.question_columns = question_columns
        self.replace_dict = {"yes": 1, "no": 0}
        self.app = FastAPI()
        @self.app.post("/analyze")
        async def analyze(file: UploadFile = File(...)):
            contents = await file.read()
            df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
            for col in self.question_columns:
                if col in df.columns:
                    df[col] = df[col].map(self.replace_dict)
            shares_dict = {}
            for col in self.question_columns:
                if col in df.columns:
                    shares_dict[col] = round(df[col].mean(), 2)
            response = {"shares_yes": shares_dict}
            if "city" in df.columns:
                by_city_df = (
                    df.groupby("city")[self.question_columns]
                    .mean()
                    .round(2)
                    .reset_index()
                )
                response["by_city"] = by_city_df.to_dict(orient="records")
            return response
    def run(self):
        uvicorn.run(self.app, host="127.0.0.1", port=8000)