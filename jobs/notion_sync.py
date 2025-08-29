import os, requests
msg = {"text": "✅ Nightly Notion sync ran."}
hook = os.getenv("SLACK_WEBHOOK_URL")
if hook: requests.post(hook, json=msg, timeout=10)
print("ok")
