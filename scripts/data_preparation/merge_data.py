import pandas as pd

def merge_data():
    # Load cleaned data
    event_data = pd.read_csv('data/cleaned/event_data_clean.csv')
    fight_data = pd.read_csv('data/cleaned/fight_data_clean.csv')
    fight_stats = pd.read_csv('data/cleaned/fight_stats_clean.csv')
    fighter_data = pd.read_csv('data/cleaned/fighter_data_clean.csv')

    fight_event_merge = fight_data.merge(event_data, on='event_id')
    stats_merge = fight_event_merge.merge(fight_stats, on='fight_id')
    fighter_merge = stats_merge.merge(fighter_data, on='fighter_id')

    fighter_merge.to_csv('data/processed/ufc_data_prepared.csv', index=False)

if __name__ == '__main__':
    merge_data()