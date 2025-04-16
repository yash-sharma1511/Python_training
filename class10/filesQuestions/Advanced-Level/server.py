with open('server.log', 'r') as infile:
    lines = infile.readlines()
error_count = 0
error_lines = []
for line in lines:
    if "ERROR" in line:
        error_count += 1
        error_lines.append(line)
with open('errors_only.log', 'w') as outfile:
    outfile.writelines(error_lines)
print(f'Total ERRORs found: {error_count}')
