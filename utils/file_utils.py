def load_fasta(file_location):
  f = open(file_location, "r")
  lines = f.readlines()
  result = dict()

  dna = ''
  filename = ''
  for idx, line in enumerate(lines):
    if line.startswith('>'):
      filename = line[1:].rstrip()
    else:
      dna = dna + line.strip()

      if idx >= len(lines)-1 or lines[idx + 1].startswith('>'):
        result[filename] = dna
        filename = ''
        dna = ''

  return result

