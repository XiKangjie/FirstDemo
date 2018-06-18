import click

@click.command()
@click.argument('name')
def edit(name):
    filename = name + ".cfg"
    click.edit(editor="vim", filename=filename, extension='.cfg')

if __name__ == "__main__":
    edit()
