import subprocess

import click


@click.command()
@click.argument('username', nargs=1)
def main(username):
    process = subprocess.Popen(['python', 'fetcher.py', username])
    process.communicate()

    process = subprocess.Popen(['python', 'analyzer.py', username])
    process.communicate()

    process = subprocess.Popen(['python', 'plotter.py', username])
    process.communicate()


if __name__ == '__main__':
    main()