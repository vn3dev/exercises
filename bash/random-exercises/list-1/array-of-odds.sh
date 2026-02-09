#!/bin/bash

# Escreva um algoritmo que leia 10 números e armazene em um vetor. Depois, mostre apenas os números que estão em posições ímpares do vetor


numbers=()

for ((i=0; i<10; i++)); do
  read -p "Enter the number at position $i: " numbers[$i]
done

echo
echo "Numbers at odd positions in the array:"

for ((i=1; i<10; i+=2)); do
  echo "Position $i -> ${numbers[$i]}"
done