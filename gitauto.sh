#!/usr/bin/bash

echo 'What file would you like to add?: '
read FILE
git add $FILE

echo 'Enter commit message: '
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the branch:'
read branch

git push -u origin $branch

read

echo "chasvibe"


