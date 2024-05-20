from createapp import create_app

def main():
    try:
        app = create_app()
        app.run(debug=True)  
    except Exception as e:
        print(e)  

if __name__ == '__main__':
    main()
