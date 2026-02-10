#!/usr/bin/env bash

prices=()
quantities=()
total=0

for ((i=0; i<10; i++)); do
  read -p "enter price: " prices[$i]
  read -p "enter quantity: " quantities[$i]
  total=$((total + prices[$i] * quantities[$i]))
done

echo "total stock value: $total"