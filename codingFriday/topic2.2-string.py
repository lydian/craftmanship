#http://www.careercup.com/question?id=11903075

# input number of row, string

def convert(str, row):
    rows = ["" for i in range(row)]
    current_row = 0
    current_direction = 1
    for c in str:
        rows[current_row] += c
        current_row += current_direction
        if current_row == row -1 or current_row == 0:
            current_direction *= -1
    print rows

convert("PAYPALISHIRING", 3)
convert("PAYPALISHIRING", 4)
convert("PAYPALISHIRING", 5)
