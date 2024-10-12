from bs4 import BeautifulSoup


def extract_csv_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='waffle')
    result = []

    if not table:
        print("CSV table not found.")
        return result

    rows = table.find_all('tr')
    for row in rows:
        row_data = [td.get_text(strip=True) for td in row.find_all('td')]
        result.append(row_data)

    return result