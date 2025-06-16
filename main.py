from levenstein import levenshtein_distance, levenshtein_distance_optimized


def run_examples():
    print("--- Демонстрация работы алгоритма расстояния Левенштейна ---")

    # Пример 1: Простая опечатка
    word1, word2 = "алгоритм", "алгаритм"
    dist1 = levenshtein_distance(word1, word2)
    dist2 = levenshtein_distance_optimized(word1, word2)
    assert dist1 == dist2
    print(f"\nСравнение '{word1}' и '{word2}': {dist1}")

    # Пример 2: из курсовой работы
    word3, word4 = "молоко", "колокол"
    dist3 = levenshtein_distance(word3, word4)
    dist4 = levenshtein_distance_optimized(word3, word4)
    assert dist3 == dist4
    print(f"\nСравнение '{word3}' и '{word4}': {dist3}")

    # Пример 3: Разные длины строк
    word5, word6 = "sunday", "saturday"
    dist5 = levenshtein_distance(word5, word6)
    dist6 = levenshtein_distance_optimized(word5, word6)
    assert dist5 == dist6
    print(f"\nСравнение '{word5}' и '{word6}': {dist5}")


if __name__ == "__main__":
    run_examples()
