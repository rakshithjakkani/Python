from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    art = '''
 _   _      _ _          ____ _                 _                 
| | | | ___| | | ___    / ___| | ___  _   _  __| |                
| |_| |/ _ \ | |/ _ \  | |   | |/ _ \| | | |/ _` |                
|  _  |  __/ | | (_) | | |___| | (_) | |_| | (_| |                
|_| |_|\___|_|_|\___/   \____|_|\___/ \__,_|\__,_|                
   / \   _ __ ___ | |__   __ _ ___ ___  __ _  __| | ___  _ __ ___ 
  / _ \ | '_ ` _ \| '_ \ / _` / __/ __|/ _` |/ _` |/ _ \| '__/ __|
 / ___ \| | | | | | |_) | (_| \__ \__ \ (_| | (_| | (_) | |  \__ \
/_/   \_\_| |_| |_|_.__/ \__,_|___/___/\__,_|\__,_|\___/|_|  |___/        
    '''
    return f"<pre>{art}</pre>"  # Use <pre> for preserving ASCII art formatting


# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Listen on all IPs, port 5000
