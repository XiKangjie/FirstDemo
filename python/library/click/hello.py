import click

@click.command()
@click.option('-c', '--count', default=1, help='Number of greetings.')
@click.option('-n', '--first-second', prompt='Your name first second',
              help='The person to greet.')
def hello(count, first_second):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % first_second)

if __name__ == '__main__':
    hello()

"""
$ python hello.py -n "aa bb"
Hello aa bb!
$ python hello.py --first-second "aa bb"
Hello aa bb!
$ python hello.py --first-second="aa bb"
Hello aa bb!
$ python hello.py -n="aa bb"
Hello =aa bb!
$ python hello.py -c 2 -n"aa bb"
Hello aa bb!
Hello aa bb!
"""
