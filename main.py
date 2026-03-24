from Ashare import *
import pandas as pd

# 1. 设置目标日期
target_stock = 'sh600900'
start_date_str = '2024-09-18'

def run_task():
    print(f"开始获取 {target_stock} 的历史数据...")
    
    try:
        # 2. 索性取足够长的数据（比如 500 个交易日，肯定能覆盖到 2024年9月）
        # Ashare 的 get_price 通常只支持 count 参数
        df = get_price(target_stock, frequency='1d', count=500)
        
        if df is None or df.empty:
            print("未能获取到数据。")
            return

        # 3. 将索引转换为日期格式，方便我们按日期“切菜”
        df.index = pd.to_datetime(df.index)
        
        # 4. 只保留 2024-09-18 以后的数据
        df_filtered = df[df.index >= start_date_str]

        # 5. 打印结果预览
        print(f"过滤后的数据从 {df_filtered.index.min()} 到 {df_filtered.index.max()}")
        print(f"共计 {len(df_filtered)} 个交易日。")
        print(df_filtered.head()) 

        # 6. 保存文件（注意：文件名最好简洁，方便 YAML 找）
        output_file = 'stock_600900_history.csv'
        df_filtered.to_csv(output_file, encoding='utf-8-sig')
        print(f"\n文件已成功保存为: {output_file}")

    except Exception as e:
        print(f"运行出错: {e}")

if __name__ == "__main__":
    run_task()
