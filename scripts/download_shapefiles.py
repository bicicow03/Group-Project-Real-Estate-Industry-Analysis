import requests
import os
import zipfile

def download_file(url, filename):
    """Download file from URL"""
    
    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded {filename}")

def extract_zip(zip_path, extract_to):
    """Extract zip file to directory"""
    
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")

def download_essential_shapefiles():
    """
    Download essential shapefiles for geospatial visualisation and analysis:
    - SA2 boundaries (required for population/income analysis)
    - Suburb boundaries (for property visualization)
    """
    
    # Create data directory
    os.makedirs('data/shapefiles', exist_ok=True)
    
    # Essential files for Week 1-2
    downloads = {
        # SA2 boundaries - Required for project SA2 analysis
        'SA2_2021_AUST_GDA2020.zip':'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip',
        
        # Suburb boundaries - For property mapping visualization
        'SAL_2021_AUST_GDA2020.zip':'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SAL_2021_AUST_GDA2020_SHP.zip'
    }
    
    for filename, url in downloads.items():
        try:
            # Download
            filepath = os.path.join('data/shapefiles', filename)
            download_file(url, filepath)
            
            # Extract
            extract_dir = os.path.join('data/shapefiles', filename.replace('.zip', ''))
            extract_zip(filepath, extract_dir)
            
            # Remove zip file to save space
            os.remove(filepath)
            
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
    
    print("\nDownloads complete!")
    print("Files saved to: data/shapefiles/")

if __name__ == "__main__":
    download_essential_shapefiles()