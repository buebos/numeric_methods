Matrix = list[list[float]]


def clear():
    print("\033[H\033[J", end="")
    print(
        """
ooo        ooooo               .             o8o                   oooooooooooo oooo                     oooo        
`88.       .888'             .o8             `"'                   `888'     `8 `888                     `888        
 888b     d'888   .oooo.   .o888oo oooo d8b oooo  oooo    ooo       888          888   .oooo.    .oooo.o  888  oooo  
 8 Y88. .P  888  `P  )88b    888   `888""8P `888   `88b..8P'        888oooo8     888  `P  )88b  d88(  "8  888 .8P'   
 8  `888'   888   .oP"888    888    888      888     Y888'          888    "     888   .oP"888  `"Y88b.   888888.    
 8    Y     888  d8(  888    888 .  888      888   .o8"'88b         888          888  d8(  888  o.  )88b  888 `88b.  
o8o        o888o `Y888""8o   "888" d888b    o888o o88'   888o      o888o        o888o `Y888""8o 8""888P' o888o o888o 
                                                                                                                     
                                                                                                                   
          """
    )


def transpose(
    input_arr: list[list],
):
    output_arr: list[list] = []

    for i in range(len(input_arr)):
        for j in range(len(input_arr[i])):
            if len(output_arr) <= j:
                output_arr.append([])

            output_arr[j].append(input_arr[i][j])
    return output_arr


def tabulate(headers: list[str], data: list[list]):
    column_width = 10
    data = transpose(data)
    table_res = (
        "_" * (((len(data[0]) + 1) * (column_width)) - 1) + "_" + "\n"
    )

    for i in range(len(data)):
        table_res += "\n"
        header = headers[i]

        table_res += (
            header[0:column_width]
            + " " * (column_width - len(header))
            + "|"
        )

        for j in range(len(data[i])):
            cell_data = str(data[i][j])[0:9]
            table_res += (
                cell_data + " " * (column_width - len(cell_data) - 1) + "|"
            )

        table_res += (
            "\n" + "_" * ((len(data[i]) + 1) * column_width) + "|" + "\n"
        )

    return table_res


def copy_matrix(matrix: Matrix):
    return [row[:] for row in matrix]


def trunc_if_near(x: float, thresh: float = 0.999999):
    floating = abs(x - int(x))
    diff_to_int = 1 - floating

    if floating > thresh:
        return x + diff_to_int if x > 0 else x + floating - 1
    elif floating < 1 - thresh:
        return x - floating if x > 0 else x + floating

    return x


def persist_input(
    prompt: str,
    isRightCall=lambda numeric_value: not not numeric_value
    or numeric_value == 0,
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


def render_capture_matrix():
    matrix: Matrix = []

    clear()

    system_size = int(
        persist_input(
            "Introduce el tamaño de la matriz: ",
            lambda numeric_value: numeric_value > 0,
        )
    )
    matrix_cols = system_size + 1

    clear()

    for diag_i in range(system_size):
        matrix.append([])

        for row in range(matrix_cols):
            print(
                "Ahora, introduce los elementos de la matriz cuadrada, estos deberían corresponder a los coeficientes de las ecuaciones que tienes en tu sistema. Posteriormente, también se introducirá el resultado correspondiente a la fila actual.\n"
            )

            render_matrix(matrix)

            if row <= system_size:
                matrix[diag_i].append(
                    persist_input(
                        f"Introduce el coeficiente [{diag_i + 1}][{row + 1}] del sistema: "
                    )
                )
            else:
                matrix[diag_i].append(
                    persist_input(
                        f"Introduce el resultado de la fila [{diag_i + 1}] del sistema (este valor es parte de la extensión): "
                    )
                )
            clear()

    return matrix


def render_matrix(matrix: Matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])
    print()


def gauss_jordan(original_matrix: Matrix):
    matrix = copy_matrix(original_matrix)
    matrix_rows = len(original_matrix)
    matrix_cols = matrix_rows + 1

    for diag_i in range(matrix_rows):
        diag_element = matrix[diag_i][diag_i]

        # Invertir las filas si algun elemento de la diagonal es 0
        if diag_element == 0:
            for eval_row in range(diag_i + 1, matrix_rows):
                if matrix[eval_row][diag_i] != 0:
                    matrix[diag_i], matrix[eval_row] = (
                        matrix[eval_row],
                        matrix[diag_i],
                    )
                    diag_element = matrix[diag_i][diag_i]
                    break
            if diag_element == 0:
                continue

        if diag_element != 1:
            for col in range(0, matrix_cols):
                matrix[diag_i][col] = matrix[diag_i][col] / diag_element

        # Iteramos entre filas
        for eval_row in range(0, matrix_rows):
            if eval_row != diag_i:
                row_factor = matrix[eval_row][diag_i]

                for eval_col in range(0, matrix_cols):
                    substraction = row_factor * matrix[diag_i][eval_col]
                    matrix[eval_row][eval_col] = (
                        matrix[eval_row][eval_col] - substraction
                    )

    for i in range(matrix_rows):
        matrix[i][-1] = trunc_if_near(matrix[i][-1])

    return matrix


