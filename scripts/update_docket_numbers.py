#!/usr/bin/env python3
"""
Systematic Docket Number Update Script
=====================================

This script updates docket numbers across all files in the ClaudeScotus project
based on the central docket registry. It handles:

1. Markdown files with docket references
2. Folder renaming
3. README files within case folders
4. JSON metadata files
5. Cross-references in documentation

Usage:
    python3 scripts/update_docket_numbers.py [--dry-run] [--case CASE_KEY]

Options:
    --dry-run       Show what would be changed without making changes
    --case CASE_KEY Update only specific case (e.g., students-for-fair-admissions-v-harvard)
"""

import json
import os
import re
import argparse
import shutil
from pathlib import Path

class DocketUpdater:
    def __init__(self, project_root="/home/fitz/ClaudeScotus"):
        self.project_root = Path(project_root)
        self.registry_path = self.project_root / "data/terms/2022-2023/docket_registry.json"
        self.registry = self.load_registry()
        
    def load_registry(self):
        """Load the central docket registry"""
        with open(self.registry_path, 'r') as f:
            return json.load(f)
            
    def get_cases_needing_updates(self):
        """Get cases that have verified dockets different from current"""
        updates_needed = {}
        for case_key, case_data in self.registry['cases'].items():
            if (case_data.get('verified_docket') and 
                case_data['verified_docket'] != case_data['current_docket']):
                updates_needed[case_key] = case_data
        return updates_needed
        
    def update_file_content(self, file_path, old_docket, new_docket, dry_run=False):
        """Update docket number references in a file"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Track what changes we're making
            changes = []
            
            # Pattern 1: Explicit docket number references
            pattern1 = rf'\b{re.escape(old_docket)}\b'
            if re.search(pattern1, content):
                changes.append(f"Docket number: {old_docket} -> {new_docket}")
                if not dry_run:
                    content = re.sub(pattern1, new_docket, content)
            
            # Pattern 2: Folder name references  
            old_folder = f"{old_docket}_"
            new_folder = f"{new_docket}_"
            if old_folder in content:
                changes.append(f"Folder reference: {old_folder} -> {new_folder}")
                if not dry_run:
                    content = content.replace(old_folder, new_folder)
                    
            # Pattern 3: Docket Number field updates
            pattern3 = rf'(\*\*Docket Number\*\*:?\s*)`?{re.escape(old_docket)}`?'
            if re.search(pattern3, content):
                changes.append(f"Docket field: {old_docket} -> {new_docket}")
                if not dry_run:
                    content = re.sub(pattern3, rf'\1`{new_docket}`', content)
            
            # Write changes if any were made
            if changes and not dry_run:
                with open(file_path, 'w') as f:
                    f.write(content)
                    
            return changes
            
        except Exception as e:
            return [f"Error updating {file_path}: {e}"]
    
    def rename_case_folder(self, case_data, dry_run=False):
        """Rename case folder to match new docket number"""
        old_docket = case_data['current_docket']
        new_docket = case_data['verified_docket']
        
        # Extract case slug from folder name
        old_folder_name = case_data['folder_name']
        case_slug = old_folder_name.split('_', 1)[1] if '_' in old_folder_name else old_folder_name
        new_folder_name = f"{new_docket}_{case_slug}"
        
        old_path = self.project_root / "data/terms/2022-2023/cases" / old_folder_name
        new_path = self.project_root / "data/terms/2022-2023/cases" / new_folder_name
        
        changes = []
        if old_path.exists():
            changes.append(f"Rename folder: {old_folder_name} -> {new_folder_name}")
            if not dry_run:
                shutil.move(str(old_path), str(new_path))
                # Update registry with new folder name
                case_data['folder_name'] = new_folder_name
        else:
            changes.append(f"Warning: Folder {old_folder_name} not found")
            
        return changes, new_folder_name
    
    def update_case(self, case_key, case_data, dry_run=False):
        """Update all references for a single case"""
        old_docket = case_data['current_docket']
        new_docket = case_data['verified_docket']
        
        print(f"\\n{'DRY RUN: ' if dry_run else ''}Updating {case_key}")
        print(f"  {old_docket} -> {new_docket}")
        
        all_changes = []
        
        # 1. Rename case folder
        folder_changes, new_folder_name = self.rename_case_folder(case_data, dry_run)
        all_changes.extend(folder_changes)
        
        # 2. Update main tracking files
        tracking_files = [
            "data/terms/2022-2023/prediction_tracking.md",
            "data/terms/2022-2023/case_list_with_identifiers.md", 
            "data/terms/2022-2023/opinions_tracker.md"
        ]
        
        for file_rel_path in tracking_files:
            file_path = self.project_root / file_rel_path
            if file_path.exists():
                changes = self.update_file_content(file_path, old_docket, new_docket, dry_run)
                if changes:
                    all_changes.append(f"{file_rel_path}: {', '.join(changes)}")
        
        # 3. Update case folder README and metadata
        case_folder = self.project_root / "data/terms/2022-2023/cases" / (new_folder_name if not dry_run else case_data['folder_name'])
        if case_folder.exists():
            readme_path = case_folder / "README.md"
            if readme_path.exists():
                changes = self.update_file_content(readme_path, old_docket, new_docket, dry_run)
                if changes:
                    all_changes.append(f"Case README: {', '.join(changes)}")
                    
            metadata_path = case_folder / "metadata.json"
            if metadata_path.exists():
                try:
                    with open(metadata_path, 'r') as f:
                        metadata = json.load(f)
                    
                    if metadata.get('docket_number') == old_docket:
                        all_changes.append(f"Metadata JSON: docket_number {old_docket} -> {new_docket}")
                        if not dry_run:
                            metadata['docket_number'] = new_docket
                            with open(metadata_path, 'w') as f:
                                json.dump(metadata, f, indent=2)
                except Exception as e:
                    all_changes.append(f"Error updating metadata: {e}")
        
        # 4. Update registry current_docket
        if not dry_run:
            case_data['current_docket'] = new_docket
            case_data['folder_name'] = new_folder_name
        
        # Print summary
        if all_changes:
            for change in all_changes:
                print(f"    - {change}")
        else:
            print(f"    No changes needed")
            
        return all_changes
    
    def save_registry(self):
        """Save updated registry back to file"""
        with open(self.registry_path, 'w') as f:
            json.dump(self.registry, f, indent=2)
    
    def run(self, dry_run=False, specific_case=None):
        """Run the update process"""
        updates_needed = self.get_cases_needing_updates()
        
        if not updates_needed:
            print("No docket updates needed.")
            return
            
        if specific_case:
            if specific_case not in updates_needed:
                print(f"Case '{specific_case}' does not need docket updates.")
                return
            updates_needed = {specific_case: updates_needed[specific_case]}
        
        print(f"{'DRY RUN MODE: ' if dry_run else ''}Found {len(updates_needed)} cases needing docket updates:")
        
        for case_key, case_data in updates_needed.items():
            self.update_case(case_key, case_data, dry_run)
        
        # Save registry if changes were made
        if not dry_run:
            self.save_registry()
            print(f"\\nRegistry updated with {len(updates_needed)} case changes.")
        
        print(f"\\n{'DRY RUN COMPLETE' if dry_run else 'UPDATE COMPLETE'}")

def main():
    parser = argparse.ArgumentParser(description='Update docket numbers across ClaudeScotus project')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be changed without making changes')
    parser.add_argument('--case', help='Update only specific case (use case key from registry)')
    
    args = parser.parse_args()
    
    updater = DocketUpdater()
    updater.run(dry_run=args.dry_run, specific_case=args.case)

if __name__ == "__main__":
    main()