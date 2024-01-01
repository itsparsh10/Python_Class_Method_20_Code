#WAP to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Function to calculate word frequency
def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
      
    return frequency

input_text = input("Enter a sentence: ")


frequency_dict = word_frequency(input_text)
sorted_keys = sorted(frequency_dict.keys())

print("Word Frequency:")
for key in sorted_keys:
    print(f"{key}: {frequency_dict[key]}")
