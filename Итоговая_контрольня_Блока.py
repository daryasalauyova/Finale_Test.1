def filter_array(strings):
    filtered_array = []
    for string in strings:
        if len(string) <= 3:
            filtered_array.append(string)
    return filtered_array

def main():
    input_array = input("Enter text separated by commas: ").split(",")
    output_array = filter_array(input_array)
    print("Reculte:", output_array)

if __name__ == "__main__":
    main()