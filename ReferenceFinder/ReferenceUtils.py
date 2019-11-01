from docx import Document


class ReferenceUtils:

    @staticmethod
    def __save_references_file(txt_file_name, lst_txt_result):

        try:
            my_doc = open(txt_file_name, 'w', encoding='utf-8')
            for p in lst_txt_result:
                my_doc.writelines(str(p).strip() + '\n')
            my_doc.close()
        except Exception as e:
            print('error!', e)

    def find_references(self, docx_file_path, result_file_path):
        ls_txt_data = []
        mode = False
        temp_txt = ''
        document = Document(docx_file_path)
        for para in document.paragraphs:
            all_para_txt = str(para.text)
            for char in all_para_txt:
                if char == '(':
                    mode = True
                if mode:
                    temp_txt = temp_txt + char
                if char == ')':
                    mode = False
                    if 8 < len(temp_txt) < 100 and self.__has_numbers(temp_txt):
                        ls_txt_data.append(temp_txt.strip()[1:-1])
                    temp_txt = ''
        ls = list(set(ls_txt_data))
        ls.sort()
        self.__save_references_file(result_file_path, ls)
        return ls

    @staticmethod
    def __has_numbers(input_str):
        return any(char.isdigit() for char in input_str)
