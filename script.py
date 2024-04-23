import sys
import subprocess
import shutil

# Accept two numbers as command line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <min_chars> <max_chars>")
    sys.exit(1)

min_chars = int(sys.argv[1])
max_chars = int(sys.argv[2])

# Run a loop from min_chars to max_chars
for length in range(min_chars, max_chars + 1):
    # Print the length being processed
    print(f"Generating passwords with length: {length}")

    # Execute the command './enumNG -H=hint-file.txt -a=alpha-file.txt -m 100000 -l <length> -L 2 -u=username.txt'
    command = ['./enumNG', '-H=hint-file.txt', '-a=alpha-file.txt', '-m', '1000', '-l', str(length), '-L', '2', '-u=username.txt']

    try:
        # Run the command
        subprocess.run(command, check=True)

        # Copy the results from ./results/createdPWs.txt into the new file
        shutil.copyfile("./results/createdPWs.txt", f"./results/createdPWs_{length}.txt")
        print(f"Output saved to ./results/createdPWs_{length}.txt")
        
    except subprocess.CalledProcessError as e:
        print("Error:", e)
