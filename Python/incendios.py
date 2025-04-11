import csv
from collections import defaultdict

def somaIncendios(csv_file):
    sums = defaultdict(int)
    
    # Abrir e ler o arquivo CSV
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            year = row['year']
            state = row['state']
            number = int(row['number'])
            
            # Somar os números agrupando por 'year' e 'state'
            sums[(year, state)] += number
    
    return sums

csv_file = 'amazon.csv'
result = somaIncendios(csv_file)

year_input = input("Digite o ano desejado: ")
state_input = input("Digite o estado desejado: ")

total = result.get((year_input, state_input), 0)
print(f'Total para {year_input} em {state_input}: {total}')