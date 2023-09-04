import argparse
import google.generativeai as palm


def get_fix(path, apikey):

    # required prompt
    prompt = '''
    You are an expert at analyzing logs.
    You have to summarize the content log content given to you and
    suggest ways to fix errors if possible. Ignore any warnings
    that you see. If the file is not a typical log file or if the file is
    a program file in any programming language then inform the user
    that the file provided was not a log file.
    '''
    palm.configure(api_key=apikey)

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    try:
        with open(path, 'r') as file:
            prompt += "\nAnalyze the following content:\n" + file.read()
            file.close()
            ans = palm.generate_text(model=model, prompt=prompt,
                 temperature=0, max_output_tokens=800)
            print(ans.candidates[0]['output'])
    except FileNotFoundError:
        print("Unable to find specified file. Use pwd for referrence.")


parser = argparse.ArgumentParser(description="Get file name")
parser.add_argument('filename')
parser.add_argument('apikey')
# Arguments
args = parser.parse_args()
get_fix(args.filename, args.apikey)
