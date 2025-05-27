import re


def convert_to_markdown(text):
    if re.match(r'^\s*#{1,6}\s', text):
        return text

    text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', text)
    text = re.sub(r'__(.*?)__', r'**\1**', text)
    text = re.sub(r'_(.*?)_', r'*\1*', text)
    text = re.sub(r'\*(.*?)\*', r'*\1*', text)
    text = re.sub(r'`(.*?)`', r'`\1`', text)

    if re.match(r'^\s*[\*\-]\s+', text):
        return text

    return text


def live_text_to_readme():
    print("Enter your text (type 'exit' to quit):")

    with open("README.md", "w", encoding="utf-8") as file:
        while True:
            line = input()
            if line.lower() == 'exit':
                print("Saved all input to README.md")
                break
            md_line = convert_to_markdown(line)
            file.write(md_line + "\n")
            print("Markdown:", md_line)


if __name__ == "__main__":
    live_text_to_readme()
