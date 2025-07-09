#!/usr/bin/env python3
"""
Supreme Court Case Document Collection Script
Triggered by Claude Code hooks when new case folders are created
"""

import os
import json
import sys
import requests
from pathlib import Path
import time
from datetime import datetime

# Configuration
COURTLISTENER_TOKEN = "cc8cf79b1d5393f6e71126830caab5fcd57de76b"
COURTLISTENER_BASE_URL = "https://www.courtlistener.com/api/rest/v4/"
RATE_LIMIT_DELAY = 4  # seconds between requests (under 1000/hour limit)

class SupremeCourtDataCollector:
    def __init__(self, case_path):
        self.case_path = Path(case_path)
        self.case_name = self.case_path.name
        self.headers = {
            "Authorization": f"Token {COURTLISTENER_TOKEN}",
            "Content-Type": "application/json"
        }
        self.collected_documents = {}
        
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def parse_case_info(self):
        """Extract case information from folder name"""
        # Format: 21-432_arellano-v-mcdonough
        parts = self.case_name.split('_')
        if len(parts) >= 2:
            docket_number = parts[0]
            case_title = parts[1].replace('-', ' ').title()
            return docket_number, case_title
        return None, None
    
    def query_courtlistener(self, endpoint, params=None):
        """Make API request to CourtListener"""
        url = f"{COURTLISTENER_BASE_URL}{endpoint}"
        try:
            self.log(f"Querying: {url}")
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            time.sleep(RATE_LIMIT_DELAY)  # Respect rate limits
            return response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"API Error: {e}")
            return None
    
    def collect_documents(self):
        """Main collection process for all 8 documents"""
        docket_number, case_title = self.parse_case_info()
        if not docket_number:
            self.log(f"Could not parse case info from {self.case_name}")
            return
        
        self.log(f"Starting document collection for {case_title} ({docket_number})")
        
        # 1. Find the case in CourtListener
        case_data = self.find_supreme_court_case(docket_number)
        if not case_data:
            self.log(f"Case not found in CourtListener: {docket_number}")
            return
        
        self.log(f"Found case: {case_data.get('case_name', 'Unknown')}")
        
        # 2. Collect each document type
        collection_methods = [
            ("lower_court_opinion", self.collect_lower_court_opinion),
            ("cert_petition", self.collect_cert_petition),
            ("cert_opposition", self.collect_cert_opposition),
            ("cert_grant", self.collect_cert_grant),
            ("petitioner_brief", self.collect_petitioner_brief),
            ("respondent_brief", self.collect_respondent_brief),
            ("oral_argument", self.collect_oral_argument),
            ("supreme_court_opinion", self.collect_supreme_court_opinion)
        ]
        
        for doc_type, method in collection_methods:
            self.log(f"Collecting {doc_type}...")
            try:
                result = method(case_data)
                self.collected_documents[doc_type] = result
                if result:
                    self.log(f"✅ {doc_type} collected successfully")
                else:
                    self.log(f"❌ {doc_type} not available")
            except Exception as e:
                self.log(f"❌ Error collecting {doc_type}: {e}")
                self.collected_documents[doc_type] = None
        
        # 3. Create metadata.json
        self.create_metadata(case_data)
        
        # 4. Update README.md with collection status
        self.update_readme()
        
        self.log(f"Document collection completed for {case_title}")
    
    def find_supreme_court_case(self, docket_number):
        """Find case in CourtListener by docket number"""
        params = {
            "court": "scotus",
            "docket_number": docket_number
        }
        
        result = self.query_courtlistener("dockets/", params)
        if result and result.get("results"):
            return result["results"][0]
        return None
    
    def collect_lower_court_opinion(self, case_data):
        """Collect lower court opinion (Document 0)"""
        # Create folder structure
        lower_court_path = self.case_path / "lower_court"
        lower_court_path.mkdir(parents=True, exist_ok=True)
        
        # This would require additional API calls to find the lower court case
        # For now, create placeholder
        placeholder_path = lower_court_path / "lower_court_opinion.pdf"
        with open(placeholder_path, 'w') as f:
            f.write("# Lower Court Opinion\n\nTo be collected from original court records.")
        
        return {
            "type": "lower_court_opinion",
            "path": str(placeholder_path),
            "status": "placeholder_created",
            "timestamp": time.time()
        }
    
    def collect_cert_petition(self, case_data):
        """Collect cert petition (Document 1)"""
        return self.collect_brief_document(case_data, "cert_petition", "cert_stage")
    
    def collect_cert_opposition(self, case_data):
        """Collect cert opposition (Document 2)"""
        return self.collect_brief_document(case_data, "cert_opposition", "cert_stage")
    
    def collect_cert_grant(self, case_data):
        """Collect cert grant order (Document 3)"""
        return self.collect_brief_document(case_data, "cert_grant", "cert_stage")
    
    def collect_petitioner_brief(self, case_data):
        """Collect petitioner brief on merits (Document 4)"""
        return self.collect_brief_document(case_data, "petitioner_brief", "briefs")
    
    def collect_respondent_brief(self, case_data):
        """Collect respondent brief on merits (Document 5)"""
        return self.collect_brief_document(case_data, "respondent_brief", "briefs")
    
    def collect_brief_document(self, case_data, doc_type, folder_name):
        """Generic method to collect brief documents"""
        folder_path = self.case_path / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Try to find the document in CourtListener
        docket_id = case_data.get("id")
        if docket_id:
            # Query for docket entries that might contain briefs
            params = {"docket": docket_id}
            result = self.query_courtlistener("docket-entries/", params)
            
            if result and result.get("results"):
                # Look for relevant document in docket entries
                for entry in result["results"]:
                    description = entry.get("description", "").lower()
                    if self.matches_document_type(description, doc_type):
                        # Found matching document
                        file_path = folder_path / f"{doc_type}.pdf"
                        if self.download_docket_entry(entry, file_path):
                            return {
                                "type": doc_type,
                                "path": str(file_path),
                                "status": "collected",
                                "timestamp": time.time(),
                                "description": entry.get("description")
                            }
        
        # If not found, create placeholder
        placeholder_path = folder_path / f"{doc_type}.pdf"
        with open(placeholder_path, 'w') as f:
            f.write(f"# {doc_type.replace('_', ' ').title()}\n\nDocument not yet available in CourtListener.")
        
        return {
            "type": doc_type,
            "path": str(placeholder_path),
            "status": "placeholder_created",
            "timestamp": time.time()
        }
    
    def matches_document_type(self, description, doc_type):
        """Check if docket entry description matches document type"""
        type_keywords = {
            "cert_petition": ["petition", "certiorari", "cert"],
            "cert_opposition": ["opposition", "response", "brief in opposition"],
            "cert_grant": ["granted", "certiorari granted"],
            "petitioner_brief": ["petitioner", "brief for petitioner"],
            "respondent_brief": ["respondent", "brief for respondent"]
        }
        
        keywords = type_keywords.get(doc_type, [])
        return any(keyword in description for keyword in keywords)
    
    def download_docket_entry(self, entry, file_path):
        """Download a docket entry document"""
        # CourtListener API structure for docket entries
        # This would need to be implemented based on actual API structure
        return False  # Placeholder
    
    def collect_oral_argument(self, case_data):
        """Collect oral argument transcript/audio (Document 6)"""
        oral_arg_path = self.case_path / "oral_arguments"
        oral_arg_path.mkdir(parents=True, exist_ok=True)
        
        docket_id = case_data.get("id")
        params = {"docket": docket_id}
        
        result = self.query_courtlistener("oral-arguments/", params)
        if result and result.get("results"):
            oral_arg = result["results"][0]
            files_downloaded = []
            
            # Download audio file
            audio_url = oral_arg.get("local_path_mp3")
            if audio_url:
                audio_path = oral_arg_path / "oral_argument.mp3"
                if self.download_file(audio_url, audio_path):
                    files_downloaded.append(str(audio_path))
            
            # Download transcript
            transcript_url = oral_arg.get("local_path_original_file")
            if transcript_url:
                transcript_path = oral_arg_path / "transcript.pdf"
                if self.download_file(transcript_url, transcript_path):
                    files_downloaded.append(str(transcript_path))
            
            if files_downloaded:
                return {
                    "type": "oral_argument",
                    "files": files_downloaded,
                    "status": "collected",
                    "timestamp": time.time()
                }
        
        # Create placeholder
        placeholder_path = oral_arg_path / "oral_argument_placeholder.txt"
        with open(placeholder_path, 'w') as f:
            f.write("# Oral Argument\n\nAudio and transcript to be collected from CourtListener.")
        
        return {
            "type": "oral_argument",
            "path": str(placeholder_path),
            "status": "placeholder_created",
            "timestamp": time.time()
        }
    
    def collect_supreme_court_opinion(self, case_data):
        """Collect Supreme Court opinion (Document 7)"""
        opinions_path = self.case_path / "opinions"
        opinions_path.mkdir(parents=True, exist_ok=True)
        
        docket_id = case_data.get("id")
        params = {"docket": docket_id}
        
        result = self.query_courtlistener("opinion-clusters/", params)
        if result and result.get("results"):
            cluster = result["results"][0]
            cluster_id = cluster.get("id")
            
            # Get detailed cluster information
            cluster_detail = self.query_courtlistener(f"opinion-clusters/{cluster_id}/")
            if cluster_detail:
                opinions = cluster_detail.get("sub_opinions", [])
                downloaded_opinions = []
                
                for opinion in opinions:
                    opinion_type = opinion.get("type", "unknown")
                    filename = f"{opinion_type}_opinion.pdf"
                    file_path = opinions_path / filename
                    
                    # Try to download opinion
                    if opinion.get("local_path"):
                        if self.download_file(opinion["local_path"], file_path):
                            downloaded_opinions.append({
                                "type": opinion_type,
                                "author": opinion.get("author"),
                                "path": str(file_path)
                            })
                    else:
                        # Create text version from plain text
                        if opinion.get("plain_text"):
                            with open(file_path.with_suffix('.txt'), 'w') as f:
                                f.write(opinion["plain_text"])
                            downloaded_opinions.append({
                                "type": opinion_type,
                                "author": opinion.get("author"),
                                "path": str(file_path.with_suffix('.txt'))
                            })
                
                if downloaded_opinions:
                    return {
                        "type": "supreme_court_opinion",
                        "opinions": downloaded_opinions,
                        "status": "collected",
                        "timestamp": time.time()
                    }
        
        # Create placeholder
        placeholder_path = opinions_path / "supreme_court_opinion.txt"
        with open(placeholder_path, 'w') as f:
            f.write("# Supreme Court Opinion\n\nOpinion to be collected from CourtListener.")
        
        return {
            "type": "supreme_court_opinion",
            "path": str(placeholder_path),
            "status": "placeholder_created",
            "timestamp": time.time()
        }
    
    def download_file(self, url, local_path):
        """Download file from URL to local path"""
        if not url.startswith("http"):
            url = f"https://www.courtlistener.com{url}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            time.sleep(RATE_LIMIT_DELAY)
            self.log(f"Downloaded: {local_path}")
            return True
        except Exception as e:
            self.log(f"Download failed for {url}: {e}")
            return False
    
    def create_metadata(self, case_data):
        """Create metadata.json with case information"""
        metadata = {
            "case_name": case_data.get("case_name"),
            "docket_number": case_data.get("docket_number"),
            "term": self.extract_term_from_path(),
            "collection_date": time.time(),
            "collection_timestamp": datetime.now().isoformat(),
            "documents": self.collected_documents,
            "courtlistener_id": case_data.get("id"),
            "courtlistener_url": case_data.get("absolute_url"),
            "status": "documents_collected"
        }
        
        metadata_path = self.case_path / "metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        self.log(f"Created metadata: {metadata_path}")
    
    def update_readme(self):
        """Update README.md with collection status"""
        readme_path = self.case_path / "README.md"
        
        # Read existing README or create new one
        if readme_path.exists():
            with open(readme_path, 'r') as f:
                content = f.read()
        else:
            content = f"# {self.case_name}\n\n"
        
        # Add collection status
        status_section = "\n## Document Collection Status\n\n"
        
        document_names = {
            "lower_court_opinion": "Lower Court Opinion",
            "cert_petition": "Cert Petition",
            "cert_opposition": "Cert Opposition",
            "cert_grant": "Cert Grant",
            "petitioner_brief": "Petitioner Brief",
            "respondent_brief": "Respondent Brief",
            "oral_argument": "Oral Argument",
            "supreme_court_opinion": "Supreme Court Opinion"
        }
        
        for doc_type, doc_name in document_names.items():
            doc_info = self.collected_documents.get(doc_type)
            if doc_info and doc_info.get("status") == "collected":
                status_section += f"- ✅ {doc_name}\n"
            elif doc_info and doc_info.get("status") == "placeholder_created":
                status_section += f"- ⏳ {doc_name} (placeholder)\n"
            else:
                status_section += f"- ❌ {doc_name}\n"
        
        status_section += f"\n**Collection Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        status_section += f"**Collection Script**: collect_case_documents.py\n"
        
        # Update README
        if "## Document Collection Status" in content:
            # Replace existing status section
            parts = content.split("## Document Collection Status")
            content = parts[0] + status_section
        else:
            content += status_section
        
        with open(readme_path, 'w') as f:
            f.write(content)
        
        self.log(f"Updated README: {readme_path}")
    
    def extract_term_from_path(self):
        """Extract Supreme Court term from file path"""
        path_parts = self.case_path.parts
        for part in path_parts:
            if part.startswith("20") and "-" in part:
                return part
        return "unknown"

def main():
    """Main function called by hook"""
    # Get case path from stdin (hook input) or command line
    case_path = None
    
    if not sys.stdin.isatty():
        # Called by hook - read JSON from stdin
        try:
            hook_data = json.load(sys.stdin)
            # Extract file path from hook data
            if "payload" in hook_data:
                case_path = hook_data["payload"].get("file_path")
        except:
            pass
    
    # Fallback to command line argument
    if not case_path and len(sys.argv) > 1:
        case_path = sys.argv[1]
    
    # Final fallback to current directory
    if not case_path:
        case_path = os.getcwd()
    
    # Extract case folder from path
    if "cases/" in case_path:
        # Remove README.md from path if present
        if case_path.endswith("README.md"):
            case_path = os.path.dirname(case_path)
        
        # Extract just the case folder
        case_folder = case_path.split("cases/")[1].split("/")[0]
        base_path = case_path.split("cases/")[0]
        full_case_path = os.path.join(base_path, "cases", case_folder)
    else:
        full_case_path = case_path
    
    print(f"Starting document collection for: {full_case_path}")
    
    collector = SupremeCourtDataCollector(full_case_path)
    collector.collect_documents()

if __name__ == "__main__":
    main()