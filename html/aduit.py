def convert(num):
    base = [81, 27, 9, 3, 1]

    result = []
    zero_number = 0
    two_number = 0
    for b in base:
        a = num / b
        num = num % b
        result.append(int(a))
        if int(a) == 0:
            zero_number = zero_number + 1

        if int(a) == 2:
            two_number = two_number + 1

    audit_result = "\t".join(map(lambda x: str(x), result))
    if zero_number >= 3:
        audit_result = audit_result + '\t不同意'
    elif two_number >= 3:
        audit_result = audit_result + '\t同意'
    else:
        audit_result = audit_result + '\t同意需要修改'

    return audit_result


if __name__ == '__main__':
    for i in range(243):
        print(convert(i))