def evaluate_gauss_jordan(matrix: Matrix):
    system_size = len(matrix)
    extension_col = system_size
    results: list[float] = []

    for row in range(system_size):
        row_vars = 0

        for j in range(system_size):
            if matrix[row][j] != 0:
                row_vars += 1

        if row_vars == 1:
            results.append(trunc_if_near(matrix[row][extension_col]))
        elif row_vars == 0 and matrix[row][extension_col] == 0:
            return "arbitrary"
        elif row_vars == 0 and matrix[row][extension_col] != 0:
            return "inconsistent"

    return results


def solve_arbitrary(result_matrix: Matrix):
    results: list[float] = []
    system_size = len(result_matrix)
    arbitrary_val = persist_input(
        f"El sistema es arbitrario en función de una variable, introduce un valor para definir todas las demás variables del sistema: "
    )
    for row in range(system_size):
        vars_in_row = 0
        for col in range(system_size):
            if result_matrix[row][col] != 0:
                vars_in_row += 1
        if not vars_in_row:
            results.append(arbitrary_val)
        else:
            results.append(
                result_matrix[row][-1]
                - arbitrary_val * result_matrix[row][-2]
            )

    return results


def check_matrix_results(original_matrix: Matrix, results: list[float]):
    system_size = len(original_matrix)
    evaluations: Matrix = []

    for row in range(system_size):
        result = 0
        original_result = original_matrix[row][-1]

        for col in range(system_size):
            result += original_matrix[row][col] * results[col]

        evaluations.append([trunc_if_near(result), original_result])

    return evaluations


def main(render_result_check: bool = True, use_example: bool = False):
    if not use_example:
        original_matrix = render_capture_matrix()
    else:
        clear()
        original_matrix = [
            [
                4.0,
                6.0,
                9.0,
                1.0,
                -4.0,
                23.0,
                12.0,
                -32.0,
                -21.0,
                44.0,
                98.0,
            ],
            [-3.0, 4.0, 6.0, 9.0, 3.0, 98.0, 1.0, 23.0, -5.0, -6.0, 66.0],
            [
                2.0,
                3.0,
                -3.0,
                -4.0,
                2.0,
                -22.0,
                33.0,
                55.0,
                -4.0,
                4.0,
                -22.0,
            ],
            [3.0, 3.0, -3.0, 4.0, 1.0, 5.0, 22.0, 44.0, -7.0, 5.0, -33.0],
            [
                6.0,
                4.0,
                2.0,
                1.0,
                22.0,
                44.0,
                55.0,
                33.0,
                -99.0,
                6.0,
                -33.0,
            ],
            [12.0, 2.0, 5.0, 6.0, 1.0, 1.0, 77.0, 2.0, -33.0, -8.0, -44.0],
            [4.0, 3.0, 2.0, 5.0, 2.0, 56.0, 8.0, 3.0, -1.0, 9.0, -99.0],
            [
                4.0,
                -5.0,
                -5.0,
                4.0,
                3.0,
                76.0,
                9.0,
                -6.0,
                -7.0,
                -21.0,
                100.0,
            ],
            [6.0, -7.0, -9.0, 2.0, 5.0, 33.0, 10.0, 0.0, 2.0, -2.0, 8.0],
            [4.0, 10.0, 5.0, 1.0, 6.0, 22.0, 11.0, 1.0, 3.0, -2, 9],
        ]
    header_results = ["# Variable", "Valor"]
    result_matrix = gauss_jordan(original_matrix)
    results = evaluate_gauss_jordan(result_matrix)

    if results == "arbitrary":
        results = solve_arbitrary(result_matrix)
        print(
            tabulate(
                header_results,
                [[i + 1, results[i]] for i in range(len(results))],
            )
        )
    elif results == "inconsistent":
        print(
            "Las ecuaciones son incosistentes, por lo tanto una solucion no pudo ser encontrada"
        )
    else:
        print(
            tabulate(
                header_results,
                [[i + 1, results[i]] for i in range(len(results))],
            )
        )

    if not isinstance(results, str) and render_result_check:
        print(
            "\nAl realizar las ecuaciones, se obtuvieron los siguientes resultados para cada fila, contra el resultado que se proporcionaba en la matriz original:"
        )
        print(
            tabulate(
                ["Resultado", "Original"],
                check_matrix_results(original_matrix, results),
            )
        )


main(render_result_check=True, use_example=False)
