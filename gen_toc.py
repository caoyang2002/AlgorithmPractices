#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_chinese_title(text):
    """从标题中提取中文字符和有意义的标题"""
    # 移除开头的#号和空格
    text = text.lstrip('#').strip()

    # 处理链接格式 [title](url)
    link_match = re.search(r'\[([^\]]+)\](?:\([^)]*\))?', text)
    if link_match:
        title_text = link_match.group(1)
    else:
        title_text = text

    # 去除开头的数字、点、空格
    title_text = re.sub(r'^[\d\.\s]+', '', title_text).strip()

    # 提取中文字符和基本标点
    chinese_parts = []
    # 分割文本，保留中文、英文字母、空格和基本标点
    parts = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+|\s+|[，。！？、：；""''（）\[\]{}]', title_text)

    result = ""
    for part in parts:
        if re.match(r'[\u4e00-\u9fff]', part):  # 中文
            result += part
        elif re.match(r'[a-zA-Z]', part):  # 英文单词
            if result and not result.endswith(' '):
                result += ' '
            result += part
        elif part in '，。！？、：；""''（）':  # 中文标点
            result += part
        elif part.strip() == '':  # 空格
            if result and not result.endswith(' '):
                result += ' '

    result = result.strip()

    # 如果没有中文，尝试提取英文部分
    if not result:
        english_match = re.search(r'[a-zA-Z][a-zA-Z\s]*', title_text)
        if english_match:
            result = english_match.group().strip()

    # 如果还是空，返回清理后的原标题
    if not result:
        result = re.sub(r'[\[\]()（）]', '', title_text).strip()

    return result or title_text

def extract_first_heading(file_path):
    """从markdown文件中提取第一个#标题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    return extract_chinese_title(line)
    except Exception as e:
        print(f"❌ 读取文件 {file_path} 出错: {e}")
        return file_path.stem

    return file_path.stem

def get_directory_display_name(dir_path):
    """获取目录的显示名称"""
    index_file = dir_path / "index.md"
    if index_file.exists():
        title = extract_first_heading(index_file)
        return title
    else:
        # 如果没有index.md，使用目录名处理
        dir_name = dir_path.name
        # 去除数字、下划线等前缀
        display_name = re.sub(r'^[\d_]+', '', dir_name).replace('_', ' ').strip()
        return display_name or dir_name

def collect_files_recursive(dir_path, src_path, current_level=1, max_level=10):
    """递归收集目录中的文件，按层级组织"""
    if current_level > max_level:
        return {}

    result = {
        'display_name': get_directory_display_name(dir_path),
        'index_file': None,
        'files': [],
        'subdirs': {}
    }

    # 收集当前目录下的文件
    md_files = []
    subdirs = []

    for item in dir_path.iterdir():
        if item.is_file() and item.suffix == '.md':
            md_files.append(item)
        elif item.is_dir() and not item.name.startswith('.'):
            subdirs.append(item)

    # 处理markdown文件
    for md_file in md_files:
        relative_path = md_file.relative_to(src_path)
        file_title = extract_first_heading(md_file)

        # 确保文件标题不是链接格式
        if file_title.startswith('[') and '](' in file_title:
            # 如果标题本身就是链接格式，只提取标题部分
            match = re.search(r'\[([^\]]+)\]', file_title)
            if match:
                file_title = extract_chinese_title(match.group(1))

        if md_file.name == "index.md":
            result['index_file'] = (file_title, str(relative_path))
        else:
            result['files'].append((file_title, str(relative_path)))

    # 递归处理子目录
    for subdir in subdirs:
        subdir_data = collect_files_recursive(subdir, src_path, current_level + 1, max_level)
        if subdir_data['index_file'] or subdir_data['files'] or subdir_data['subdirs']:
            result['subdirs'][subdir.name] = subdir_data

    return result

def write_directory_content(f, dir_data, indent_level=0):
    """递归写入目录内容"""
    indent = "  " * indent_level

    # 写入index.md文件（如果存在）
    if dir_data['index_file']:
        title, path = dir_data['index_file']
        f.write(f"{indent}- [{title}]({path})\n")

    # 写入当前目录的其他文件
    if dir_data['files']:
        sorted_files = sorted(dir_data['files'], key=lambda x: x[1])
        for file_title, file_path in sorted_files:
            f.write(f"{indent}  - [{file_title}]({file_path})\n")

    # 递归写入子目录
    if dir_data['subdirs']:
        sorted_subdirs = sorted(dir_data['subdirs'].items(), key=lambda x: x[0])
        for subdir_name, subdir_data in sorted_subdirs:
            write_directory_content(f, subdir_data, indent_level + 1)

def generate_index():
    """遍历src下的所有子目录，生成总索引"""
    src_path = Path("src")
    if not src_path.exists():
        print("❌ src 目录不存在")
        return

    # 处理根目录下的.md文件
    root_files = []
    directories = {}

    for item in src_path.iterdir():
        if item.is_file() and item.suffix == '.md' and item.name != 'toc.md':
            title = extract_first_heading(item)
            root_files.append((title, item.name))
        elif item.is_dir() and not item.name.startswith('.'):
            print(f"📁 处理目录: {item.name}")
            dir_data = collect_files_recursive(item, src_path)
            if dir_data['index_file'] or dir_data['files'] or dir_data['subdirs']:
                directories[item.name] = dir_data
                print(f"   显示名称: {dir_data['display_name']}")

    # 生成 toc.md 文件
    with open("src/toc.md", "w", encoding="utf-8") as f:
        f.write("# 算法练习\n")
        f.write("\n")

        # 写入根目录文件
        if root_files:
            for file_title, file_path in sorted(root_files, key=lambda x: x[1]):
                f.write(f"- [{file_title}]({file_path})\n")

        # 按目录名排序处理各个目录
        for dir_name in sorted(directories.keys()):
            dir_data = directories[dir_name]

            # 写入目录标题（一级标题）
            f.write(f"# {dir_data['display_name']}\n")

            # 写入目录内容（递归处理所有层级）
            write_directory_content(f, dir_data, 0)

            # 如果目录为空
            if not dir_data['index_file'] and not dir_data['files'] and not dir_data['subdirs']:
                f.write("*该目录暂无文件*\n")
            f.write("\n")
        # 计算总文件数（递归统计）
        def count_files(data):
            count = 0
            if data['index_file']:
                count += 1
            count += len(data['files'])
            for subdir_data in data['subdirs'].values():
                count += count_files(subdir_data)
            return count

        total_files = sum(count_files(data) for data in directories.values()) + len(root_files)
        f.write(f"---\n**统计**: 共 {len(directories)} 个目录，{total_files} 个文件\n")

def main():
    try:
        print("🚀 开始生成总索引...")
        generate_index()
        print("✅ 总索引生成完成！文件保存在 src/toc.md")
    except Exception as e:
        print(f"❌ 生成过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
