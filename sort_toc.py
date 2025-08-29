#!/usr/bin/env python3
"""
LeetCode表格按难度排序脚本
按照 Easy -> Medium -> Hard 的顺序重新排列每个 ### 部分中的表格行
"""

import re
import sys
from typing import List, Tuple

def parse_table_row(line: str) -> Tuple[str, str, str, str]:
    """
    解析表格行，返回 (编号, 标题, 解决方案, 难度)
    """
    # 移除首尾的 | 并分割
    parts = [part.strip() for part in line.strip().strip('|').split('|')]
    if len(parts) >= 4:
        return parts[0], parts[1], parts[2], parts[3]
    return '', '', '', ''

def get_difficulty_order(difficulty: str) -> int:
    """
    返回难度的排序顺序：Easy=1, Medium=2, Hard=3
    """
    difficulty = difficulty.lower().strip()
    if 'easy' in difficulty:
        return 1
    elif 'medium' in difficulty:
        return 2
    elif 'hard' in difficulty:
        return 3
    else:
        return 4  # 未知难度排在最后

def format_table_row(number: str, title: str, solution: str, difficulty: str) -> str:
    """
    格式化表格行
    """
    return f"|{number}|{title}|{solution}|{difficulty}|"

def sort_leetcode_tables(content: str) -> str:
    """
    对LeetCode表格按难度排序
    """
    lines = content.split('\n')
    result_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # 检查是否是 ### 标题行
        if line.startswith('###'):
            result_lines.append(line)
            i += 1

            # 查找表格开始
            table_started = False
            table_rows = []
            header_line = ""
            separator_line = ""

            while i < len(lines):
                current_line = lines[i]

                # 如果遇到下一个 ### 或文件结束，停止处理当前section
                if current_line.startswith('###'):
                    break

                # 检查是否是表格头
                if not table_started and current_line.strip().startswith('|') and '#' in current_line:
                    table_started = True
                    header_line = current_line
                    result_lines.append(current_line)
                    i += 1

                    # 添加分隔线
                    if i < len(lines) and lines[i].strip().startswith('|---'):
                        separator_line = lines[i]
                        result_lines.append(separator_line)
                        i += 1
                    continue

                # 如果表格已开始，收集表格行
                if table_started and current_line.strip().startswith('|') and current_line.strip() != separator_line.strip():
                    # 解析表格行
                    number, title, solution, difficulty = parse_table_row(current_line)
                    if number and title and solution and difficulty:
                        table_rows.append((number, title, solution, difficulty, current_line))
                        i += 1
                        continue
                    else:
                        # 不是有效的表格行，结束表格处理
                        if table_rows:
                            # 排序并添加表格行
                            table_rows.sort(key=lambda x: (get_difficulty_order(x[3]), int(x[0]) if x[0].isdigit() else float('inf')))
                            for row in table_rows:
                                result_lines.append(row[4])  # 使用原始行格式
                            table_rows = []
                        table_started = False
                        result_lines.append(current_line)
                        i += 1
                        continue

                # 表格结束或其他行
                if table_started and table_rows:
                    # 排序并添加表格行
                    table_rows.sort(key=lambda x: (get_difficulty_order(x[3]), int(x[0]) if x[0].isdigit() else float('inf')))
                    for row in table_rows:
                        result_lines.append(row[4])  # 使用原始行格式
                    table_rows = []
                    table_started = False

                result_lines.append(current_line)
                i += 1

            # 处理最后一个表格（如果存在）
            if table_started and table_rows:
                table_rows.sort(key=lambda x: (get_difficulty_order(x[3]), int(x[0]) if x[0].isdigit() else float('inf')))
                for row in table_rows:
                    result_lines.append(row[4])  # 使用原始行格式
        else:
            result_lines.append(line)
            i += 1

    return '\n'.join(result_lines)

def main():
    """
    主函数
    """
    if len(sys.argv) != 2:
        print("Usage: python sort_toc.py <input_file>")
        print("Example: python sort_toc.py README.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace('.md', '_sorted.md') if input_file.endswith('.md') else input_file + '_sorted'

    try:
        # 读取文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 排序表格
        sorted_content = sort_leetcode_tables(content)

        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sorted_content)

        print(f"✅ 排序完成！")
        print(f"📁 输入文件: {input_file}")
        print(f"📁 输出文件: {output_file}")
        print(f"📊 排序规则: Easy → Medium → Hard")

    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 错误：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
