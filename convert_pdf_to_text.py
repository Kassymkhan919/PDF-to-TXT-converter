import PySimpleGUI as sg
import os.path
import pdftotext

sg.theme('GreenTan')

file_list_column = [
    [
        sg.Text("PDF Folder"),
        sg.In(size=(25,1), enable_events=True,key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),key="-FILE LIST-"
            )
    ],
]

image_viewer_column = [
    [sg.Text("Choose an Image from list on left:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
     [sg.Image(key="-IMAGE-")],
    ]

layout = [
     [
         sg.Column(file_list_column),
         sg.VSeparator(),
        #  sg.Column(image_viewer_column),
        sg.Button('Convert',bind_return_key=True)
     ]
 ]   




# Code to convert pdf to text
# 


# print(len(pdf))

# text_resume = '\n\n'.join(pdf)
# print(text_resume)
# save text
# with open('resume.txt', 'w') as file:
    # file.write(text_resume)

def getTextFromPDF(filename):
    with open(filename, 'rb') as file:
        pdf = pdftotext.PDF(file)

    text_resume = '\n\n'.join(pdf)
    with open('filename.txt', 'w') as file:
        file.write(text_resume)
    return 0


window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
                # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith(".pdf")
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "Convert":
        getTextFromPDF(filename)
        print(filename)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values['-FILE LIST-'][0]
            )
            # window["-TOUT-"].update(filename)
            # window["-IMAGE-"].update(filename=filename)
            
        except:
            pass

window.close()




# layout = [[sg.Text('Hello from PYSimpleGUI')], [sg.Button("OK")]]
# window = sg.Window("PDF Converter", layout)
# while True:
#     event, values = window.read()
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break
# window.close()


