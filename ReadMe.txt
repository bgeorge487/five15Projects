I was tasked with creating a fillable PDF by someone I work for.

Since I'm terrible with word processors I decided to see if there was a Python library available for this task, and of course there was!
Following the documentation for the borb library (https://github.com/jorisschellekens/borb) I decided to try my hand at it.

I finished up the current iteration on 04/04/2024
I learned to batch add to a layout, as evidenced by the reserved spaces section:

```
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
```
As I continue to learn this library I hope to further update the formatting of the page. If I decide to return to a word editor to finish my task, I will periodically return to practice my Python.