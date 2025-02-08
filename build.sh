git checkout --orphan gh-pages
git add -f build/*
git commit -m "Deploy to GitHub Pages"
git push origin gh-pages --force
