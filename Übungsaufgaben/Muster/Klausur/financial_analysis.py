from typing import List, Dict, Tuple


def read_file(path: str) -> List[Dict[str, str]]:
    return [
        {key: value for key, value in zip(["date", "open", "high", "low", "close", "adj close", "volume"],
                                          line.strip().split(","))} for index, line in enumerate(open(path)) if index > 0
    ]


def analyze_open_stats(content: List[Dict[str, str]]) -> Tuple[float, float, float]:
    open_prices = [float(line["open"]) for line in content]
    min_price = round(min(open_prices), 2)
    max_price = round(max(open_prices), 2)
    avg_price = round(sum(open_prices) / len(open_prices), 2)

    return min_price, max_price, avg_price


def greatest_gap(content: List[Dict[str, str]]) -> str:
    prices: List[Tuple[float, float, str]] = list(zip([float(line["high"]) for line in content],
                                                      [float(line["low"]) for line in content],
                                                      [line["date"] for line in content]))
    return max(prices, key=lambda x: abs(x[0] - x[1]))[2]


def sum_profitable_days(content: List[Dict[str, str]]) -> int:
    return sum(1 for line in content if float(line["open"]) < float(line["close"]))
