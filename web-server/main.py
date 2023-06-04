import store 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4,5]


@app.get('/contact',response_class= HTMLResponse)
def get_dict():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap" rel="stylesheet">
    <title>Document</title>
    <style>
        :root{
            --very-light-pink:#c7c7c7;
            --text-input-field:#f7f7f7;
            --hospital-green:#ACD9b2;
            --white:#FFFFFF;
            --black:#000000;
            --sm:14px;
            --md:16px;
            --lg:18px;
        }
        body{
            font-family: 'Quicksand', sans-serif;
            margin:0;
        }
        .my-order{
            width: 100%;
            height: 100vh;
            display: grid;
            place-items: center;
        }
        .Titulo{
            font-size: var(--lg);
            margin-bottom: 40px;
        }
        .my-order-container{
            display: grid;
            grid-template-rows: auto 1fr auto;
            width: 300px;
        }

        .my-order-content{
            display: flex;
            flex-direction: column;
        }

        .orden {
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 16px;
            align-items: center;
            background-color: var(--text-input-field);
            margin-bottom: 16px;
            border-radius: 8px;
            padding: 0 24px;
        }

        .orden p:nth-child(1){
            display: flex;
            flex-direction: column;
        }

        .orden p span:nth-child(1){
            font-size: var(--md);
            font-weight: bold;
        }
        .orden p span:nth-child(2){
            font-size: var(--sm);
            color: var(--very-light-pink);
        }
        .orden p:nth-child(2){
           text-align: end;
           font-weight: bold;
        }
        .shopping {
            display: grid;
            grid-template-columns: auto 1fr auto auto;
            gap: 16px;
            margin-bottom: 24px;
            align-items: center;
        }
        .shopping figure img{
            width: 70px;
            height: 70px;
            border-radius: 20px;
            object-fit: cover;
        }
        .shopping figure {
            margin: 0;
        }

        .shopping p:nth-child(2){
            color: var(--very-light-pink);
        }

        .shopping p:nth-child(3){
            font-size: var(--md);
            font-weight: bold;
        }



    </style>
    </head>
    <body>
        <div class="my-order">
            <div class="my-order-container">
                <h1 class="Titulo"> Mi Orden</h1>
                <div class="my-order-content">
                    <div class="orden">
                        <p>
                            <span> 27-05-2023</span>
                            <span> 6 articulos</span>
                        </p>
                        <p>$560.00</p>
                    </div>
            
                    <div class="shopping">
                        <figure>
                            <img src="https://images.pexels.com/photos/100582/pexels-photo-100582.jpeg?auto=compress&cs=tinysrgb&w=400" alt="cicla" class="producto-img">
                        </figure>
                        <p>Bike</p>
                        <p>$30.00</p>
                    </div>

                    <div class="shopping">
                        <figure>
                            <img src="https://images.pexels.com/photos/1298601/pexels-photo-1298601.jpeg?auto=compress&cs=tinysrgb&w=400" alt="" class="producto-img">
                        </figure>
                        <p>Control Xbox</p>
                        <p>$60.00</p>
                    </div>

                    <div class="shopping">
                        <figure>
                            <img src="https://images.pexels.com/photos/16776031/pexels-photo-16776031.jpeg?auto=compress&cs=tinysrgb&w=400" alt="" class="producto-img">
                        </figure>
                        <p>Xbox Series X</p>
                        <p>$600.00</p>
                    </div>
                </div>
            </div>
        </div> 
        
    </body>
    </html>
"""

def run():
    store.get_categories()

if __name__ == '__main__':
    run()