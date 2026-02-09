#!/usr/bin/env bash

# Crie um algoritmo que leia 15 números, armazene em um vetor e diga quantos números são maiores que a média dos valores informados.

numbers=()
sum=0
count=0

for ((i=0; i<15; i++)); do
  read -p "enter a number: " numbers[$i]
  sum=$((sum + numbers[$i]))
done

avg=$((sum / 15))

echo "average: $avg"

for n in "${numbers[@]}"; do
  if (( n > avg )); then
    count=$((count + 1))
  fi
done

echo "greater than average: $count"
