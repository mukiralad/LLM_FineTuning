import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

def upload_training_files():
    """Upload training and validation files to OpenAI"""
    try:
        print("Uploading training file...")
        train_file = client.files.create(
            file=open("data/processed/YOUR_TRAIN_FILE.jsonl", "rb"),
            purpose="fine-tune"
        )
        
        print("Uploading validation file...")
        val_file = client.files.create(
            file=open("data/processed/YOUR_VAL_FILE.jsonl", "rb"),
            purpose="fine-tune"
        )
        
        return train_file.id, val_file.id
    except Exception as e:
        print(f"Error uploading files: {str(e)}")
        raise

def create_fine_tuning_job(training_file_id, validation_file_id):
    """Create and start fine-tuning job"""
    try:
        print("Creating fine-tuning job...")
        job = client.fine_tuning.jobs.create(
            training_file=training_file_id,
            validation_file=validation_file_id,
            model="gpt-3.5-turbo",  # Placeholder for the base model
            hyperparameters={
                "n_epochs": 3  # Replace if needed with configurable parameters
            }
        )
        return job.id
    except Exception as e:
        print(f"Error creating fine-tuning job: {str(e)}")
        raise

def monitor_progress(job_id):
    """Monitor fine-tuning progress"""
    while True:
        try:
            job = client.fine_tuning.jobs.retrieve(job_id)
            print(f"Status: {job.status}")
            
            if job.status in ['succeeded', 'failed']:
                if job.status == 'succeeded':
                    print(f"Fine-tuning complete! Model ID: {job.fine_tuned_model}")
                else:
                    print("Fine-tuning failed!")
                break
                
            # Get recent events
            events = client.fine_tuning.jobs.list_events(
                job_id,
                limit=5
            )
            for event in events:
                print(f"{event.created_at}: {event.message}")
                
            time.sleep(60)  # Check every minute
            
        except Exception as e:
            print(f"Error monitoring job: {str(e)}")
            break

def main():
    try:
        # Upload files
        train_file_id, val_file_id = upload_training_files()
        print(f"Files uploaded successfully. Training file ID: {train_file_id}")
        
        # Create fine-tuning job
        job_id = create_fine_tuning_job(train_file_id, val_file_id)
        print(f"Fine-tuning job created. Job ID: {job_id}")
        
        # Monitor progress
        print("Monitoring training progress...")
        monitor_progress(job_id)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
