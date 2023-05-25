import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def persist_input(
    query: str,
    isRightCall=lambda numeric_value: numeric_value != None,
):
    numeric_value = None

    while numeric_value == None:
        try:
            numeric_value = float(query)

            assert isRightCall(numeric_value)
        except:
            numeric_value = None

            query = input(
                "El valor introducido es inválido, por favor intentalo de nuevo y asegúrate de que sea un número mayor a 0: "
            )

    return numeric_value


def renderMatrix(matrix: list[list[float]]):
    for i in range(0, len(matrix)):
        print(matrix[i])
    print()


clear()

matrix: list[list[float]] = []
matrix_sqr_side = int(
    persist_input(
        input("Introduce el tamaño de la matriz: "),
        lambda numeric_value: numeric_value > 0,
    )
)
matrix_cols = matrix_sqr_side + 1

clear()

for diag_i in range(1, matrix_sqr_side + 1):
    matrix.append([])

    for eval_row in range(1, matrix_cols + 1):
        print(
            "Ahora, introduce los elementos de la matriz cuadrada, estos deberían corresponder a los coeficientes de las ecuaciones que tienes en tu sistema. Posteriormente, también se introducirá el resultado correspondiente a la fila actual.\n"
        )

        renderMatrix(matrix)

        if eval_row <= matrix_sqr_side:
            matrix[diag_i - 1].append(
                persist_input(
                    input(
                        f"Introduce el coeficiente [{diag_i}][{eval_row}] del sistema: "
                    ),
                )
            )
        else:
            matrix[diag_i - 1].append(
                persist_input(
                    input(
                        f"Introduce el resultado de la fila [{diag_i}] del sistema: "
                    ),
                )
            )
        clear()

for diag_i in range(0, matrix_sqr_side):
    diag_element = matrix[diag_i][diag_i]

    # Invertir las filas si algun elemento de la diagonal es 0
    if diag_element == 0:
        for eval_col in range(diag_i + 1, matrix_sqr_side):
            if matrix[diag_i][eval_col] != 0:
                diag_element = matrix[diag_i][eval_col]

                break

    if diag_element != 1:
        for col in range(0, matrix_cols):
            matrix[diag_i][col] = matrix[diag_i][col] / diag_element

    # Iteramos entre filas
    for eval_row in range(0, matrix_sqr_side):
        if eval_row != diag_i:
            row_factor = matrix[eval_row][diag_i]

            for eval_col in range(0, matrix_cols):
                substraction = row_factor * matrix[diag_i][eval_col]
                matrix[eval_row][eval_col] = (
                    matrix[eval_row][eval_col] - substraction
                )
