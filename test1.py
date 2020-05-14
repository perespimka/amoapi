from docxtpl import DocxTemplate


def test_temlp():
    doc = DocxTemplate('TEST.docx')
    context = {
        'position_from_card': 'sex v govno', 
        'tbl': [
            {'col1': 'val1', 'col2': 'val2', 'col3': 'val3' }, 
            {'col1': 'val1a', 'col2': 'val2a', 'col3': 'val3a' }
        ]
    }



    doc.render(context)
    doc.save('vgovno_tab.docx')


if __name__ == "__main__":
    test_temlp()