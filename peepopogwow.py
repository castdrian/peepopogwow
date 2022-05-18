from colorama import Fore

def print_rainbow(text):
	colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
	for i, c in enumerate(text):
		print(colors[i % len(colors)], c, end="")
	print(Fore.RESET)

print_rainbow("peepopog wow".join([" " for _ in range(0, int(80 * 25))]))