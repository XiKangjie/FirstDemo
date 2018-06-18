import click

class Repo(object):
    def __init__(self, debug=False):
        self.debug = debug

pass_repo = click.make_pass_decorator(Repo)

@click.group()
#@click.option('-n', '--debug/--no-debug', default=True)
@click.option('-d', '--debug', is_flag=True, default=True)
@click.pass_context
def cli(ctx, debug):
    ctx.obj = Repo(debug)
    click.echo(ctx.obj)
    print "cli repo debug: %s" % debug

@cli.command()
@click.option('--debug/--no-debug', default=False)
@pass_repo
def set_repo(repo, debug):
    repo.debug = debug
    click.echo(repo)
    print "set_repo debug: %s" % debug

@cli.command()
@pass_repo
def get_repo(repo):
    click.echo(repo)
    print "get_repo debug: %s" % repo.debug

if __name__ == '__main__':
    cli()


"""
$ python context.py --debug get_repo
<__main__.Repo object at 0x7feaea92d850>
cli repo debug: True
<__main__.Repo object at 0x7feaea92d850>
get_repo debug: True


$ python context.py set_repo --debug
<__main__.Repo object at 0x7f83c0289850>
cli repo debug: False
<__main__.Repo object at 0x7f83c0289850>
set_repo debug: True

$ python context.py get_repo
<__main__.Repo object at 0x7f7d10754850>
cli repo debug: False
<__main__.Repo object at 0x7f7d10754850>
get_repo debug: False
"""
