import csv
import itertools

# Load CSV tables
def load_table(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)[1:]
        table = {}
        for row in reader:
            key = row[0]
            for col, val in zip(header, row[1:]):
                table[(key,col)] = val
        return table

WHO = load_table("tables/WHO_table.csv")
WHERE = load_table("tables/WHERE_table.csv")
WHEN = load_table("tables/WHEN_table.csv")

WHO_list = ["ME","WE","YOU⁺","YOU⁻","THEY₀","THEY₄"]
WHERE_list = ["EAST","SOUTH","WEST","NORTH"]
WHEN_list = ["SPRING","SUMMER","AUTUMN","WINTER"]

# Generate full 96x96 table
with open("tables/FULL_TABLE.csv","w",newline="") as f:
    writer = csv.writer(f)
    header = [""] + [f"{w},{r},{t}" for w in WHO_list for r in WHERE_list for t in WHEN_list]
    writer.writerow(header)
    for w1,r1,t1 in itertools.product(WHO_list, WHERE_list, WHEN_list):
        row = [f"{w1},{r1},{t1}"]
        for w2,r2,t2 in itertools.product(WHO_list, WHERE_list, WHEN_list):
            w3 = WHO[(w1,w2)]
            r3 = WHERE[(r1,r2)]
            t3 = WHEN[(t1,t2)]
            row.append(f"{w3},{r3},{t3}")
        writer.writerow(row)
