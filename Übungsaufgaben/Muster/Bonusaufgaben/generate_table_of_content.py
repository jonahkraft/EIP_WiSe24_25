import os


def main():
    output = "# Inhaltsverzeichnis\n\n"
    inside_codeblock = False  # Variable, um sich zu merken, ob man gerade in einem Codeblock ist
    cwd = os.getcwd()  # Die Datei ist darauf ausgelegt, in demselben Ordner wie die Markdown-Dateien zu sein. Ansonsten hier relativen Pfad angeben.

    for i, f in enumerate(sorted(os.listdir(cwd))):

        if f.startswith("00") or not f[0].isdigit():  # Das Inhaltsverzeichnis selbst und ggf. versteckte Dateien sollten ignoriert werden
            continue

        os.chdir(cwd)
        with open(f) as file:
            output += f"## {file.readline().strip().strip("#").strip()}\n\n"  # Titel
            output += f"> [Link]({f})\n\n"  # Link

            # Bullet points

            for line in file:

                if line.startswith("```python"):
                    inside_codeblock = True
                elif line.startswith("```") and not line.startswith("```python"):
                    inside_codeblock = False

                if not inside_codeblock:
                    if (line.startswith("#") or line.startswith("##")) and not line.startswith("###"):
                        help_ = line.replace("#", "")
                        output += f"- {help_.strip()}\n"

            output += "\n\n"

    with open("00_inhaltsverzeichnis.md", "w") as file:
        file.write(output)


if __name__ == '__main__':
    main()
