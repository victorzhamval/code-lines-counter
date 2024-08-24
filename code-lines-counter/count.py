import os
import utils

def count_file(file: str, should_print_output: bool = True):
  isFile = os.path.isfile(file)
  if isFile:
    lines_count = 0
    lines = open(file,  errors="ignore")
    real_path = os.path.realpath(file)
    if should_print_output: utils.print_line_jump()
    blank_lines_count = 0
    for line in lines:
      lines_count += 1
      line_stp = line.strip()
      if line_stp == "":
        blank_lines_count += 1
    if should_print_output:
      utils.print_file_output(lines_count, blank_lines_count, real_path)
    return [lines_count, blank_lines_count]
  else:
    utils.print_line_jump()
    utils.print_error("File not found. -> " + file)
    return [0, 0]

def count_files(files: tuple):
  lines_count = 0
  blank_lines_count = 0
  for file in files:
    c_file = count_file(file)
    lines_count += c_file[0]
    blank_lines_count += c_file[1]
  utils.print_line_jump()
  if len(files) > 1:
    utils.print_dir_output(lines_count, blank_lines_count)
    utils.print_line_jump()

def count_dir(dir: str):
  lines_count = 0
  blank_lines_count = 0
  files = list(map(lambda file: dir + "/" + file, os.listdir(dir)))
  real_path = os.path.realpath(dir) 
  utils.print_dir(real_path)
  utils.print_line_jump()
  for file in files:
    is_file = os.path.isfile(file)
    if is_file:
      c_file = count_file(file, False)
      lines_count += c_file[0]
      blank_lines_count += c_file[1]
  utils.print_file_output(lines_count, blank_lines_count)
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
    utils.print_dir_output(lines_count, blank_lines_count)
    utils.print_line_jump()
  else:
    utils.print_error("Directory not found.")
