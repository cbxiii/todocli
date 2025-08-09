import typer 

app = typer.Typer()

# @app.command()
# def hello(name: str, iq: int, display_iq: bool = True):
#     print(f"Hello, {name}")
#     if display_iq:
#         print(f"Your IQ is {iq}")

# @app.command()
# def goodbye():
#     print("Goodbye")

@app.command()
def add(todo: str):
    first_time = input("Is this the first item you're adding? (Answer 'yes' or 'no'.)")
    if first_time.lower() == "yes":
        try:
            with open("todolist.txt", 'w') as f:
                f.write(todo + "\n")
            print(f"Added '{todo}' to your to-do list.")
        except:
            print("Couldn't add to your to-do list.")
    elif first_time.lower() == "no":
        try:
            with open("todolist.txt", 'a') as f:
                f.write(todo + "\n")
            print(f"Added '{todo}' to your to-do list.")
        except:
            print("Couldn't add to your to-do list.")
    else:
        print("Please enter either 'yes' or 'no'.")


@app.command()
def remove(todo: str):
    print(f"Successfully removed todo: {todo}")

@app.command()
def list():
    print("Your Current To-do List: \n")
    try:
        with open("todolist.txt", 'r') as f:
            for line in f:
                print("-- " + line)
    except:
        print("Todo list file has not yet been created. Please add at least one todo with the 'add' command." \
        " Type 'todo_cli.py --help.' for more help.")


if __name__ == "__main__":
    app()