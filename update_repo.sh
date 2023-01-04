#/usr/bin/env bash

dpkg-scanpackages ./debs > Packages
python ./icons.py
rm Packages.gz Packages.bz2
gzip -c9 Packages > Packages.gz
bzip2 -c9 Packages > Packages.bz2
