#!/bin/bash
pip3 freeze > requirements.txt
git add .
echo "You can now proceed to git commit with your preferred message, and git push :)"