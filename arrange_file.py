import sys

delete_count = 0
args = sys.argv

if(len(args) != 2):
    print("python arrange_file.py ファイル名(.txt除く) の形で入力してください")

with open(f"./{args[1]}.txt") as f:
    output = open(f"(変){args[1]}.txt", "w")
    for i, line in enumerate(f):
        if (delete_count > 0):
            delete_count += 1

            if (delete_count == 4):
                delete_count = 0
            continue

        if(line == "\n"):
            continue

        if(line[:4] == "NOTE"):
            delete_count += 1
            continue

        output.write(line.strip() + "\n")