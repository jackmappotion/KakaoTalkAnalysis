import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:
    class RatioVisualizer:
        def __init__(self, ratio_series) -> None:
            self.ratio_series = ratio_series

        @staticmethod
        def _format_top_n(ratio_series, top_n):
            top_n_series = ratio_series.nlargest(top_n)
            top_n_series = pd.concat(
                [top_n_series, pd.Series({"etc": 1 - top_n_series.sum()})]
            )
            return top_n_series

        def draw_pieplot(self, top_n=None):
            ratio_series = self.ratio_series.copy()
            if top_n:
                ratio_series = self._format_top_n(ratio_series, top_n)
            plt.pie(
                x=ratio_series.values,
                labels=ratio_series.index,
                autopct="%.1f%%",
                colors=sns.color_palette("Set2"),
            )
            plt.tight_layout()
            plt.show()
            return None
