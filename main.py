scenario = (50000, 1600, 1.10, 480)


def calculate_investment(init, input, annual_fee, period):
    tax = ((annual_fee) ** (1/12))

    inputs = [(init, period)]

    growth = 1.00

    for i in range(1, period):
        inputs.append(((input * growth), period - i))
        if (i + 1) % 12 == 0:
            growth *= 1  # 1.05

    result = 0
    total_input = 0

    for value, months in inputs:
        total_input += value
        investment = value * (tax ** months)
        result += investment
        print(f'{value} -> {investment} ({((investment/value) * 100) - 100})')

    return (total_input, result - ((result - total_input) * .15))


print(calculate_investment(*scenario))
