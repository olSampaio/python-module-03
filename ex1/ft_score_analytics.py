import sys

def convert(arg):
	try:
		return (int(arg))
	except ValueError:
		print(f"Invalid parameter: '{arg}'")
		return None

def main():

	idx = 1

	print("=== Player Score Analytics ===")
	if(len(sys.argv) == 1):
		print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
		return

	lista = [convert(arg) for arg in sys.argv[1:]]	
	numeros = [nbr for nbr in lista if nbr is not None]
	if (len(numeros) == 0):
		print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
		return
	if(len(sys.argv) > 1):
		print(f"Scores processed: {numeros}")
		print(f"Total players: {len(sys.argv) - 1}")
		print(f"Total score: {sum(numeros)}")
		print(f"Average score: {sum(numeros) / (len(sys.argv) - 1)}")
		print(f"High score: {max(numeros)}")
		print(f"Low score: {min(numeros)}")
		print(f"Score range: {max(numeros) - min(numeros)}")

if __name__ == "__main__":
	main()