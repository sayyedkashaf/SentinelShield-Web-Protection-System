from detector import detect_attack

test_input = input("Enter test input: ")

result = detect_attack(test_input)

if result:
    print("Attack Detected:", result)
else:
    print("Safe Request")