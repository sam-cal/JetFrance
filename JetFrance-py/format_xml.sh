
cat villes_france_2.xml \
|sed -e 's/<\/column>/\/>/g' \
|sed -e 's/d">/d"/g'

