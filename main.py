# 初期のカード状態のリスト（False: 裏）
cards = [False] * 100


def main():
    # 2~100までで、各数字ごとにひっくり返すカード番号のリストを格納する
    numbers_to_turn_over_lists = []
    # 2~100までで、各数字ごとにひっくり返すカード番号のリストを作成
    for i in range(2, 101):
        numbers = [j for j in range(i, 101, i)]
        numbers_to_turn_over_lists.append(numbers)

    # 上記で作成したひっくり返す番号リスト（-1でcardsのインデックス）で、現状を反転させる
    for numbers_to_turn_over in numbers_to_turn_over_lists:
        for i in numbers_to_turn_over:
            # 現在のcards状態を反転させる
            cards[i-1] = not cards[i-1]

    # 最終的なcardsの状態からFalse（裏）だけのインデックスを取得（+1してカード番号）
    r = [i+1 for i, v in enumerate(cards) if not v]
    print(r)


if __name__ == "__main__":
    main()
