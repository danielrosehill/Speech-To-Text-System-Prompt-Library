#!/usr/bin/env python3
"""
Prompt Combiner Script

This script combines various text transformation prompts into a unified system prompt.
It allows users to select from categorized prompts and combines them with the basic
cleanup prompt to create custom system prompts for specific use cases.
"""

import os
import sys
from datetime import datetime
import json

# Define the base directory for the system prompts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "system-prompts")
BASIC_PROMPT_PATH = os.path.join(PROMPTS_DIR, "basic", "basic-cleanup.md")
OUTPUT_DIR = os.path.join(BASE_DIR, "custom-system-prompts")

def ensure_output_dir():
    """Ensure the output directory exists."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

def get_prompt_categories():
    """Get all prompt categories (directories) from the system-prompts folder."""
    categories = []
    for item in os.listdir(PROMPTS_DIR):
        item_path = os.path.join(PROMPTS_DIR, item)
        if os.path.isdir(item_path) and item != "basic":  # Exclude the basic folder
            categories.append(item)
    return sorted(categories)

def get_prompts_in_category(category):
    """Get all prompts in a specific category."""
    category_path = os.path.join(PROMPTS_DIR, category)
    prompts = []
    for item in os.listdir(category_path):
        if item.endswith(".md"):
            prompt_path = os.path.join(category_path, item)
            prompt_name = item[:-3]  # Remove .md extension
            prompts.append((prompt_name, prompt_path))
    return sorted(prompts)

def read_prompt_content(prompt_path):
    """Read the content of a prompt file."""
    with open(prompt_path, 'r', encoding='utf-8') as file:
        return file.read()

def list_all_prompts():
    """List all available prompts categorized by directory."""
    categories = get_prompt_categories()
    all_prompts = {}
    
    for category in categories:
        prompts = get_prompts_in_category(category)
        all_prompts[category] = [name for name, _ in prompts]
    
    return all_prompts

def display_all_prompts():
    """Display all available prompts to the user."""
    all_prompts = list_all_prompts()
    
    print("\n=== Available Prompt Categories ===")
    for i, category in enumerate(all_prompts.keys(), 1):
        print(f"{i}. {category.replace('-', ' ').title()} ({len(all_prompts[category])} prompts)")
    
    print("\nTo view prompts in a category, enter the category number.")
    print("To exit, enter 'q'.")

def display_category_prompts(category):
    """Display all prompts in a specific category."""
    prompts = get_prompts_in_category(category)
    
    print(f"\n=== Prompts in {category.replace('-', ' ').title()} ===")
    for i, (name, _) in enumerate(prompts, 1):
        print(f"{i}. {name.replace('-', ' ').title()}")
    
    return prompts

def select_prompts():
    """Interactive prompt selection process."""
    selected_prompts = []
    all_categories = get_prompt_categories()
    
    while True:
        display_all_prompts()
        choice = input("\nEnter category number, 'v' to view selected prompts, 's' to save, or 'q' to quit: ").strip().lower()
        
        if choice == 'q':
            if selected_prompts:
                save_choice = input("You have selected prompts. Do you want to save before quitting? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_combined_prompt(selected_prompts)
            print("Exiting program.")
            sys.exit(0)
        
        elif choice == 'v':
            if not selected_prompts:
                print("No prompts selected yet.")
            else:
                print("\n=== Selected Prompts ===")
                for i, (category, name, _) in enumerate(selected_prompts, 1):
                    print(f"{i}. [{category}] {name.replace('-', ' ').title()}")
        
        elif choice == 's':
            if not selected_prompts:
                print("No prompts selected. Please select at least one prompt before saving.")
            else:
                save_combined_prompt(selected_prompts)
        
        elif choice.isdigit() and 1 <= int(choice) <= len(all_categories):
            category_index = int(choice) - 1
            category = all_categories[category_index]
            prompts = display_category_prompts(category)
            
            while True:
                prompt_choice = input(f"\nEnter prompt number to select from {category}, 'b' to go back: ").strip().lower()
                
                if prompt_choice == 'b':
                    break
                
                elif prompt_choice.isdigit() and 1 <= int(prompt_choice) <= len(prompts):
                    prompt_index = int(prompt_choice) - 1
                    name, path = prompts[prompt_index]
                    
                    # Check if already selected
                    already_selected = False
                    for c, n, p in selected_prompts:
                        if p == path:
                            already_selected = True
                            print(f"Prompt '{name}' is already selected.")
                            break
                    
                    if not already_selected:
                        selected_prompts.append((category, name, path))
                        print(f"Added '{name}' to selected prompts.")
                
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid choice. Please try again.")

def save_combined_prompt(selected_prompts):
    """Combine the basic prompt with selected prompts and save to output directory."""
    ensure_output_dir()
    
    # First, read the basic cleanup prompt
    basic_prompt = read_prompt_content(BASIC_PROMPT_PATH)
    
    # Combine with selected prompts
    combined_content = basic_prompt + "\n\n"
    
    # Add metadata about which prompts were combined
    combined_content += "# Combined Prompts\n\n"
    combined_content += "This system prompt combines the following components:\n\n"
    combined_content += "1. Basic Cleanup (foundation)\n"
    
    for i, (category, name, path) in enumerate(selected_prompts, 2):
        combined_content += f"{i}. {category.replace('-', ' ').title()}: {name.replace('-', ' ').title()}\n"
    
    combined_content += "\n# Additional Transformations\n\n"
    
    # Add the content of each selected prompt
    for category, name, path in selected_prompts:
        prompt_content = read_prompt_content(path)
        # Extract just the content part (skip the title)
        content_lines = prompt_content.split('\n')
        if content_lines and content_lines[0].startswith('# '):
            # Keep the title as a secondary heading
            content_lines[0] = '#' + content_lines[0]  # Convert to subheading
        prompt_content = '\n'.join(content_lines)
        combined_content += prompt_content + "\n\n"
    
    # Generate filename based on selected prompts
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    categories = "_".join(sorted(set(category for category, _, _ in selected_prompts)))
    filename = f"combined_{categories}_{timestamp}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(combined_content)
    
    print(f"\nCombined prompt saved to: {output_path}")
    
    # Also save a JSON metadata file for reference
    metadata = {
        "timestamp": timestamp,
        "base_prompt": "basic-cleanup",
        "selected_prompts": [
            {"category": category, "name": name}
            for category, name, _ in selected_prompts
        ]
    }
    
    metadata_path = output_path.replace('.md', '.json')
    with open(metadata_path, 'w', encoding='utf-8') as file:
        json.dump(metadata, file, indent=2)
    
    print(f"Prompt metadata saved to: {metadata_path}")
    return output_path

def main():
    """Main function to run the script."""
    print("=== System Prompt Combiner ===")
    print("This script combines various text transformation prompts into a unified system prompt.")
    print("The basic cleanup prompt will be used as the foundation, and you can select additional prompts to layer on top.")
    
    select_prompts()

if __name__ == "__main__":
    main()
