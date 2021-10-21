#!/bin/bash

echo "Please enter a number: "
read number_1

echo "Please enter one more: "
read number_2

result=$((number_1 + number_2))
echo "The answer is: $result"
