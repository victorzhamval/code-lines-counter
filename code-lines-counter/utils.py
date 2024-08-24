from click import echo, style

def print_output(name: str, content: str, bg: str = "white"):
  echo(style(name, bg = bg), nl=False)
  echo(" : ", nl=False)
  echo(style(content, fg = bg), nl=True)

def print_line_jump():
  echo()