import pdfplumber

def check_pdf_has_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                if page.extract_text().strip():
                    return True
        return False
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False

if __name__ == "__main__":

    no_text_pdf_list = []
    for i in range(1035):
        path = f"D:\\NTCUST\\Project\\Competition\\AI_CUP\\競賽資料集\\reference\\finance\\{i}.pdf"
        if not check_pdf_has_text(path):
            no_text_pdf_list.append(i)
        if i % 100 == 0:
            print(f"Processed {i} PDFs")

    print("no_text_pdf_list: ", no_text_pdf_list)