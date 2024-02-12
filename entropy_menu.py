import argparse
from entropy_calculator import calculate_alphabet_power, calculate_hartley_entropy, calculate_shannon_entropy, calculate_redundancy

def main():
    parser = argparse.ArgumentParser(description="Entropy Calculator CLI")
    parser.add_argument("filename", help="Name of the text file")
    args = parser.parse_args()

    while True:
        print("\nEntropy Calculator Menu:")
        print("1. Calculate Entropy")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            try:
                with open(args.filename, "r", encoding="utf-8") as file:
                    text = file.read()
            except FileNotFoundError:
                print(f"Error: File '{args.filename}' not found.")
                continue

            alphabet_power = calculate_alphabet_power(text)
            hartley_entropy = calculate_hartley_entropy(alphabet_power)
            shannon_entropy = calculate_shannon_entropy(text)
            redundancy = calculate_redundancy(alphabet_power, shannon_entropy)

            print(f"\nAlphabet Power: {alphabet_power}")
            print(f"Hartley Entropy: {hartley_entropy}")
            print(f"Shannon Entropy: {shannon_entropy}")
            print(f"Redundancy: {redundancy:.2f}%")

        elif choice == "2":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()