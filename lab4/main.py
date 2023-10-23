import random

# Function to embed a single bit message in an RTF file
def embed_message(input_file, message_file, output_file):
    with open(input_file, 'r') as in_file:
        rtf_data = in_file.read()

    with open(message_file, 'r') as msg_file:
        message = msg_file.read()

    # Generate a list of random positions to hide the message
    positions = random.sample(range(len(rtf_data)), len(message))

    # Embed the message bits into the RTF file
    result_data = list(rtf_data)
    for i, pos in enumerate(positions):
        result_data[pos] = f'\\u{ord(message[i]):04x}'

    with open(output_file, 'w') as out_file:
        out_file.write("".join(result_data))

# Function to calculate character distribution in a text file
def character_distribution(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    distribution = {}
    for char in content:
        if char.isalpha():
            distribution[char] = distribution.get(char, 0) + 1
    return distribution

if __name__ == '__main__':
    input_rtf_file = 'container.rtf'
    message_file = 'message.txt'
    output_rtf_file = 'result.rtf'

    # Embed the message
    embed_message(input_rtf_file, message_file, output_rtf_file)

    # Character distribution before embedding
    distribution_before = character_distribution(input_rtf_file)

    # Character distribution after embedding
    distribution_after = character_distribution(output_rtf_file)

    # Display character distributions in tables
    print("Character Distribution Before Embedding:")
    print("{:<6} {:<6}".format("Char", "Count"))
    for char, count in distribution_before.items():
        print("{:<6} {:<6}".format(char, count))

    print("\nCharacter Distribution After Embedding:")
    print("{:<6} {:<6}".format("Char", "Count"))
    for char, count in distribution_after.items():
        print("{:<6} {:<6}".format(char, count))
