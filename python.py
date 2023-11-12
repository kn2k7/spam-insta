import requests

def send_report(user_id):
    url = f"https://api.instagram.com/users/{user_id}/report"
    payload = {
        "reason": "spam",
        "description": "This user is repeatedly sending spam messages."
    }
    headers = {
        "Authorization": "Bearer <access_token>"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Report sent successfully.")
    else:
        print("Failed to send report.")

user_id = "<user_id>"
send_report(user_id)
