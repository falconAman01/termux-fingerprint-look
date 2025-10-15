import subprocess
import time

result = subprocess.run(["termux-fingerprint"], capture_output=True, text=True)

true = """{
  "errors": [],
  "failed_attempts": 0,
  "auth_result": "AUTH_RESULT_SUCCESS"
}"""

current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
final_result = f"{current_time}\n{result.stdout}\n\n\n\n"

with open("data.log", "a") as file:
    file.write(final_result)

if result.stdout == true:
    print("Wellcome! Fingerprint match")
else:
    print("Very Bad! Fingerprint Not match")

