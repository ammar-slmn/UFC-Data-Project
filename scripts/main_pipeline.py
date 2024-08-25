import subprocess

def run_clean_data():
    subprocess.run(['python', 'scripts/data_preparation/clean_data.py'])

def run_merge_data():
    subprocess.run(['python', 'scripts/data_preparation/merge_data.py'])

def run_upload_to_s3():
    subprocess.run(['python', 'scripts/cloud_storage/upload_to_aws.py'])

def main():
    run_clean_data()
    run_merge_data()
    run_upload_to_s3()

if __name__ == '__main__':
    main()