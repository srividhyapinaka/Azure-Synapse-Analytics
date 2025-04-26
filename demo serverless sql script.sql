select Category,sum(Total_Fat) as Total_fat from OPENROWSET(
    BULK 'https://sriadlsgen2synpase.dfs.core.windows.net/srifilesystemsynpase/menu_data.csv',
    FORMAT = 'CSV',
    HEADER_ROW = TRUE,
    PARSER_VERSION = '2.0'
    )as query1
    GROUP BY Category