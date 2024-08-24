import click
import count

@click.command()
@click.option('-f', '--file', help='Count a single file', multiple=True)
@click.option('-d', '--directory', help='Count a single file', multiple=False)

def cli(file: tuple, directory: str):
  
  if not (len(file)  == 0):
    count.count_files(file)
  else:
    count.count_dirs(directory)
    
if __name__ == '__main__':
  cli()