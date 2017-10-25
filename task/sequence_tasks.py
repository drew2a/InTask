def create_3_5_10_array(n):
    five_div_flag = 0
    recalculate_flag = 0
    result_digit = 0
    digits = [0]
    for i in range(int(n / 3)):
        five_div_flag += 1
        result_digit += 3
        recalculate_flag += 1

        if five_div_flag == 5:
            five_div_flag = 0
            digits[0] += 3
            continue

        if recalculate_flag > 3:
            recalculate_flag = 1
            digits = list(extract_digits(result_digit))
        else:
            digits[0] += 3

        digits_sum = sum(digits)
        if digits_sum < 10:
            yield result_digit