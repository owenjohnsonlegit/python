with open('/Users/owenjohnson/Documents/GitHub/python/Python-Class/bruh.txt', 'r') as file1, open('/Users/owenjohnson/Documents/GitHub/python/Python-Class/bruh2.txt', 'r') as file2, open('/Users/owenjohnson/Documents/GitHub/python/Python-Class/output.txt', 'w') as output_file:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        if i < len(lines1):
            output_file.write(f"p1.{i + 1}\n")
            output_file.write(lines1[i])

        if i < len(lines2):
            output_file.write(f"p2.{i + 1}\n")
            output_file.write(lines2[i])