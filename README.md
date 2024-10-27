# LLM Fine-Tuning for Cold Email Generation

![LLM Fine-Tuning](https://img.shields.io/badge/LLM-Fine--Tuning-blue.svg) ![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg) ![Stars](https://img.shields.io/github/stars/mukiralad/LLM_FineTuning.svg) ![License](https://img.shields.io/github/license/mukiralad/LLM_FineTuning)

Welcome to **LLM Fine-Tuning for Cold Email Generation**! This project allows you to fine-tune a state-of-the-art language model to generate personalized cold emails for job opportunities, marketing, and outreach. Whether you are a recruiter, salesperson, or a job seeker, our fine-tuned model will help you craft human-like emails that engage and convert.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Fine-Tuning Process](#fine-tuning-process)
- [Usage Guide](#usage-guide)
- [Data Preparation](#data-preparation)
- [How to Contribute](#how-to-contribute)
- [References](#references)
- [License](#license)

## Features
- Fine-tune your any SOTA GPT model for **personalized cold email generation**.
- In-depth guides to help you understand every step of the fine-tuning process.
- Example JSON files for training and testing to get you started easily.
- Quality-focused data validation to ensure high-quality outputs.
- Support for generating cold emails with **specific calls to action** and tailored content.

## Demo
Check out the **demo cold emails** generated using this repository! View the `generated_email.txt` for a sample of what this fine-tuning project can do.

## Installation
Follow the detailed steps below to set up everything needed to run this project.

### 1. Clone the Repository
First, clone this repository to your local machine:

```sh
$ git clone https://github.com/mukiralad/LLM_FineTuning.git
$ cd LLM_FineTuning
```

### 2. Set Up Python Environment
Ensure you have Python 3.7 or higher installed. We recommend using a virtual environment.

#### Using Virtualenv
```sh
$ python -m venv llm_finetune_env
$ source llm_finetune_env/bin/activate  # On Windows use `llm_finetune_env\Scripts\activate`
```

### 3. Install Dependencies
Install the required dependencies using `pip`:

```sh
$ pip install -r requirements.txt
```

### 4. Install Additional Tools
- [Docker](https://docs.docker.com/get-docker/): Used for containerizing applications (optional).
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git): Used for version control.

## Setup Instructions

### 1. OpenAI API Key Setup
Create an `.env` file in the root directory and add your OpenAI API key.

```sh
OPENAI_API_KEY=your_openai_api_key_here
```

**Note**: The `.env` file is included in `.gitignore` to ensure your API key remains private.

### 2. Data Preparation
- To generate `emails_data.json`, please refer to my [Fetch Emails GCP Repository](https://github.com/mukiralad/fetch-emails-gcp). This repository will help you collect the necessary email data for fine-tuning.
- Place the generated `emails_data.json` in the `data/raw` directory.

## Fine-Tuning Process

### Cost and Token Usage
The cost of fine-tuning can vary depending on the number of tokens used. In my case, fine-tuning the model for 25,176 tokens(100 emails approx.) cost approximately **$0.21**. This information can help you estimate your own costs.

### 1. Upload Training Data
First, run `train.py` to upload your training and validation data to OpenAI.

```sh
$ python src/train.py
```

This script uploads `cold_email_train.jsonl` and `cold_email_test.jsonl` to the OpenAI API, setting up files for fine-tuning.

### 2. Start Fine-Tuning
Create the fine-tuning job using the same script:

```sh
$ python src/finetune.py
```

This script will initiate the fine-tuning job and display the status. Once fine-tuning is complete, the **model ID** will be displayed in the terminal. This model ID will also be available in the **OpenAI API dashboard** for future reference.

### 3. Monitor Training Progress
To monitor the fine-tuning progress, use:

```sh
$ python src/train.py
```

The script will continuously display updates on the training process until completion.

## Usage Guide
Once the fine-tuning is complete, you can generate cold emails using `test.py`.

```sh
$ python src/test.py
```

The output email will be saved to `generated_email.txt`. This file demonstrates the power of personalization for professional outreach.

## Data Preparation
To prepare your data, ensure the following:
- **Email Data File**: Store your email data in JSON format (`emails_data.json`) and save it in `data/raw/`.
- **Training and Validation Split**: Use the `main()` function in the provided scripts to split the data into training and validation sets.

## How to Contribute
We welcome contributions to improve this project!
- **Fork** the repository.
- Create a **feature branch**.
- **Commit** your changes.
- Open a **Pull Request**.

Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Keywords
- **LLM Fine-Tuning**
- **Cold Email Generation**
- **Personalized Outreach**
- **OpenAI API**
- **Professional Communication**
- **Machine Learning for Marketing**
- **Python Email Generation**

## References
- [Fetch Emails GCP Repository](https://github.com/mukiralad/fetch-emails-gcp): To generate the `emails_data.json`.
- [OpenAI Fine-Tuning Documentation](https://platform.openai.com/docs/guides/fine-tuning): For additional details on the fine-tuning process.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Show Your Support
Feel free to share your feedback or open an issue if you have suggestions for improvement.

