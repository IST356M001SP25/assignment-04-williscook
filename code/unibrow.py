import pandas as pd
import streamlit as st
import pandaslib as pl

# TODO Write code here to complete the unibrow.py
st.title("UniBrow")
st.caption("The Universal Data Browser")

file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])

if file:
    file_extension = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_extension)

    columns = pl.get_column_names(df)
    selected_columns = st.multiselect("Select columns to display", columns, default=columns)

    filter_data = st.checkbox("Filter data")

    if filter_data:
        st.subheader("Filter Data")

        columns_for_filter = pl.get_columns_of_type(df, 'object')
        
        if columns_for_filter:
 
            filter_column = st.selectbox("Select column to filter", columns_for_filter)
            if filter_column:
                unique_values = pl.get_unique_values(df, filter_column)
                selected_value = st.selectbox("Select value to filter by", unique_values)

                filtered_df = df[df[filter_column] == selected_value][selected_columns]
        else:
            st.warning("No columns available to filter on.")
            filtered_df = df[selected_columns]
    else:
        filtered_df = df[selected_columns]

    st.dataframe(filtered_df)

    st.subheader("Summary Statistics")
    st.dataframe(filtered_df.describe())

