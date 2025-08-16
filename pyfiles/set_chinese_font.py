import matplotlib.pyplot as plt
import platform

def set_chinese_font():
    """
    根据操作系统设置matplotlib的中文显示字体。
    """
    sys_name = platform.system()
    
    if sys_name == 'Windows':
        font_list = ['SimHei', 'Microsoft YaHei', 'STHeiti']
    elif sys_name == 'Darwin':  # macOS
        font_list = ['Arial Unicode MS', 'Hiragino Sans GB', 'STHeiti']
    elif sys_name == 'Linux':
        font_list = ['WenQuanYi Zen Hei', 'AR PL UMing CN', 'DejaVu Sans']
    else:
        # 默认回退到通用字体
        font_list = ['sans-serif']

    # 遍历字体列表，找到第一个可用的字体
    # 注：matplotlib会按照列表顺序寻找字体
    for font in font_list:
        try:
            plt.rcParams['font.sans-serif'] = [font]
            # 解决负号显示问题
            plt.rcParams['axes.unicode_minus'] = False
            print(f"成功设置为 {font} 字体。")
            return
        except KeyError:
            continue
    
    print("警告: 未找到合适的中文显示字体，可能无法正常显示。")