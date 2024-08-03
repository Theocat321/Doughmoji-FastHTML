from fasthtml.common import *

css = Style('''
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
    body, html { height: 100%; margin: 0; font-family: 'Roboto', sans-serif; }
    body { display: flex; flex-direction: column; }
    main { flex: 1 0 auto; }
    footer { flex-shrink: 0; padding: 10px; text-align: center; background-color: #333; color: white; }
    footer a { color: #9cf; }
    .main-button{background-color: #FF6F61; color: black; border-radius:25px; filter: drop-shadow(5px 2px 3px #000000); width:fit-content; padding: 10px 20px; font-size: 20px; }
    h1{font-size: 3em; font-weight: bold; font-family: 'Oswald', sans-serif;}
            
    .black{color: black;}
''')

app = FastHTML(hdrs=(picolink,css))

@app.get("/")
def get():
    return Section(
        # Header
        

        # Main Section
        Div(
            Div(
                H1('DOUGHMOJI',cls='black',style='font-size:72px;margin:0;'),
                P("Creative Doughnuts for Creative People",cls='black', style='font-size:20px;'),
            ),
            Button('SHOP NOW', hx_get='/create', cls='main-button', style='position:absolute; bottom:10%;'),
            style='''
            position: relative;
            display: flex;
            flex-direction: column;
            align-content: center;
            justify-content: center;
            align-items: center;
            text-align:center;
            height: 100vh;
            background: radial-gradient(ellipse at center, #FFFAC2, #F6DE57);
            '''
        )
    )


serve()