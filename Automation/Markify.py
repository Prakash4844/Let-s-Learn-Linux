from markdownify import markdownify
import os

# Script only work in Pycharm

path = "/home/zaphkiel/Documents/Test"

for file_name in os.listdir(path):
    if file_name.endswith(".md"):
        print(file_name)
        print(f"Working on {file_name}")

        with open(os.path.join(path, file_name), "r+") as f:
            print(f'--------------Opened {f}...\n----------------')
            lines = f.readlines()

            # find the line number of the "## Quiz Question" line
            quiz_line = -1
            for i, line in enumerate(lines):
                if "## Quiz Question" in line:
                    quiz_line = i
                    break

            if quiz_line != -1:
                # insert the quiz text after the quiz question heading
                lines.insert(quiz_line + 1, "\n{{< quizdown >}}\n")
                new_text = "".join(lines)
                html = markdownify(new_text, heading_style="ATX")

                f.seek(0)
                f.write(html)
                f.truncate()
                print(f"----------------Done {f}\n-------------------")
            else:
                # if the quiz question heading is not found, skip the file
                print(f"No quiz question heading found in {f}")
