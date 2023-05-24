import os

OPERATION_SYMBOLS = ["-", "+"]


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


def parse_matrix(equation: str):
    literals: list[str] = []
    lastIsLiteral = False
    awaitingSymbol = None
    coeficients: list[str] = []

    for char in equation:
        if (
            not char.isdigit() and char != symbol
            for symbol in OPERATION_SYMBOLS
        ):
            literals.append(char)
            lastIsLiteral = True

        if (char == symbol for symbol in OPERATION_SYMBOLS):
            awaitingSymbol = char

        if char.isdigit() and awaitingSymbol:
            coeficients.append(awaitingSymbol + char)


clear()

matrix: list[list[float]] = []
matrix_side = int(
    persist_input(
        input("Introduce el tamaño de la matriz: "),
        lambda numeric_value: numeric_value > 0,
    )
)
det = 1

clear()

for i in range(1, matrix_side + 1):
    matrix.append([])

    for j in range(1, matrix_side + 1):
        matrix[i - 1].append(
            persist_input(
                input(f"Introduce el índice [{i}][{j}] de la matriz: "),
            )
        )
        renderMatrix(matrix)

        clear()


original_matrix = matrix.copy()

# Desde la primera fila hasta n - 1 filas, debido a que la última
# ya no tiene elementos debajo para convertir a 0
for i in range(0, matrix_side):
    current_diag = matrix[i][i]

    # Invertir las filas si algun elemento de la diagonal es 0
    if current_diag == 0:
        for j in range(i + 1, matrix_side):
            if matrix[j][i] != 0:
                matrix[i], matrix[j] = (
                    matrix[j],
                    matrix[i],
                )
                det = -det

                break
        current_diag = matrix[i][i]

        if current_diag == 0:
            break

    det *= current_diag

    if i >= matrix_side - 1:
        break

    # Iteramos entre filas
    for j in range(i + 1, matrix_side):
        current_substract = matrix[j][i]
        for k in range(i, matrix_side):
            substraction = current_substract * matrix[i][k] / current_diag
            matrix[j][k] = matrix[j][k] - substraction


renderMatrix(original_matrix)
renderMatrix(matrix)

print("Determinante:", det)
#%%