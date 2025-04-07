from fpdf import FPDF

class Shirtificate:
    def __init__(self, name=None):
        self.name = self.get_name()
        self.generate_pdf()

    def get_name(self):
        name = input("Name: ").strip()
        return name

    def generate_pdf(self):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.image("shirtificate.png", x=18, y=80, w=175)
        pdf.set_font("Helvetica", size=45, style="B")
        pdf.cell(0, 30, "CS50 Shirtificate", align="C")
        pdf.set_font("Helvetica", "B", size=25)
        pdf.set_text_color(255, 255, 255)
        pdf.ln(pdf.eph/2)
        pdf.cell(0, 0, f"{self.name.capitalize()} took CS50P", align="C")
        pdf.output("shirtificate.pdf")

def main():
    shirt = Shirtificate()


if __name__ == "__main__":
    main()

# PASS
