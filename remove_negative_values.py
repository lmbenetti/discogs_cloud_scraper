import os

def remove_negative_rows(input_file):
    temp_file = input_file + ".tmp"
    removed = 0
    kept = 0

    with open(input_file, "r") as fin, open(temp_file, "w") as fout:
        header = next(fin)
        fout.write(header)

        for line in fin:
            parts = line.rstrip("\n").split("\t")

            if len(parts) < 3:
                continue  # skip malformed rows

            release_id, have, want = parts

            if have == "-1" and want == "-1":
                removed += 1
                continue  # skip writing this row
            elif have == "-2" and want == "-2":
                removed += 1
                continue  # skip writing this row
            elif have == "-3" and want == "-3":
                removed += 1
                continue  # skip writing this row
            fout.write(line)
            kept += 1

    os.replace(temp_file, input_file)

    print(f"Removed {removed} rows.")
    print(f"Kept {kept} rows.")

remove_negative_rows("/Users/licho/Documents/daniel_ids/releases_have_want_worker5.tsv")
