import pandas as pd


class StatsController:
    def __init__(self, df) -> None:
        self.df = df

    def user_chat_ratio(self, recent_n=None):
        df = self.df.copy()
        if recent_n:
            df = df.tail(recent_n)
        ucr_df = (df.groupby("User").size() / len(df)).to_frame("ratio")
        return ucr_df

    def user_len_ratio(self, recent_n=None):
        df = self.df.copy()
        if recent_n:
            df = df.tail(recent_n)
        len_df = pd.concat([df["User"], df["Message"].apply(len)], axis=1)
        ulr_df = (
            len_df.groupby("User")["Message"].sum() / len_df["Message"].sum()
        ).to_frame("ratio")
        return ulr_df

    def user_arg_ratio(self, arg, recent_n=None):
        df = self.df
        if recent_n:
            df = df.tail(recent_n)
        filtered_df = df[df["Message"].str.contains(arg)]
        ratio_series = (
            filtered_df.groupby("User").size() / df.groupby("User").size()
        ).dropna()
        ratio_df = ratio_series.to_frame(name="ratio")
        return ratio_df
