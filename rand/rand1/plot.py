import matplotlib.pyplot as plt

def plot_linear(input_sizes, average_hires):
    plt.plot(input_sizes, average_hires, marker="o")

    plt.xticks(input_sizes, labels=input_sizes)

    plt.xlabel("Number of candidates")
    plt.ylabel("Average number of hires")
    plt.title("Average hires by input size - Linear scale")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_semi_log(input_sizes, average_hires):
    plt.plot(input_sizes, average_hires, marker="o")

    plt.xscale("log")
    plt.xticks(input_sizes, labels=input_sizes)

    plt.xlabel("Number of candidates")
    plt.ylabel("Average number of hires")
    plt.title("Average hires by input size - Logarithmic x-axis")
    plt.grid(True)

    plt.tight_layout()
    plt.show()