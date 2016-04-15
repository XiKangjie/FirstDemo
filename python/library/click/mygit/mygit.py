import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, default=False, help='Run in debug mode.')
def mygit(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@mygit.command()
@click.option('-f', '--force', is_flag=True, default=False, help='Force pull.')
@click.argument('repo')
def pull():
    ''' Pull repo. '''
    click.echo('Pulling')

@mygit.command()
@click.option('-f', '--force', is_flag=True, default=False, help='Force push.')
@click.argument('repo')
def push():
    ''' Push repo. '''
    click.echo('Pushing')
