import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def frequency_analysis(text):

    text = text.upper()

    letter_frequencies = {}
    #initialize the dictionary
    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


if __name__ == '__main__':

    plain_text = "Hello this is ayush kumar verma"
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)

