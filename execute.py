import pandas as pd


def main():
    # Load data from CSV
    df = pd.read_csv('data.csv')
    
    # Perform numeric computations with validation
    total = 0.0
    for value in df['numeric_column']:
        try:
            total += float(value)
        except (ValueError, TypeError):
            continue  # Skip invalid entries
    
    # Save result to JSON
    result = {'total': total}
    with open('result.json', 'w') as json_file:
        json.dump(result, json_file)


if __name__ == '__main__':
    main()