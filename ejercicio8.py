import random

def print_char_matrix(matrix):
    for row in matrix:
        print("\t".join(row))
    print()

def fill_in_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = chr(random.randint(65, 91))  # Random uppercase letter

def search_word(matrix, word):
    word_char = list(word)
    counter_words_found = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            first_letter = matrix[row][col]
            if word_char[0] == first_letter:

                if len(word_char) > 1:
                    directions = [
                        (-1, -1),  # Up-left
                        (-1, 0),   # Up
                        (-1, 1),   # Up-right
                        (0, 1),    # Right
                        (1, 1),    # Down-right
                        (1, 0),    # Down
                        (1, -1),   # Down-left
                        (0, -1)    # Left
                    ]
                    for dr, dc in directions:
                        found = False
                        r, c = row, col
                        for i in range(len(word_char)):
                            if not (0 <= r < len(matrix) and 0 <= c < len(matrix[r])) or word_char[i] != matrix[r][c]:
                                found = False
                                break
                            r += dr
                            c += dc
                            found = True

                        if found:
                            print(f"Encontrado en ({row},{col}) hacia {'arriba izquierda' if (dr, dc) == (-1, -1) else 'arriba' if (dr, dc) == (-1, 0) else 'derecha' if (dr, dc) == (0, 1) else 'abajo derecha' if (dr, dc) == (1, 1) else 'abajo' if (dr, dc) == (1, 0) else 'abajo izquierda' if (dr, dc) == (1, -1) else 'izquierda'}.")
                            counter_words_found += 1

                else:
                    print(f"Encontrado en ({row},{col}).")
                    counter_words_found += 1

    print(f"La palabra {word} se ha encontrado {counter_words_found} veces.")

def main():
    rows = int(input("Ingrese el numero de filas: "))
    cols = int(input("Ingrese el numero de columnas: "))
    print()

    matrix = [[''] * cols for _ in range(rows)]

    fill_in_matrix(matrix)

    print_char_matrix(matrix)

    word = input("Ingrese la palabra a buscar: ").upper()

    search_word(matrix, word)

if __name__ == "__main__":
    main()
