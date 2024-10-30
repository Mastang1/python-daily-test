from HTMLTable import HTMLTable

def creat_email_html(table_name, rows_text):
    '''
    生成邮件正文内容，HTML格式
    '''
    # 标题内容
    # table = HTMLTable(caption="xxxUI自动化测试结果（附件为报告详情）")
    table = HTMLTable(caption=table_name)
 
    # 没有实现空行
    table.append_data_rows('')
 
    # 表头
    table.append_header_rows((
        ('SN', 'test case', 'result', 'test step information'),
    ))
    lineSteps = r'''
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
today is a nice day\n
'''
    for it in range(30):
        table.append_data_rows((
            (it, lineSteps, 'passed', 'test step information'),
        ))
    # table.append_data_rows(rows_text)
 
    # 标题样式
    caption_style = {
        'text-align': 'center',
        'cursor': 'pointer'
    }
    table.caption.set_style(caption_style)
 
    # 设置边框
    border_style = {
        'border-color': '#000',
        'border-width': '1px',
        'border-style': 'solid',
        'border-collapse': 'collapse',
        # 实现表格居中
        'margin': 'auto',
    }
    # 外边框
    table.set_style(border_style)
    # 单元格边框
    table.set_cell_style(border_style)
 
    # 单元格样式
    # 先得设置cell_style，cell_style包括header_cell_style，会把header_cell_style配置覆盖
    cell_style = {
        'text-align': 'center',
        'padding': '4px',
        'background-color': '#ffffff',
        'font-size': '0.95em',
    }
    table.set_cell_style(cell_style)
 
    # 表头样式
    header_cell_style = {
        'text-align': 'center',
        'padding': '4px',
        'background-color': '#aae1fe',
        'color': '#FFFFFF',
        'font-size': '0.95em',
    }
    table.set_header_cell_style(header_cell_style)
 
    # 如果通过率小于80%，标红
    # for row in table.iter_data_rows():
    #     # 共 28，通过 24，通过率= 85.71%
    #     tmp_value = row[3].value
    #     # 85.71%
    #     # tmp_res = re.findall(r".+?通过率= (.+)", tmp_value)[0]
    #     # 85.71
    #     res = tmp_value.strip('%')
    #     if float(res) < 80:
    #         # 通过率<80%，标红
    #         row[3].set_style({
    #             'background-color': '#ffdddd',
    #         })
 
    # 生产HTML
    html = table.to_html()
    print(type(html))
    return html

tabHeader = '''
MPECAN test report
'''

html = creat_email_html(tabHeader, 'How to do???')
with open('test.html', 'w') as htmlFile:
    htmlFile.write(str(html))