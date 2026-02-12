import argparse
import os
import xml.etree.ElementTree as ET
import re

# 注册 SVG 命名空间，防止保存时出现 ns0: 前缀
ET.register_namespace('', "http://www.w3.org/2000/svg")
NS = {'svg': 'http://www.w3.org/2000/svg'}

def parse_style_string(style_str):
    """
    解析 style="fill:red; stroke:black" 格式的字符串为字典
    """
    styles = {}
    if not style_str:
        return styles
    
    items = style_str.split(';')
    for item in items:
        if ':' in item:
            key, value = item.split(':', 1)
            styles[key.strip()] = value.strip()
    return styles

def process_element(elem):
    """
    处理单个 XML 元素：
    1. 将 style 属性转换为 XML 属性
    2. 赋予默认填充色，防止 Word 显示黑块
    """
    # 获取原本的 style 属性
    style_str = elem.get('style')
    if style_str:
        styles = parse_style_string(style_str)
        
        # 需要转换的关键属性列表 (Word 更喜欢属性而不是 CSS)
        attr_map = ['fill', 'stroke', 'stroke-width', 'font-size', 'font-family']

        # 1. 将 style 中的定义提取为 XML 属性
        for key, value in styles.items():
            if key in attr_map:
                # 如果 XML 属性不存在，则用 style 里的值覆盖
                if elem.get(key) is None:
                    elem.set(key, value)
        
        # 2. 移除 style 属性 (避免 Word 混淆)
        del elem.attrib['style']

    # 3. 针对 Word "黑块" 问题的特殊补丁
    # Mermaid 的节点通常是 rect, circle, polygon, ellipse
    # 去掉可能的命名空间前缀
    tag_name = elem.tag.split('}')[-1] 
    
    if tag_name in ['rect', 'circle', 'ellipse', 'polygon']:
        # 如果没有 fill 属性，Word 默认会渲染成黑色。
        # 这里强制给一个默认底色 (Mermaid 默认淡紫/淡蓝)
        if 'fill' not in elem.attrib:
             elem.set('fill', '#ECECFF') # Mermaid 默认节点色
        
        # 如果没有 stroke，给个边框色
        if 'stroke' not in elem.attrib:
             elem.set('stroke', '#9370DB') # 默认边框色

def process_svg_file(input_path):
    """
    读取并格式化单个 SVG 文件
    """
    if not os.path.exists(input_path):
        print(f"[Error] File not found: {input_path}")
        return

    folder, filename = os.path.split(input_path)
    new_filename = f"new_{filename}"
    output_path = os.path.join(folder, new_filename)

    try:
        tree = ET.parse(input_path)
        root = tree.getroot()

        # ==================== 修复的核心逻辑 START ====================
        # 建立父子关系映射 (Parent Map)
        # 因为 ElementTree 不支持直接找父节点，我们需要自己遍历一遍
        parent_map = {c: p for p in root.iter() for c in p}

        # 查找所有 style 标签 (无论嵌套多深)
        # 注意：这里要用 list() 包裹，因为我们在迭代过程中会修改树结构
        for style in list(root.findall('.//svg:style', NS)):
            # 找到它的父节点，从父节点中移除它
            if style in parent_map:
                parent_map[style].remove(style)
            else:
                # 如果它是根节点的直接子节点 (虽然在 parent_map 也能处理，双重保险)
                root.remove(style)
        # ==================== 修复的核心逻辑 END ======================

        # 2. 遍历所有元素进行处理
        # 使用 XPath 查找所有常见绘图元素
        tags = ['g', 'rect', 'circle', 'ellipse', 'polygon', 'path', 'line', 'text']
        for tag in tags:
            for elem in root.findall(f'.//svg:{tag}', NS):
                process_element(elem)

        # 3. 保存文件
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
        print(f"[Success] Processed: {filename} -> {new_filename}")

    except ET.ParseError:
        print(f"[Error] Could not parse XML: {input_path}")
    except Exception as e:
        print(f"[Error] Failed to process {input_path}: {str(e)}")
        # 打印详细堆栈以便调试
        import traceback
        traceback.print_exc()

def main():
    parser = argparse.ArgumentParser(
        description="Format Mermaid SVGs for Microsoft Word compatibility.",
        epilog="Example: python format_svg_to_word.py --folder ./docs/images"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--folder', type=str, help="Path to the folder containing SVG files.")
    group.add_argument('--file', type=str, help="Path to a single SVG file.")

    args = parser.parse_args()

    if args.file:
        process_svg_file(args.file)
    
    elif args.folder:
        if not os.path.isdir(args.folder):
            print(f"[Error] Folder not found: {args.folder}")
            return
        
        files = [f for f in os.listdir(args.folder) if f.lower().endswith('.svg') and not f.startswith('new_')]
        if not files:
            print(f"[Info] No original SVG files found in {args.folder}")
            return
        
        print(f"Found {len(files)} SVG files in {args.folder}...")
        for f in files:
            process_svg_file(os.path.join(args.folder, f))

if __name__ == "__main__":
    main()