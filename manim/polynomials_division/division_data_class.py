class DivisionData:
    def __init__(self, dividend: list[str], divisor: list[str], steps: list['DivisionStep']):
        self.dividend = dividend
        self.divisor = divisor
        self.steps = steps


class DivisionStep:
    def __init__(
            self,
            result,
            products: list[str],
            dividends: list[str],
            is_last: bool = False
    ):
        self.result = result
        self.products = products
        self.dividends = dividends
        self.is_last = is_last
