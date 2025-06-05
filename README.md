Transformer-MarianMT
--------------------

This project fine-tunes a pre-trained MarianMT model for English to Vietnamese translation using Hugging Face Transformers.

Requirements:
- transformers
- torch
- sentencepiece

Install dependencies:

    pip install transformers torch sentencepiece

Usage:

1. Download the script: NLP_T.py

2. Prepare the training folder:
   Create a folder named TRAIN_INFO and make sure it contains your training and validation files.

3. Set the folder path inside the script:
   Example:

       model_path = r"C:\Users\XOX\Downloads\NLP_T"

4. Run the script:

       python NLP_T.py

Notes:
- Ensure the TRAIN_INFO folder contains correctly formatted data.
- The script uses MarianMTModel and Trainer from Hugging Face.


