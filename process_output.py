def replace_special_characters(file_path):
    # 定义替换规则
    replacements = {
        "&apos;": "'",
        "&quot;": "\"",
        "&amp;": "&",
        "@@ ": ""
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 按行分割内容
    lines = content.split('\n')

    # 合并属于同一段落的行
    paragraphs = []
    current_paragraph = []

    for line in lines:
        if line.startswith(('S-','T-', 'H-', 'D-', 'P-')):
            if current_paragraph:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
        current_paragraph.append(line.strip())
    
    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))

    # 替换特定段落中的内容
    new_paragraphs = []
    for paragraph in paragraphs:
        if paragraph.startswith(('T-', 'H-', 'D-')):
            for old, new in replacements.items():
                paragraph = paragraph.replace(old, new)
        new_paragraphs.append(paragraph)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_paragraphs))

    print(f"Replacements complete for file: {file_path}")

# 使用示例
file_path = 'output_fairseq.txt'  # 替换为你的文件路径
replace_special_characters(file_path)