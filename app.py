import time
import traceback
from memory_profiler import memory_usage

def run_user_code(user_code):
    def wrapped():
        exec(user_code)

    start_time = time.time()

    try:
        mem_usage = memory_usage(wrapped, max_usage=True)
        execution_time = time.time() - start_time

        return {
            "status": "success",
            "execution_time": execution_time,
            "memory_usage": mem_usage,
            "error": None
        }

    except Exception:
        execution_time = time.time() - start_time
        return {
            "status": "error",
            "execution_time": execution_time,
            "memory_usage": None,
            "error": traceback.format_exc()
        }

if __name__ == "__main__":
    print("Shadow Compile AI Prototype v2")
    print("Paste your Python code below (type END on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_code = "\n".join(lines)
    result = run_user_code(user_code)

    print("\n--- RESULT ---")
    print("Status:", result["status"])
    print("Execution Time:", round(result["execution_time"], 6), "seconds")

    if result["memory_usage"]:
        print("Memory Usage:", result["memory_usage"], "MiB")

    if result["error"]:
        print("\nError Detected:")
        print(result["error"])
