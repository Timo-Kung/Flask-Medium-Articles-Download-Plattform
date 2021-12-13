import pdfkit


url = r"https://towardsdatascience.com/python-go-from-rookie-to-rockstar-d03fa07a32e8"
to_file = 'F:\Flask\music_platform\webpage_html'

def url_to_pdf(url, to_file):
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_url(url, to_file, configuration=config)
    print('完成')

url_to_pdf(url, 'F:\Flask\music_platform\webpage_html\out_1.pdf')