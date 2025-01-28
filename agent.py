import http.client
import json
import sys

def query_ollama(prompt):
    host = 'localhost'
    port = 11434
    endpoint = '/api/generate'

    try:
        # Create a connection to Ollama's serve
        conn = http.client.HTTPConnection(host, port)

        # Prepare the request body with the prompt
        data = {
            "model": "deepseek-r1:32b",
            "prompt": prompt,
            "stream": False
        }

        headers = {'Content-Type': 'application/json'}

        # Send POST request
        conn.request('POST', endpoint, json.dumps(data), headers)

        # Get response
        response = conn.getresponse()
        if response.status != 200:
            print(f"Error: {response.status} {response.reason}")
            return ""

        # Read and parse the response
        raw_data = response.read().decode('utf-8')
        result = json.loads(raw_data)

        # Extract and return the generated text
        conn.close()
        return result.get("response", "")

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def main():
    if len(sys.argv) > 1:
        prompt = ' '.join(sys.argv[1:])
    else:
        # If no argument, prompt user for input
        prompt = input("Enter your query: ")

    response = query_ollama(prompt)
    print("\nAI Response:")
    print(response)

if __name__ == "__main__":
    main()