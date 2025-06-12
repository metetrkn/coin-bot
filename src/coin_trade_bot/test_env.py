"""Test script to verify environment variable loading."""
import os
from dotenv import load_dotenv

def test_env_loading():
    # Load environment variables
    load_dotenv()
    
    # Get Binance credentials
    binance_api_key = os.getenv('BINANCE_API_KEY')
    binance_api_secret = os.getenv('BINANCE_API_SECRET')
    
    # Get X credentials
    x_api_key = os.getenv('X_API_KEY')
    x_api_secret = os.getenv('X_API_SECRET')
    x_access_token = os.getenv('X_ACCESS_TOKEN')
    x_access_token_secret = os.getenv('X_ACCESS_SECRET')
    
    # Print results (masking the actual values for security)
    print("\nTesting Environment Variables:")
    print("-" * 30)
    print("Binance Credentials:")
    print(f"BINANCE_API_KEY: {'*' * len(binance_api_key) if binance_api_key else 'Not found'}")
    print(f"BINANCE_API_SECRET: {'*' * len(binance_api_secret) if binance_api_secret else 'Not found'}")
    
    print("\nX (Twitter) Credentials:")
    print(f"X_API_KEY: {'*' * len(x_api_key) if x_api_key else 'Not found'}")
    print(f"X_API_SECRET: {'*' * len(x_api_secret) if x_api_secret else 'Not found'}")
    print(f"X_ACCESS_TOKEN: {'*' * len(x_access_token) if x_access_token else 'Not found'}")
    print(f"X_ACCESS_TOKEN_SECRET: {'*' * len(x_access_token_secret) if x_access_token_secret else 'Not found'}")
    
    # Test Binance connection if credentials exist
    if binance_api_key and binance_api_secret:
        print("\nTesting Binance Connection:")
        try:
            import requests
            
            # Binance spot testnet base URL
            base_url = "https://testnet.binance.vision/api/v3"
            
            # Test endpoint
            endpoint = "/ping"
            
            # Add API key to headers
            headers = {
                "X-MBX-APIKEY": binance_api_key
            }
            
            # Make test request
            response = requests.get(f"{base_url}{endpoint}", headers=headers)
            
            if response.status_code == 200:
                print("✅ Successfully connected to Binance testnet!")
            else:
                print("❌ Failed to connect to Binance testnet")
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")
                
        except Exception as e:
            print("❌ Error testing Binance connection:")
            print(str(e))
    else:
        print("\n❌ Binance credentials not found!")
    
    # Test X connection if credentials exist
    if all([x_api_key, x_api_secret, x_access_token, x_access_token_secret]):
        print("\nTesting X (Twitter) Connection:")
        try:
            import tweepy
            
            # Create authentication object
            auth = tweepy.OAuthHandler(x_api_key, x_api_secret)
            auth.set_access_token(x_access_token, x_access_token_secret)
            
            # Create API object
            api = tweepy.API(auth)
            
            # Test connection by getting user info
            user = api.verify_credentials()
            print(f"✅ Successfully connected to X (Twitter)!")
            print(f"Connected as: @{user.screen_name}")
            
        except Exception as e:
            print("❌ Error testing X connection:")
            print(str(e))
    else:
        print("\n❌ X (Twitter) credentials not found!")
        print("Please make sure your .env file contains all required X credentials:")
        print("- X_API_KEY")
        print("- X_API_SECRET")
        print("- X_ACCESS_TOKEN")
        print("- X_ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    test_env_loading() 