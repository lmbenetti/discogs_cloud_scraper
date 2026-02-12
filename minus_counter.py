def count_minus_one_rows(filename):
    total = 0
    minus_one = 0

    with open(filename, "r") as f:
        next(f)  # skip header
        for line in f:
            total += 1
            parts = line.strip().split("\t")
            if len(parts) >= 3 and parts[1] == "-1" and parts[2] == "-1":
                minus_one += 1

    percentage = (minus_one / total * 100) if total > 0 else 0.0

    print(f"Total rows: {total}")
    print(f"-1/-1 rows: {minus_one}")
    print(f"Percentage: {percentage:.2f}%")

    return minus_one, percentage


# usage
count_minus_one_rows("releases_have_want_total.tsv")