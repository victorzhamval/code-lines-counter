import os
import utils

def count_file(file: str, should_print_output: bool = True):
  isFile = os.path.isfile(file)
  if isFile:
    lines_count = 0
    lines = open(file,  errors="ignore")
    if should_print_output: utils.print_line_jump()
    blank_lines_count = 0
    for line in lines:
      lines_count += 1
      line_stp = line.strip()
      if line_stp == "":
        blank_lines_count += 1
    if should_print_output:
      utils.print_output("File", os.path.realpath(file), "cyan")
      utils.print_output("Lines", str(lines_count), "green")
      utils.print_output("Blank lines", str(blank_lines_count), "magenta")
      utils.print_line_jump()
    return [lines_count, blank_lines_count]
  else:
    utils.print_output("Error", "File not found.", "red")
    return [0, 0]     

def count_dir(dir: str):
  lines_count = 0
  blank_lines_count = 0
  files = list(map(lambda file: dir + "/" + file, os.listdir(dir)))
  utils.print_output("Directory: ", dir, "blue")
  utils.print_line_jump()
  for file in files:
    is_file = os.path.isfile(file)
    if is_file:
      c_file = count_file(file, False)
      lines_count += c_file[0]
      blank_lines_count += c_file[1]
  utils.print_output("Total lines", lines_count, "yellow")
  utils.print_output("total blank lines", blank_lines_count, "yellow")
  utils.print_line_jump()
  return [lines_count, blank_lines_count]
  
def count_dirs(dir: str):
  is_dir = os.path.isdir(dir)

  if is_dir:
    dirs = list(os.walk(dir))
    lines_count = 0
    blank_lines_count = 0
    utils.print_line_jump()
    for curr_dir in dirs: 
      c_dir = count_dir(curr_dir[0])
      lines_count += c_dir[0]
      blank_lines_count += c_dir[1]
    utils.print_output("Total lines", lines_count, "yellow")
    utils.print_output("total blank lines", blank_lines_count, "yellow")
    utils.print_line_jump()
  else:
    utils.print_output("Error", "Directory not found.", "red")
  