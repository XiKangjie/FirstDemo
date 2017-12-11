import click

@click.command()
@click.option('-c', '--count', default=1, help='Number of greetings.')
@click.option('-fs', '--first-second', prompt='Your name first second',
              help='The person to greet.')
@click.option('-f', '--first', help='The person to greet.')
@click.option('-s', '--second', help='The person to greet.')
def hello(count, first_second, first, second):
    """Simple program that greets NAME for a total of COUNT times."""
    for i in (first_second, first, second):
        for x in range(count):
            if i:
                click.echo('Hello %s!' % (i))

if __name__ == '__main__':
    hello()

"""
$ python hello.py -n "aa bb"
Hello aa bb!
$ python hello.py --first-second "aa bb"
Hello aa bb!
$ python hello.py --first-second="aa bb"
Hello aa bb!
$ python hello.py -fs="aa bb"
Hello =aa bb!
$ python hello.py -c 2 -fs"aa bb"
Hello aa bb!
Hello aa bb!
$ python hello.py -fs "1 2" -f 3 -s 4
Hello 1 2!
Hello 3!
Hello 4!
"""
