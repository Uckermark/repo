import os

with open("Packages", 'r') as file:
  packages = []
  text = file.read()
  lines = text.split("\n")
  for line in lines:
    if "Package: " in line:
      packages.append(line)

for package in packages:
  text1, text2 = text.split(package + "\n")
  id = package.split("Package: ")[1]
  if os.path.exists("./icons/" + id + ".webp"):
    icon = "Icon: https://www.uckermark.tk/repo/icons/" + id + ".webp\n"
    text = text1 + "\n" + package + "\n" + icon + text2

with open("Packages", 'w') as file:
  file.write(text)
