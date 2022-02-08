from fpdf import FPDF


class PDF(FPDF):
    def content(self, filepath):
        with open(filepath, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('arial', size=12)
        self.multi_cell(0, 5, txt)
        self.ln()


pdf = PDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt="hello world", align='R')
pdf.ln()
pdf.content('example.txt')
pdf.output("hello_world.pdf")
