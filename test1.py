from docxtpl import DocxTemplate
import time


def test_templ():
    doc = DocxTemplate('TEST.docx')
    context = {
        'position_from_card': 'sex v govno', 
        'tbl': [
            {'col1': 'val1', 'col2': 'val2', 'col3': 'val3' }, 
            {'col1': 'val1a', 'col2': 'val2a', 'col3': 'val3a' }
        ]
    }



    doc.render(context)
    doc.save('venv/vgovno_trab.docx')

def test_string():
    ax = 'sss'
    a = (f'{ax}asdsd'
         f'  s {ax}'
    )
    print(a)

def time_test():
    now = time.strftime('%d-%m-%Y', time.localtime())
    print(now)
if __name__ == "__main__":
    test_templ()