import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

st.title("📈 Performance Ratio (PR) Evolution Visualizer")


uploaded_file = st.file_uploader("Upload your CSV file (must include Date, PR, GHI columns)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    df=df.drop_duplicates(subset="Date")
    

    df = df.sort_values(by='Date')
    df.set_index('Date', inplace=True)


    min_date = df.index.min().date()
    
    max_date = df.index.max().date()

    start_date = st.date_input("Select start date", min_value=min_date, max_value=max_date, value=min_date)
    
    end_date = st.date_input("Select end date", min_value=min_date, max_value=max_date, value=max_date)

    if start_date > end_date:
        st.error("Start date must be before end date.")
    else:
        df_range = df.loc[start_date:end_date]

        if df_range.empty:
            
            st.warning("No data available for the selected range.")
        else:
            
            def get_budget(date):
                base_value = 73.9
                start_year = 2019
                year_index = (date.year - start_year) if date.month >= 7 else (date.year - start_year - 1)
                return base_value * ((1 - 0.008) ** year_index)

            df_range["Budget_Pr"] = df_range.index.to_series().apply(get_budget).round(3)

           
            df_range["PR_30"] = df_range["PR"].rolling(window=30, min_periods=1).mean()

            
            def ghi_color(ghi):
                if ghi < 2:
                    return 'navy'
                elif ghi < 4:
                    return 'lightblue'
                elif ghi < 6:
                    return 'orange'
                else:
                    return 'brown'

            df_range["Color"] = df_range["GHI"].apply(ghi_color)

         
            fig, ax = plt.subplots(figsize=(14, 7))
            ax.scatter(df_range.index, df_range["PR"], c=df_range["Color"], s=15, label="Daily PR")
            
            ax.plot(df_range.index, df_range["PR_30"], color='red', label="30d moving average of PR", linewidth=2)
            
            ax.plot(df_range.index, df_range["Budget_Pr"], color='darkgreen', label="Budget PR", linewidth=2)

      
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
            plt.xticks(rotation=45)
            ax.set_ylabel("Performance Ratio")
            
            ax.set_ylim(0, 100)
            ax.set_title(f"Performance Ratio Evolution\nFrom {start_date} to {end_date}")

           
            custom_lines = [
                
                Line2D([0], [0], color='navy', marker='o', linestyle='', label='< 2'),
                
                Line2D([0], [0], color='lightblue', marker='o', linestyle='', label='2 - 4'),
                
                Line2D([0], [0], color='orange', marker='o', linestyle='', label='4 - 6'),
                
                Line2D([0], [0], color='brown', marker='o', linestyle='', label='> 6'),
                
                Line2D([0], [0], color='red', label='30-d moving average'),
                Line2D([0], [0], color='darkgreen', label='Budget PR')
                
            ]
            ax.legend(handles=custom_lines, loc='upper left')

            st.pyplot(fig)

           
            st.subheader("Average PR Metrics")
            st.write(f"**Average PR in range:** {df_range['PR'].mean():.2f} %")
            st.write(f"**Average PR Lifetime (entire dataset):** {df['PR'].mean():.2f} %")
