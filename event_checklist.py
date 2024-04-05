from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.flexible_column_width_table import FlexibleColumnWidthTable
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.forms.text_field import TextField
from borb.pdf.canvas.layout.forms.text_area import TextArea
from borb.pdf.canvas.layout.forms.check_box import CheckBox
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.forms.drop_down_list import DropDownList
from decimal import Decimal

def main():
    # Create an empty document
    pdf = Document()

    # Create an empty page
    page = Page()

    # Add the page to the document
    pdf.add_page(page)

    # Create PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # Heading
    layout.add(Paragraph("Event Checklist", horizontal_alignment=Alignment.CENTERED,font="Helvetica",font_size=Decimal(24)))

    # Table to layout the page
    tableContact: FlexibleColumnWidthTable = FlexibleColumnWidthTable(number_of_rows=3,number_of_columns=4)
    
    # Event Name
    tableContact.add(Paragraph("Event Name: ",horizontal_alignment=Alignment.RIGHT, font_size=Decimal(12), font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

    # Event Date
    tableContact.add(Paragraph("Event Date: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

    # Contact Name
    tableContact.add(Paragraph("Contact Name: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

    # Contact Phone
    tableContact.add(Paragraph("Contact Address: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

    # Contact Email
    tableContact.add(Paragraph("Contact Email: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

    # Contact Phone
    tableContact.add(Paragraph("Contact Phone: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    tableContact.add(TextField(value="",font_size=Decimal(10)))

 
    # Table Properties
    tableContact.set_padding_on_all_cells(Decimal(5),Decimal(5),Decimal(5),Decimal(5))
    tableContact.no_borders()

    # Add the table to the page layout
    layout.add(tableContact)

    # Social Media Header
    layout.add(Paragraph("Social Media:",horizontal_alignment=Alignment.LEFT,font="Helvetica", font_size=Decimal(12)))

    # Table for Socials
    socialMediaTable: FlexibleColumnWidthTable = FlexibleColumnWidthTable(number_of_rows=2,number_of_columns=4)
    # Social Media Fields

    #Facebook
    socialMediaTable.add(Paragraph("Facebook: ",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    socialMediaTable.add(TextField(value="",font_size=Decimal(10)))
    
    #Instagram
    socialMediaTable.add(Paragraph("Instagram: @",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    socialMediaTable.add(TextField(value="",font_size=Decimal(10)))

    #TikTok
    socialMediaTable.add(Paragraph("TikTok: @",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    socialMediaTable.add(TextField(value="",font_size=Decimal(10)))

    #Twitter/X
    socialMediaTable.add(Paragraph("Twitter/X: @",horizontal_alignment=Alignment.RIGHT,font="Helvetica"))
    socialMediaTable.add(TextField(value="",font_size=Decimal(10),padding_left=Decimal(0)))

    # Add table to layout:
    socialMediaTable.set_padding_on_all_cells(Decimal(5),Decimal(5),Decimal(5),Decimal(5))
    socialMediaTable.no_borders()
    layout.add(socialMediaTable)
    
    # Travel Section
    layout.add(
        FlexibleColumnWidthTable(number_of_rows=1,number_of_columns=4)
        .add(Paragraph("Will there be travel? (Check for yes)",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12),padding_top=Decimal(1)))
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("If yes, do you need a hotel room?",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12),padding_left=Decimal(2)))
        .add(CheckBox(font_size=Decimal(10)))        
        .set_padding_on_all_cells(Decimal(2),Decimal(2),Decimal(2),Decimal(2))
        .no_borders()
    )

    # Header for reserved spaces
    layout.add(Paragraph("Space Reserved (Check all that apply):",horizontal_alignment=Alignment.LEFT,font="Helvetica", font_size=Decimal(12)))
    # Space(s) Reserved
    layout.add(
        FlexibleColumnWidthTable(number_of_rows=1, number_of_columns=10)
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("Pronto Dining Room",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12)))
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("Pronto Patio",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12),padding_left=Decimal(2)))
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("Pronto Bar",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12),padding_left=Decimal(2)))
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("Pronto Spare Room",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12)))
        .add(CheckBox(font_size=Decimal(10)))
        .add(Paragraph("Five15",horizontal_alignment=Alignment.RIGHT,font="Helvetica",font_size=Decimal(12),padding_left=Decimal(2)))        
        .set_padding_on_all_cells(Decimal(2),Decimal(2),Decimal(0),Decimal(0))
        .no_borders()
    )

    # Attempt to store PDF
    with open("EventChecklist.pdf","wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)

if __name__ == '__main__':
    main()
