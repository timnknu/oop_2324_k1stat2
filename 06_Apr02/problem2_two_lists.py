

if __name__ == "__main__":
    thelog = MyClass(
        ['e4 d6', 'Nc3 e5', 'Bc4 Be7'],
        ['d4 Nf6', 'Nf3 Nbd7', '0–0 c6']
    )

    for mov in thelog:
        print(mov)
# Очікуваний результат:
# e4 d6
# d4 Nf6
# Nc3 e5
# Nf3 Nbd7
# Bc4 Be7
# 0–0 c6