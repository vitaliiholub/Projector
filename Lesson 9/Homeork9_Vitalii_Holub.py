def cats_in_hats(rounds: int, cats_amount: int) -> list:
    cats = [0 for _ in range(cats_amount)]  # 0 mean cat without hat, 1 mean cat in hat

    for step in range(1, rounds + 1):  # every round adding 1 to step
        for j in range(step - 1, cats_amount, step):
            cats[j] = 0 if cats[j] else 1  # if cat in hat - take it off, if cat without hat - put it on

    return [i + 1 for i in range(cats_amount) if cats[i]]  # return list numbers of cats with hats
