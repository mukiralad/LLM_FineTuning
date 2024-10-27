import json
import random

def load_email_data(input_file='emails_data.json'):
    """Load the email data from JSON file"""
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_enhanced_system_message():
    """Create a comprehensive system message for better email generation"""
    return (
        "You are an AI assistant that helps craft personalized cold emails for job opportunities. Follow these principles:\n"
        "1. Keep emails brief (150-200 words)\n"
        "2. Show genuine interest in the company/person\n"
        "3. Demonstrate clear value proposition\n"
        "4. Be respectful of their time\n"
        "5. Include a specific, time-bound call to action\n"
        "6. Sound human, authentic, and slightly vulnerable\n"
        "7. Use research-backed details about the recipient/company\n"
        "8. End with a polite, non-demanding request"
    )

def create_finetune_examples(emails):
    """Convert emails to fine-tuning format with improved structure"""
    finetune_data = []
    
    for email in emails:
        messages = [
            {
                "role": "system",
                "content": get_enhanced_system_message()
            },
            {
                "role": "user",
                "content": (
                    "Write a cold email using this subject line format: '{}'. "
                    "Background: Graduate student at University X, Bachelor's background, "
                    "recent experience as Engineer at Company Y. "
                    "Make it personal and include a polite request for a brief chat."
                ).format(email['subject'])
            },
            {
                "role": "assistant",
                "content": "Subject: {}\n\n{}".format(
                    email['subject'],
                    email['body'].replace('\r\n', '\n').strip()
                )
            }
        ]
        
        example = {
            "messages": messages
        }
        
        finetune_data.append(example)
    
    return finetune_data

def validate_email_quality(email_content):
    """Basic validation of email quality"""
    lines = email_content.split('\n')
    word_count = len(' '.join(lines).split())
    
    return {
        'length_ok': 100 <= word_count <= 250,  # Slightly relaxed constraints
        'has_greeting': any(line.lower().startswith(('hi', 'hello', 'dear')) for line in lines),
        'has_signature': any('best' in line.lower() or 'regards' in line.lower() for line in lines)
    }

def split_data(data, train_ratio=0.8):
    """Split data into training and testing sets"""
    random.shuffle(data)
    split_idx = int(len(data) * train_ratio)
    return data[:split_idx], data[split_idx:]

def save_finetune_data(data, filename):
    """Save data in JSONL format with quality checks"""
    valid_examples = []
    for example in data:
        email_content = example['messages'][2]['content']
        quality_check = validate_email_quality(email_content)
        if all(quality_check.values()):
            valid_examples.append(example)
    
    with open(filename, 'w', encoding='utf-8') as f:
        for example in valid_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')

def main():
    try:
        print("Loading email data...")
        emails = load_email_data()
        
        print("Converting to fine-tuning format...")
        finetune_data = create_finetune_examples(emails)
        
        print("Splitting into train and test sets...")
        train_data, test_data = split_data(finetune_data)
        
        print(f"Saving {len(train_data)} training examples...")
        save_finetune_data(train_data, 'train_data.jsonl')
        
        print(f"Saving {len(test_data)} testing examples...")
        save_finetune_data(test_data, 'test_data.jsonl')
        
        print("\nConversion complete!")
        print(f"Total examples: {len(finetune_data)}")
        print(f"Training examples: {len(train_data)}")
        print(f"Testing examples: {len(test_data)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
