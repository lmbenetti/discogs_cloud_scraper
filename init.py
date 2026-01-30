import os
import sys
import glob


def main():
    existing_workers = glob.glob("releases_have_want_*.tsv")
    if existing_workers:
        print("A worker has already been initialized in this directory.")
        print("Doing nothing.")
        return
    
    try:
        worker_num = int(input("Enter worker number (integer): ").strip())
    except ValueError:
        print("Worker number must be an integer.")
        sys.exit(1)

    worker_name = f"worker{worker_num}"
    tsv_filename = f"releases_have_want_{worker_name}.tsv"

    if os.path.exists(tsv_filename):
        print(f"Worker '{worker_name}' is already initialized. Exit.")
        return

    token = input("Enter Discogs token: ").strip()
    if not token:
        print("Token cannot be empty.")
        sys.exit(1)

    with open("token.txt", "w") as f:
        f.write(token)


    with open("worker_name.txt", "w") as f:
        f.write(worker_name + "\n")

    with open(tsv_filename, "w") as f:
        f.write("release\thave\twant\n")

    print("Worker initialized successfully:")
    print(f"  Worker name: {worker_name}")
    print(f"  Token file: token.txt")
    print(f"  Output file: {tsv_filename}")

if __name__ == "__main__":
    main()