#!/usr/bin/env python3
"""
Script to update system prompts in the flat-structure folder using Llama 3.2.
This script adds workflow and output formatting instructions to each system prompt.
"""

import os
import glob
import time
import re
from ollama import Client

def main():
    # Initialize Ollama client
    client = Client()
    
    # Path to flat-structure directory
    flat_structure_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flat-structure")
    
    # Get all markdown files
    md_files = glob.glob(os.path.join(flat_structure_dir, "*.md"))
    
    # Counter for tracking progress
    total_files = len(md_files)
    processed_files = 0
    
    print(f"Found {total_files} markdown files to process.")
    
    # Process each file
    for file_path in md_files:
        file_name = os.path.basename(file_path)
        
        # Skip README files
        if "README" in file_name.upper():
            print(f"Skipping README file: {file_name}")
            processed_files += 1
            continue
        
        print(f"Processing ({processed_files+1}/{total_files}): {file_name}")
        
        # Read the current system prompt
        with open(file_path, 'r') as f:
            current_prompt = f.read()
        
        # Skip if the file is empty
        if not current_prompt.strip():
            print(f"Skipping empty file: {file_name}")
            processed_files += 1
            continue
        
        # Create the instruction for Llama
        instruction = f"""
        I have a system prompt that needs to be updated to include clear workflow and output formatting instructions with consistent person references.
        
        Here is the current system prompt:
        
        ```
        {current_prompt}
        ```
        
        Please rewrite this system prompt to explicitly include:
        
        1. A clear workflow instruction that states:
           - "The user will provide text" (always refer to the user in the third person)
           - "You will apply the transformation described in the prompt" (always address the AI assistant in the second person)
           - "You will return the edited/transformed text" (always address the AI assistant in the second person)
        
        2. Output formatting instruction that specifies:
           - "Return only the transformed text"
           - "Do not add any commentary before or after the output"
           - "Do not include phrases like 'Here's the transformed text:' or 'I've applied the changes:'"
        
        IMPORTANT: 
        - Always refer to the user in the third person (e.g., "The user will provide text...")
        - Always address the AI assistant in the second person (e.g., "You will apply the transformation...")
        - Never use first-person language for the AI (e.g., do NOT use "I will apply...")
        - Never use second-person language for the user (e.g., do NOT use "You will provide...")
        
        Keep the original transformation instructions intact, just add these workflow and formatting instructions with the correct person references.
        Return only the updated system prompt, nothing else. Do not include phrases like "Here is the rewritten system prompt:" or any other introductory or concluding text.
        """
        
        # Call Llama 3.2 to update the prompt
        try:
            response = client.chat(
                model="llama3.2",
                messages=[{"role": "user", "content": instruction}],
                stream=False
            )
            
            # Extract the updated prompt from the response
            updated_prompt = response['message']['content'].strip()
            
            # Clean up the response - remove any introductory or concluding text
            # Remove lines like "Here is the rewritten system prompt:" or "I hope this helps!"
            updated_prompt = re.sub(r'^Here is the rewritten system prompt:\s*\n+', '', updated_prompt)
            updated_prompt = re.sub(r'^Here\'s the updated system prompt:\s*\n+', '', updated_prompt)
            updated_prompt = re.sub(r'\n+I hope this helps!.*$', '', updated_prompt)
            updated_prompt = re.sub(r'\n+Let me know if you need any adjustments!.*$', '', updated_prompt)
            
            # Remove any markdown code block markers that might have been added
            updated_prompt = re.sub(r'^```md\s*\n', '', updated_prompt)
            updated_prompt = re.sub(r'^```markdown\s*\n', '', updated_prompt)
            updated_prompt = re.sub(r'\n```\s*$', '', updated_prompt)
            
            # Write the updated prompt back to the file
            with open(file_path, 'w') as f:
                f.write(updated_prompt)
            
            print(f"✓ Updated: {file_name}")
            
            # Add a small delay to avoid overwhelming the API
            time.sleep(0.5)
            
        except Exception as e:
            print(f"✗ Error processing {file_name}: {str(e)}")
        
        processed_files += 1
        
    print(f"\nCompleted! {processed_files} files processed.")

if __name__ == "__main__":
    main()
