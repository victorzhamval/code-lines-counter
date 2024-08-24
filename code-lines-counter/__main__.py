import click
import count

@click.command()
@click.option('-f', '--file', help='Count a single file')
@click.option('-d', '--directory', help='Count a single file')

def cli(file, directory):
  if (file != None):
    count.count_file(file)
  else:
    count.count_dirs(directory)
    
if __name__ == '__main__':
  cli()