input_file = "logLatesta.txt"
output_file = "logLatesta0.txt"

with open(input_file, "r") as infile:
    with open(output_file, "w") as outfile:
        for line in infile:
            if "ext hdr" in line or "request" in line:
                if ("ext hdr" in line and "ID:1" in line):
                    # print("Got it!")
                    continue
            # and "nbr" not in line and "routing" not in line and "links" not in line and "neighbor" not in line and "DIO" not in line and "probing" not in line and "lifetime" not in line and "DAO" not in line and "DIS" not in line: 
                outfile.write(line)