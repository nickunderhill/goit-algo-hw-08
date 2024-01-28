import heapq


def min_cost(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        print(f'Кабелі в наявності: {cable_lengths}')

        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        print(f'Обʼєднуємо два найкоротші кабелі {first} і {second}')
        cost = first + second
        total_cost += cost

        print(f'Кладемо кабель довжиною {cost} в купу')
        heapq.heappush(cable_lengths, cost)

    return total_cost


def main():
    cable_lengths = [5, 10, 2, 8, 4, 7]
    print("Мінімальні витрати:", min_cost(cable_lengths))


if __name__ == "__main__":
    main()
