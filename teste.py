def front_back(string):
  start = string[0]
  end = string[len(string)-1]
  s1 = string.lstrip(start)
  s2 = s1.rstrip(end)
  return end + s2 + start
print(front_back('supercalifragilisticexpialidotion'))
