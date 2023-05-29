import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def roundIfNear(x: float, thresh=0.999999):
    if x - int(x) > thresh:
        return int(x) + 1
    elif x - int(x) < 1 - thresh:
        return int(x)

    return x


def persist_input(
    prompt: str,
    isRightCall=lambda numeric_value: numeric_value != None,
):
    numeric_value = None

    while numeric_value == None:
        try:
            numeric_value = float(input(prompt))

            assert isRightCall(numeric_value)
        except:
            numeric_value = None

            prompt = input(
                "El valor introducido es inválido, por favor intentalo de nuevo y asegúrate de que sea un número mayor a 0: "
            )

    return numeric_value


def unpermutate_matrix(incoming_matrix: list[list[float]], permutations: list[list[int]]):
    matrix = incoming_matrix.copy()

    if len(permutations):
        for permutation in permutations:
            from_row = permutation[0]
            to_row = permutation[1]

            for row in range(matrix_sqr_side):
                if row == from_row:
                    matrix[from_row], matrix[to_row] = (
                        matrix[to_row],
                        matrix[from_row],
                    )
    return matrix


def render_matrix(matrix: list[list[float]]):
    for i in range(0, len(matrix)):
        print(matrix[i])
    print()


clear()

matrix: list[list[float]] = []
matrix_sqr_side = int(
    persist_input(
        "Introduce el tamaño de la matriz: ",
        lambda numeric_value: numeric_value > 0,
    )
)
matrix_cols = matrix_sqr_side + 1
permutations: list[list[int]] = []
is_inconsistent = False
is_arbitrary = False

example_matrix = [
    [0, 4, -8, 24],
    [3, -3, 9, -15],
    [2, 4, -6, 26],
]

clear()

for diag_i in range(1, matrix_sqr_side + 1):
    matrix.append([])

    for eval_row in range(1, matrix_cols + 1):
        print(
            "Ahora, introduce los elementos de la matriz cuadrada, estos deberían corresponder a los coeficientes de las ecuaciones que tienes en tu sistema. Posteriormente, también se introducirá el resultado correspondiente a la fila actual.\n"
        )

        render_matrix(matrix)

        if eval_row <= matrix_sqr_side:
            matrix[diag_i - 1].append(persist_input(f"Introduce el coeficiente [{diag_i}][{eval_row}] del sistema: "))
        else:
            matrix[diag_i - 1].append(
                persist_input(
                    f"Introduce el resultado de la fila [{diag_i}] del sistema (este valor es parte de la extensión): "
                )
            )
        clear()


for diag_i in range(0, matrix_sqr_side):
    diag_element = matrix[diag_i][diag_i]

    # Invertir las filas si algun elemento de la diagonal es 0
    if diag_element == 0:
        for eval_row in range(diag_i + 1, matrix_sqr_side):
            if matrix[eval_row][diag_i] != 0:
                matrix[diag_i], matrix[eval_row] = (
                    matrix[eval_row],
                    matrix[diag_i],
                )
                diag_element = matrix[diag_i][diag_i]
                permutations.append([diag_i, eval_row])
                break
        if diag_element == 0:
            continue

    if diag_element != 1:
        for col in range(0, matrix_cols):
            matrix[diag_i][col] = matrix[diag_i][col] / diag_element

    # Iteramos entre filas
    for eval_row in range(0, matrix_sqr_side):
        if eval_row != diag_i:
            row_factor = matrix[eval_row][diag_i]

            for eval_col in range(0, matrix_cols):
                substraction = row_factor * matrix[diag_i][eval_col]
                matrix[eval_row][eval_col] = matrix[eval_row][eval_col] - substraction

unpermutated_matrix_solved = unpermutate_matrix(matrix, permutations)
results: list[list[float]] = []

for row in range(matrix_sqr_side):
    vars_found = 0
    var_index = 0

    matrix[row][matrix_cols - 1] = roundIfNear(matrix[row][matrix_cols - 1])
    unpermutated_matrix_solved[row][matrix_cols - 1] = roundIfNear(unpermutated_matrix_solved[row][matrix_cols - 1])

    for j in range(matrix_sqr_side):
        if matrix[row][j] != 0:
            vars_found += 1
            var_index = j

    if vars_found == 1:
        results.append([row, matrix[row][matrix_cols - 1]])
    elif vars_found == 0 and matrix[row][matrix_cols - 1] == 0:
        is_arbitrary = True
    elif vars_found == 0 and matrix[row][matrix_cols - 1] != 0:
        is_inconsistent = True

if len(permutations):
    print("Sistema permutado:")
    render_matrix(matrix)
print("Sistema resulto:")
render_matrix(unpermutated_matrix_solved)

if is_arbitrary:
    fns = []
    arbitrary_index = None

    for col in range(matrix_cols - 1):
        repeated = 0

        for row in range(matrix_sqr_side):
            if unpermutated_matrix_solved[row][col] != 0:
                repeated += 1

        if repeated == matrix_sqr_side - 1:
            arbitrary_index = col

    for j in range(matrix_sqr_side):
        if j == arbitrary_index:
            fns.append(lambda arbitrary_val: arbitrary_val)
            continue

        fns.append(lambda arbitrary_val: matrix[j][-1] - arbitrary_val * matrix[j][-2])

    arbitrary_val = persist_input(
        f"El sistema es arbitrario en función de la variable número {arbitrary_index}, introduce un valor para definir todas las demás variables del sistema: "
    )

    for j in range(len(fns)):
        fn = fns[j]
        results.append([j, fn(arbitrary_val)])
        print(f"El valor de la variable {j + 1}:", results[j][1])
elif is_inconsistent:
    print("Las ecuaciones son incosistentes, por lo tanto una solucion no pudo ser encontrada")
else:
    for result in results:
        print(f"El valor de la variable {result[0] + 1}:", result[1])
