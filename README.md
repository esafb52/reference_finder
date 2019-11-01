

## this is basic tools for finding reference in papers 

[Visit GitHub!(https://github.com/esafb52/reference_finder)]

### using sample code: 


from ReferenceFinder import ReferenceUtils  

if __name__ == '__main__':        
    docx_file_path = 'paper.docx'        
    result_file_path = 'final_reference_result.txt'       
    ref_finder = ReferenceUtils()          
    ref_finder.find_references(docx_file_path, result_file_path)              
    print('find references complete  !!!!!!')            
