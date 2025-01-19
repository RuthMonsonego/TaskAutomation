import pandas as pd

def generate_report(tasks, output_file):
    df = pd.DataFrame(tasks)
    df.to_csv(output_file, index=False)
    print(f"Report saved to {output_file}")
