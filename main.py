from Ashare import *
import pandas as pd
from datetime import datetime

# 1. 设置参数
target_stock = 'sh600900'  # 长江电力
start_date = '2024-09-18'  # 你的起始日期
# 自动获取今天的日期作为结束日期
end_date = datetime.now().strftime('%Y-%m-%d')

def run_task():
    print(f"正在获取 {target_stock} 从 {start_date} 到 {end_date} 的行情...")
    
    try:
        # 2. 调用接口获取区间数据
        # 注意：这里我们去掉了 count，改用指定的日期区间
        df = get_price(target_stock, frequency='1d', start_date=start_date, end_date=end_date)
        
        if df is None or df.empty:
            print("未能获取到数据，请检查日期或网络。")
            return

        # 3. 预览数据
        print(f"成功获取 {len(df)} 个交易日的数据。")
        print(df.head()) # 显示前几行（9月18日左右的数据）

        # 4. 保存文件（增加 utf-8-sig 解决 Excel 打开乱码问题）
        output_file = 'stock_600900_since_20240918.csv'
        df.to_csv(output_file, encoding='utf-8-sig')
        print(f"\n文件已保存为: {output_file}")

    except Exception as e:
        print(f"运行出错: {e}")

if __name__ == "__main__":
    run_task()
