import subprocess

import click


@click.command()
@click.option('--username', help='The twitter username.')
def main(username):
    process = subprocess.Popen(['python', 'fetcher.py', '--username', username])
    process.communicate()

    process = subprocess.Popen(['python', 'analyzer.py', '--username', username])
    process.communicate()

    process = subprocess.Popen(['python', 'plotter.py', '--username', username])
    process.communicate()


if __name__ == '__main__':
    main()