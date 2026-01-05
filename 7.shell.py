import subprocess
import sys
import os

def execute_command(cmd_line):
    # 1. Handle Piping (|)
    if '|' in cmd_line:
        parts = cmd_line.split('|')
        processes = []
        prev_stdout = None

        for i, part in enumerate(parts):
            args = part.strip().split()
            
            # Determine stdin and stdout for this stage of the pipe
            stdin = prev_stdout if i > 0 else None
            stdout = subprocess.PIPE if i < len(parts) - 1 else None
            
            try:
                proc = subprocess.Popen(args, stdin=stdin, stdout=stdout, text=True)
                processes.append(proc)
                
                # Close the previous pipe's output in the parent to avoid hanging
                if prev_stdout:
                    prev_stdout.close()
                prev_stdout = proc.stdout
            except Exception as e:
                print(f"Shell error: {e}")
                return

        # Get the final output from the last process
        if processes:
            out, err = processes[-1].communicate()
            if out:
                print(out, end="")
        return

    # 2. Handle Redirection (< and >)
    args = cmd_line.strip().split()
    input_file = None
    output_file = None

    # Parse args for redirection symbols
    if '>' in args:
        idx = args.index('>')
        if idx + 1 < len(args):
            output_file = args[idx + 1]
            args = args[:idx] # Remove > and filename from command arguments

    if '<' in args:
        idx = args.index('<')
        if idx + 1 < len(args):
            input_file = args[idx + 1]
            args = args[:idx] # Remove < and filename from command arguments

    # 3. Execute basic command or redirected command
    try:
        fin = open(input_file, 'r') if input_file else None
        fout = open(output_file, 'w') if output_file else None

        subprocess.run(args, stdin=fin, stdout=fout)

        if fin: fin.close()
        if fout: fout.close()
    except FileNotFoundError:
        print(f"Shell error: File not found.")
    except Exception as e:
        print(f"Shell error: {e}")

def main():
    print("Simple Python Shell. Type 'exit' or use Ctrl+D to quit.")
    while True:
        try:
            # Display prompt and get user input
            user_input = input("python_shell> ")
            
            if not user_input.strip():
                continue
            if user_input.lower() == 'exit':
                break
                
            execute_command(user_input)
            
        except (EOFError, KeyboardInterrupt):
            print("\nExiting shell...")
            break

if __name__ == "__main__":
    main()