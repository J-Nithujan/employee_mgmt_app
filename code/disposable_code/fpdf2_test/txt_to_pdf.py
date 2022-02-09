# from fpdf import FPDF
#
#
# class PDF(FPDF):
#     def content(self, filepath):
#         with open(filepath, 'r') as fh:
#             txt = fh.read().replace(u'\u2030', '\'').encode('utf-8').decode()
#         self.set_font('helvetica', size=12)
#         self.multi_cell(0, 5, txt)
#         self.ln()
#
#
# pdf = PDF()
# pdf.add_page()
# pdf.content('example.txt')
# pdf.output("example.pdf")
#
# CONCLUSION:
# Too much complicated / time-consuming to handle if there are lots of special characters => won't be used in the
# project

