# Use this these commands
```
# create a folder and copy all the zips
mkdir contest_zip
for i in */data/sample/; do mkdir -p contest_zip/$(dirname $i); cp -r $i contest_zip/$i;  done;

for f in *.pdf; do d="${f%.pdf}"; mv "$f" "contest/$d/"; done
```
