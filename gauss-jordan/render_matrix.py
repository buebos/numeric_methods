def render_matrix(
    matrix: list[list[float | int]], cols: int, rows: int
) -> str:
    rendered = ""

    for i in range(rows):
        if i > len(matrix):
            matrix.append([])
        for j in range(cols):
            if j > len(matrix):
                matrix[i].append(0)

    return ""
