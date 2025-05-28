"""Test script to verify environment variable loading."""
import os
from dotenv import load_dotenv

def test_env_loading():
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    # Print results (masking the actual values for security)
    print("\nTesting Environment Variables:")
    print("-" * 30)
    print(f"BINANCE_API_KEY: {'*' * len(api_key) if api_key else 'Not found'}")
    print(f"BINANCE_API_SECRET: {'*' * len(api_secret) if api_secret else 'Not found'}")
    # Check if credentials are loaded
    if api_key and api_secret:
        print("\n✅ Environment variables loaded successfully!")
        
        # Test Binance API connection
        try:
            import requests
            
            # Binance spot testnet base URL
            base_url = "https://testnet.binance.vision/api/v3"
            
            # Test endpoint
            endpoint = "/ping"
            
            # Add API key to headers
            headers = {
                "X-MBX-APIKEY": api_key
            }
            
            # Make test request
            response = requests.get(f"{base_url}{endpoint}", headers=headers)
            
            if response.status_code == 200:
                print("\n✅ Successfully connected to Binance testnet!")
            else:
                print("\n❌ Failed to connect to Binance testnet")
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")
                
        except Exception as e:
            print("\n❌ Error testing Binance connection:")
            print(str(e))
            
    else:
        print("\n❌ Environment variables not found!")
        print("Please make sure your .env file exists in the root directory")
        print("and contains BINANCE_API_KEY and BINANCE_API_SECRET")

if __name__ == "__main__":
    test_env_loading() 