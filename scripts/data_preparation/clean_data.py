import pandas as pd
import logging
from typing import List

def clean_data():
    # Load raw data
    event_data = pd.read_csv('data/raw/ufc_event_data.csv')
    fight_data = pd.read_csv('data/raw/ufc_fight_data.csv')
    fight_stats = pd.read_csv('data/raw/ufc_fight_stat_data.csv')
    fighter_data = pd.read_csv('data/raw/ufc_fighter_data.csv')

    # remove columns that are not needed
    event_data.drop('event_url', axis=1, inplace=True)
    fight_data.drop('fight_url', axis=1, inplace=True)
    fight_stats.drop('fight_url', axis=1, inplace=True)
    fighter_data.drop(['fighter_nickname', 'fighter_url', 'fighter_stance'], axis=1, inplace=True)

    # handle missing values
    event_data['event_state'] = event_data['event_state'].fillna(event_data['event_city'])
    fight_data['result_details'] = fight_data['result_details'].fillna(fight_data['result'])
    fight_data = fight_data.dropna(subset=['f_1', 'f_2', 'winner', 'weight_class', 'referee']) 
    fight_stats = fight_stats.dropna(subset = ['fighter_id', 'knockdowns', 'total_strikes_att', 'total_strikes_succ', 'sig_strikes_att', 'sig_strikes_succ', 'takedown_att', 'takedown_succ', 'submission_att', 'reversals', 'ctrl_time'])
    fighter_data['fighter_nc_dq'] = fighter_data['fighter_nc_dq'].fillna('0')
    fighter_data = fighter_data.dropna(subset=['fighter_weight_lbs', 'fighter_l_name', 'fighter_dob', 'fighter_height_cm'])
    fighter_data['fighter_reach_cm'] = fighter_data['fighter_reach_cm'].fillna(fighter_data['fighter_height_cm'])

    # remove duplicates
    event_data.drop_duplicates(inplace=True)
    fight_data.drop_duplicates(inplace=True)
    fight_stats.drop_duplicates(inplace=True)
    fighter_data.drop_duplicates(inplace=True)

    # Save cleaned data
    event_data.to_csv('data/cleaned/event_data_clean.csv', index=False)
    fight_data.to_csv('data/cleaned/fight_data_clean.csv', index=False)
    fight_stats.to_csv('data/cleaned/fight_stats_clean.csv', index=False)
    fighter_data.to_csv('data/cleaned/fighter_data_clean.csv', index=False)

if __name__ == '__main__':
    clean_data()