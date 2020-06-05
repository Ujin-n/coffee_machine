unit_num = int(input())

if unit_num >= 1000:
    print("legion")
elif unit_num >= 500:
    print("swarm")
elif unit_num >= 50:
    print("horde")
elif unit_num >= 10:
    print("pack")
elif unit_num >= 1:
    print("few")
else:
    print("no army")
