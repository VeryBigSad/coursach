def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Вычисляет расстояние Левенштейна между двумя строками s1 и s2.
    Использует полную матрицу.
    Временная сложность: O(m*n)
    Пространственная сложность: O(m*n)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Удаление
                dp[i][j - 1] + 1,  # Вставка
                dp[i - 1][j - 1] + cost,
            )  # Замена

    return dp[m][n]


def levenshtein_distance_optimized(s1: str, s2: str) -> int:
    """
    Вычисляет расстояние Левенштейна между двумя строками s1 и s2.
    Использует оптимизацию по памяти.
    Временная сложность: O(m*n)
    Пространственная сложность: O(min(m, n))
    """
    m, n = len(s1), len(s2)

    # Для экономии памяти внешний цикл должен быть по более короткой строке
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m

    previous_row = list(range(n + 1))

    for i in range(m):
        current_row = [i + 1] + [0] * n
        for j in range(n):
            cost = 0 if s1[i] == s2[j] else 1
            current_row[j + 1] = min(
                previous_row[j + 1] + 1, current_row[j] + 1, previous_row[j] + cost
            )
        previous_row = current_row

    return previous_row[n]
