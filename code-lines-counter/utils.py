from click import echo, style

def print_data(name: str, content: str, bg: str = "white"):
  echo(style(name, bg = bg), nl=False)
  echo(" : ", nl=False)
  echo(style(content, fg = bg), nl=True)

def print_file_output(lines_count, blank_lines_count, file: str = None):
  if (file != None): print_data("File", file, "cyan")
  print_data("Lines", str(lines_count), "green")
  print_data("Blank lines", str(blank_lines_count), "magenta")

def print_dir_output(lines_count, blank_lines_count):
  print_data("Total Lines", str(lines_count), "yellow")
  print_data("Total blank lines", str(blank_lines_count), "yellow")

def print_dir(dir: str):
  print_data("Directory", dir, bg="blue")

def print_line_jump():
  echo()

def print_error(error: str):
  print_data("Error", error, "red")