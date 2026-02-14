def create_redo_file(input_tsv, output_txt="ids_toredo.txt"):
    redo_ids = []

    with open(input_tsv, "r") as fin:
        header = next(fin)  # skip header

        for line in fin:
            parts = line.strip().split("\t")

            # Ensure row has at least 3 columns
            if len(parts) < 3:
                continue

            release_id, have, want = parts[0], parts[1], parts[2]

            if have == "-1" and want == "-1":
                redo_ids.append(release_id)
            elif have == "-2" and want == "-2":
                redo_ids.append(release_id)
            elif have == "-3" and want == "-3":
                redo_ids.append(release_id)

    # Optional: remove duplicates (safe guard)
    redo_ids = list(set(redo_ids))

    # Write to output file
    with open(output_txt, "w") as fout:
        for rid in redo_ids:
            fout.write(rid + "\n")

    print(f"Created '{output_txt}'")
    print(f"Total IDs to redo: {len(redo_ids)}")


# Example usage
create_redo_file("/Users/licho/Documents/daniel_ids/releases_have_want_minus_worker2.tsv")