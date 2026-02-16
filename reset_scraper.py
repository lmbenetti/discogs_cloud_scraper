import os
import glob

def reset_scraper():
    files_to_delete = [
        "token.txt",
        "worker_name.txt"
    ]

    deleted = 0

    # 1️⃣ Delete fixed files
    for filename in files_to_delete:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Deleted {filename}")
            deleted += 1

    # 2️⃣ Delete releases_have_want_*.tsv files
    for filepath in glob.glob("releases_have_want_*.tsv"):
        os.remove(filepath)
        print(f"Deleted {filepath}")
        deleted += 1

    print(f"\nReset complete. Deleted {deleted} files.")

if __name__ == "__main__":
    reset_scraper()