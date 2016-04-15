import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, default=False, help='Run in debug mode.')
def mygit(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@mygit.command()
@click.option('-f', '--force', is_flag=True, default=False, help='Force pull.')
@click.argument('repo')
def pull(force, repo):
    ''' Pull repo. '''
    if force:
        click.echo('Force pull {0}'.format(repo))
    else:
        click.echo('Pull {0}'.format(repo))

@mygit.command()
@click.option('-f', '--force', is_flag=True, default=False, help='Force push.')
@click.argument('repo')
def push(force, repo):
    ''' Push repo. '''
    if force:
        click.echo('Force push {0}'.format(repo))
    else:
        click.echo('Push {0}'.format(repo))
