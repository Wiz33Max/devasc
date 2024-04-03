import click

@click.command()
@click.option('--name', prompt='Your name', help='Enter your name')
@click.option('--age', prompt='Your age', help='Enter your age')
def greet(name, age):
    """A simple command-line tool to greet users."""
    message = "Hello, {}! You are {} years old.".format(name, age)

if __name__ == '__main__':
    greet()
