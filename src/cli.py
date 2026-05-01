import click

@click.command()
@click.option('--command', default='help', help='Command to execute')
def cli(command):
    click.echo(f'Executing command: {command}')

if __name__ == '__main__':
    cli()